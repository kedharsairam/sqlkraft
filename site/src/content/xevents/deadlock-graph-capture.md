---
name: "xml_deadlock_report"
title: "Deadlock Graph Capture with xml_deadlock_report"
category: "deadlock"
description: "Production-grade techniques for capturing, querying, and analyzing SQL Server deadlock graphs using the xml_deadlock_report Extended Event, including system_health extraction and dedicated event session setup."
tags: ["extended-events","deadlock","xml_deadlock_report","blocking","deadlock-graph","diagnostics"]
targetVersion: "SQL Server 2012+"
pubDate: "2026-05-30"
---

## Overview

The `xml_deadlock_report` Extended Event fires when SQL Server detects a deadlock and chooses a victim. Each event contains the complete **deadlock graph** — an XML document listing all involved processes, resources (locks), and the victim selection details.

When a deadlock occurs, SQL Server:
1. Detects the cyclic dependency via the lock monitor
2. Selects a victim (typically the session with the lowest deadlock priority or least cost)
3. Rolls back the victim transaction
4. Fires the `xml_deadlock_report` event

The event contains the full deadlock graph XML, which can be queried to identify contention patterns, problematic queries, and lock acquisition order.

## Method 1: Querying Deadlocks from system_health

The system_health session automatically captures `xml_deadlock_report` events in its ring buffer. This is the quickest way to investigate recent deadlocks:

```sql
-- Extract deadlock graphs from the system_health ring buffer
-- Returns the most recent deadlock events with parsed process/resource details
SELECT deadlock.value('(event/@timestamp)[1]', 'datetime2') AS deadlock_time,
 deadlock.query('event/data/value/deadlock') AS deadlock_graph_xml,
 deadlock.value('(event/data[@name="database_name"]/value)[1]', 'nvarchar(256)') AS database_name
FROM (
 SELECT CAST(target_data AS XML) AS session_target
 FROM sys.dm_xe_session_targets
 WHERE event_session_address = (
 SELECT [address] FROM sys.dm_xe_sessions WHERE name = 'system_health'
 )
 AND target_name = 'ring_buffer'
) AS sh
CROSS APPLY sh.session_target.nodes('/RingBufferTarget/event[@name="xml_deadlock_report"]') AS d(deadlock)
ORDER BY deadlock_time DESC;
```

### Parsing the Deadlock Graph into Process-Level Rows

```sql
-- Extract individual processes involved in each deadlock
WITH DeadlockEvents AS (
 SELECT d.value('(event/@timestamp)[1]', 'datetime2') AS deadlock_time,
 d.query('event/data/value/deadlock') AS graph
 FROM (
 SELECT CAST(target_data AS XML) AS target_data
 FROM sys.dm_xe_session_targets
 WHERE event_session_address = (
 SELECT [address] FROM sys.dm_xe_sessions WHERE name = 'system_health'
 )
 AND target_name = 'ring_buffer'
 ) AS sh
 CROSS APPLY sh.target_data.nodes('/RingBufferTarget/event[@name="xml_deadlock_report"]') AS d(event)
)
SELECT deadlock_time,
 p.value('@id', 'varchar(50)') AS process_id,
 p.value('@spid', 'int') AS spid,
 p.value('@ecid', 'int') AS ecid,
 p.value('@transactionname', 'varchar(100)') AS transaction_name,
 p.value('@lasttranstarted', 'datetime2') AS transaction_start_time,
 p.value('@lockmode', 'varchar(20)') AS lock_mode,
 p.value('@clientapp', 'varchar(256)') AS client_application,
 p.value('@hostname', 'varchar(128)') AS host_name,
 p.value('@loginname', 'varchar(128)') AS login_name,
 p.value('@isolationlevel', 'varchar(20)') AS isolation_level,
 p.value('(inputbuf)[1]', 'nvarchar(max)') AS input_buffer
FROM DeadlockEvents
CROSS APPLY graph.nodes('//deadlock/process-list/process') AS p(process)
ORDER BY deadlock_time DESC, spid;
```

## Method 2: Dedicated Deadlock Capture Session

For environments with frequent deadlocks, create a dedicated XEvent session with file-based output for historical analysis:

```sql
-- Create a dedicated deadlock capture session with file target
CREATE EVENT SESSION [deadlock_capture]
ON SERVER
ADD EVENT sqlserver.xml_deadlock_report (
 ACTION (
 sqlserver.database_name,
 sqlserver.client_app_name,
 sqlserver.client_hostname,
 sqlserver.username,
 sqlserver.session_id
 )
 WHERE (
 [sqlserver].[database_name] = N'YourDatabaseName'
 OR [sqlserver].[database_name] IS NULL
 )
)
ADD TARGET package0.event_file (
 SET filename = N'D:\XELogs\deadlock_capture.xel',
 max_file_size = 50,
 max_rollover_files = 5
)
WITH (
 MAX_MEMORY = 2048 KB,
 EVENT_RETENTION_MODE = ALLOW_SINGLE_EVENT_LOSS,
 MAX_DISPATCH_LATENCY = 15 SECONDS,
 MAX_EVENT_SIZE = 0 KB,
 MEMORY_PARTITION_MODE = NONE,
 TRACK_CAUSALITY = ON,
 STARTUP_STATE = ON
);
GO

-- Start the session
ALTER EVENT SESSION [deadlock_capture] ON SERVER STATE = START;
GO
```

### Querying the File-Based Deadlock Archive

```sql
-- Read deadlock events from the file target and parse deadlock graphs
WITH xevents AS (
 SELECT event_data AS deadlock_event
 FROM sys.fn_xe_file_target_read_file (
 N'D:\XELogs\deadlock_capture*.xel',
 N'D:\XELogs\deadlock_capture*.xem',
 NULL,
 NULL
 )
)
SELECT event_data.value('(event/@timestamp)[1]', 'datetime2') AS deadlock_time,
 event_data.value('(event/action[@name="database_name"]/value)[1]', 'nvarchar(256)') AS database_name,
 event_data.value('(event/action[@name="client_app_name"]/value)[1]', 'nvarchar(256)') AS application_name,
 event_data.query('event/data/value/deadlock') AS deadlock_graph
FROM xevents
ORDER BY deadlock_time DESC;
```

## Enabling the Deadlock Trace Flag 1222

For backward compatibility or supplementing XEvent capture, enable trace flag 1222 to write deadlock graphs to the SQL Server error log:

```sql
-- Enable deadlock trace flag globally (requires restart or -T startup parameter)
DBCC TRACEON(1222, -1);
GO

-- Verify the trace flag is active
DBCC TRACESTATUS(1222);
GO
```

After enabling TF 1222, deadlock graphs appear in the error log. Use `sp_readerrorlog` to extract them:

```sql
-- Read deadlock graphs from the error log (TF 1222 must be enabled)
EXEC sp_readerrorlog 0, 1, 'deadlock';
```

## Deadlock Graph XML Structure Reference

Understanding the deadlock graph XML enables programmatic analysis:

```xml
<deadlock>
 <victim-list>
 <victimProcess id="processXXXXXXX" />
 </victim-list>
 <process-list>
 <process id="processXXXXXXX" spid="NN" ecid="0"
 priority="0" logused="0" waitresource="KEY:."
 waittime="XXXX" schedulerid="N" kpid="NNNN"
 status="suspended". >
 <executionStack>
 <frame procname="dbname.schema.procname" line="NN" sqlhandle="." />
 </executionStack>
 <inputbuf>
 /* Full T-SQL batch text */
 </inputbuf>
 </process>
 </process-list>
 <resource-list>
 <keylock hobtid="NNNNNNNNNN" dbid="N" objectname="db.schema.table"
 indexname="index_name" id="lockXXXXXXX" mode="X"
 associatedObjectId="NNNNNNNNNN">
 <owner-list>
 <owner id="processXXXXXXX" mode="X" />
 </owner-list>
 <waiter-list>
 <waiter id="processXXXXXXX" mode="S" requestType="wait" />
 </waiter-list>
 </keylock>
 </resource-list>
</deadlock>
```

### Key Elements

| Element | Description |
|---|---|
| `<victim-list>` | Identifies which session was chosen as the deadlock victim |
| `<process-list>` | All sessions involved in the deadlock cycle |
| `<executionStack>` | Call stack showing which query each session was executing |
| `<inputbuf>` | Full T-SQL batch text for each process |
| `<resource-list>` | Lock resources in contention — keylocks, RID locks, page locks, object locks |
| `<owner-list>` | Sessions currently holding the lock |
| `<waiter-list>` | Sessions waiting to acquire the lock |

## Best Practices

1. **Always capture `xml_deadlock_report` proactively** rather than reactively — deadlock graphs are useless after the fact if you do not have them captured.
2. **Use file targets for persistent deadlock history** — the system_health ring buffer overwrites old events.
3. **Filter by database name** in the WHERE clause of your event session to avoid capturing irrelevant deadlocks.
4. **Set `max_rollover_files` appropriately** — deadlock-heavy workloads can generate hundreds of MB of XEL files per day.
5. **Correlate deadlock timing with application error logs** to identify the precise impact on end users.
6. **Analyze the `inputbuf` and `executionStack`** to pinpoint the exact queries and stored procedures causing contention, then optimize indexing or query patterns.
