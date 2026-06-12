---
name: "Diagnosing Deadlocks in Production"
title: "Diagnosing Deadlocks in Production"
category: "blocking"
severity: "critical"
description: "Step-by-step guide to detect, capture, and analyze SQL Server deadlocks with zero downtime — using system_health, XEvent sessions, trace flags, and deadlock graph XML parsing."
tags: ["deadlock","blocking","xevents","xml_deadlock_report","system-health","victim","lock-contention"]
related: ["xevents/deadlock-graph-capture","xevents/system-health-session","dmvs/sys-dm-exec-requests","dmvs/sys-dm-tran-locks","dmvs/sys-dm-os-waiting-tasks","wait-statistics/lck_m_s","wait-statistics/lck_m_x","wait-statistics/lck_m_sch_m","scripts/to-identify-deadlock"]
pubDate: "2026-05-30"
---

Deadlocks in production are inevitable — two concurrent sessions acquire locks in different orders, forming a cyclic dependency the lock monitor must break by choosing a victim. The victim's transaction is rolled back, and the application receives error 1205.

This guide covers end-to-end deadlock diagnosis: ensuring capture is enabled, extracting deadlock graphs from your running system, parsing the XML to identify root cause, and applying remediation.

## Step 1: Verify Deadlock Capture Is Active

### Check system_health Session

The system_health session automatically includes `xml_deadlock_report`. Verify it is running:

```sql
SELECT name, status FROM sys.dm_xe_sessions WHERE name = 'system_health';
```

If the status is `Running`, deadlock graphs are already being captured in the ring buffer — no configuration needed.

### Fallback: Enable Trace Flag 1222

If you need deadlock output in the error log (for environments where XEvent access is restricted):

```sql
DBCC TRACEON(1222, -1);
DBCC TRACESTATUS(1222);
```

Trace flag 1222 writes full deadlock graphs to the SQL Server error log.

## Step 2: Extract Deadlock Graphs

### From system_health Ring Buffer (Quickest)

```sql
SELECT deadlock.value('(event/@timestamp)[1]', 'datetime2') AS deadlock_time,
 deadlock.query('event/data/value/deadlock') AS deadlock_graph_xml
FROM (
 SELECT CAST(target_data AS XML) AS session_target
 FROM sys.dm_xe_session_targets
 WHERE event_session_address = (SELECT [address] FROM sys.dm_xe_sessions WHERE name = 'system_health')
 AND target_name = 'ring_buffer'
) AS sh
CROSS APPLY sh.session_target.nodes('/RingBufferTarget/event[@name="xml_deadlock_report"]') AS d(deadlock)
ORDER BY deadlock_time DESC;
```

This returns the deadlock graph XML directly — no file I/O, no configuration.

### From Dedicated XEvent Session (Long-Term History)

For environments with frequent deadlocks, create a persistent session as detailed in the [Deadlock Graph Capture](/sqlkraft/xevents/deadlock-graph-capture/) reference. Query the file target with:

```sql
SELECT event_data.value('(event/@timestamp)[1]', 'datetime2') AS deadlock_time,
 event_data.query('event/data/value/deadlock') AS deadlock_graph
FROM sys.fn_xe_file_target_read_file(N'D:\XELogs\deadlock_capture*.xel', NULL, NULL, NULL)
ORDER BY deadlock_time DESC;
```

### From Error Log (TF 1222)

```sql
EXEC sp_readerrorlog 0, 1, 'deadlock-list';
```

Each deadlock entry begins with `deadlock-list` and contains the full victim-list, process-list, and resource-list XML.

## Step 3: Parse the Deadlock Graph

The deadlock graph XML contains three critical sections. Parse it at the process level to identify the root cause:

```sql
-- Parse all processes from the most recent deadlock
WITH DeadlockEvents AS (
 SELECT d.value('(event/@timestamp)[1]', 'datetime2') AS deadlock_time,
 d.query('event/data/value/deadlock') AS graph
 FROM (
 SELECT CAST(target_data AS XML) AS target_data
 FROM sys.dm_xe_session_targets
 WHERE event_session_address = (SELECT [address] FROM sys.dm_xe_sessions WHERE name = 'system_health')
 AND target_name = 'ring_buffer'
 ) AS sh
 CROSS APPLY sh.target_data.nodes('/RingBufferTarget/event[@name="xml_deadlock_report"]') AS d(event)
)
SELECT deadlock_time,
 p.value('@id', 'varchar(50)') AS process_id,
 p.value('@spid', 'int') AS spid,
 p.value('@lockmode', 'varchar(20)') AS lock_mode_held,
 p.value('@clientapp', 'varchar(256)') AS application,
 p.value('@hostname', 'varchar(128)') AS host,
 p.value('@loginname', 'varchar(128)') AS login,
 p.value('@lasttranstarted', 'datetime2') AS transaction_start,
 p.value('(inputbuf)[1]', 'nvarchar(max)') AS query_text
FROM DeadlockEvents
CROSS APPLY graph.nodes('//deadlock/process-list/process') AS p(process)
ORDER BY deadlock_time DESC, spid;
```

### What to Look For

| Signal | Interpretation |
|---|---|
| **Two or more processes** waiting on locks held by each other | Classic cycle deadlock |
| **Victim has lowest deadlock_priority** or rolled back more work | Default victim selection — may not be the least important session |
| **Lock mode X (exclusive)** in both directions | Write-write deadlock — typically from concurrent updates in different orders |
| **Keylock** resources with the same `hobtid` | Contention on the same index — often the B-tree leaf level |
| **inputbuf** shows identical transaction patterns | Application issues the same statements in different orders across sessions |

## Step 4: Identify the Victim and Impacted Queries

The deadlock graph identifies the victim explicitly:

```xml
<victim-list>
 <victimProcess id="processXXXXXXX" />
</victim-list>
```

Cross-reference the victim's `spid` with the parsed results to find:
- The exact query that was rolled back (`inputbuf`)
- The application and host that submitted it
- The transaction start time

Query [sys.dm_exec_requests](/sqlkraft/dmvs/sys-dm-exec-requests/) to see if there are currently any sessions in a pattern that resembles the deadlock.

## Step 5: Remediation Strategies

### Immediate Fixes

```sql
-- Set deadlock priority to protect critical sessions
SET DEADLOCK_PRIORITY HIGH;
-- Or use a numeric value: -10 to 10
SET DEADLOCK_PRIORITY 5;
```

### Application-Level Fixes

1. **Access objects in the same order** across all transactions — the single most effective deadlock prevention strategy
2. **Keep transactions short** — minimize the window for lock contention
3. **Use lower isolation levels** where business logic allows — `READ COMMITTED SNAPSHOT` eliminates many read-write deadlocks
4. **Implement retry logic** — error 1205 should trigger an automatic retry (3 retries minimum)

### Index-Level Fixes

- Add covering indexes to reduce the number of rows locked during `UPDATE` and `DELETE`
- Partition large tables to spread lock contention across multiple lock resources
- Consider `OPTIMIZE_FOR_SEQUENTIAL_KEY` for index pages that are hot spots

## Step 6: Monitor for Recurrence

Set up a dedicated [XEvent deadlock session](/sqlkraft/xevents/deadlock-graph-capture/) with file target for long-term tracking. Query it daily with an agent job:

```sql
-- Daily deadlock report
SELECT
 CAST(event_data AS XML).value('(event/@timestamp)[1]', 'datetime2') AS deadlock_time,
 CAST(event_data AS XML).value('(event/action[@name="database_name"]/value)[1]', 'nvarchar(256)') AS database_name
FROM sys.fn_xe_file_target_read_file(N'D:\XELogs\deadlock_capture*.xel', NULL, NULL, NULL)
WHERE CAST(event_data AS XML).value('(event/@timestamp)[1]', 'datetime2') >= DATEADD(DAY, -1, GETUTCDATE())
ORDER BY deadlock_time DESC;
```

## Key Reference Points

- Related DMVs: [sys.dm_exec_requests](/sqlkraft/dmvs/sys-dm-exec-requests/), [sys.dm_tran_locks](/sqlkraft/dmvs/sys-dm-tran-locks/), [sys.dm_os_waiting_tasks](/sqlkraft/dmvs/sys-dm-os-waiting-tasks/)
- Related waits: [LCK_M_S](/sqlkraft/wait-statistics/lck_m_s/), [LCK_M_X](/sqlkraft/wait-statistics/lck_m_x/), [LCK_M_SCH_M](/sqlkraft/wait-statistics/lck_m_sch_m/)
- Related script: [Identify Deadlock](/sqlkraft/scripts/to-identify-deadlock/)
- Architecture: [Locking Architecture](/sqlkraft/architecture/locking-architecture/), [Deadlock Architecture](/sqlkraft/architecture/deadlocks-architecture/)

## See Also

- [Locking & Blocking Outages](/sqlkraft/cookbook/locking-blocking-outages/) — Broader blocking investigation guide
- [High CPU Diagnostic Path](/sqlkraft/cookbook/high-cpu-diagnostic-path/) — Deadlock detection overhead can manifest as CPU pressure
