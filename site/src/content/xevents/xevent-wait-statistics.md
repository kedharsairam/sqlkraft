---
name: "xevent_wait_statistics"
title: "Wait Statistics Capture with Extended Events"
category: "wait-statistics"
description: "Architect a high-precision wait statistics monitoring pipeline using Extended Events — capture wait_type, wait_time, and blocking_session_id at per-wait granularity without the overhead of sys.dm_os_wait_stats polling."
tags: ["extended-events", "wait-statistics", "wait_info", "performance-monitoring", "sql_os", "diagnostics"]
targetVersion: "SQL Server 2012+"
pubDate: 2026-05-30
---

## Overview

Traditional wait statistics analysis relies on sampling `sys.dm_os_wait_stats` — a cumulative, instance-level view that resets on restart and provides no per-session or per-query granularity. Extended Events offers a dramatically better approach: capture individual wait events as they occur using the `sqlos.wait_info` and `sqlos.wait_info_external` events.

Each event includes:
- **wait_type** — the specific wait type (e.g., `LCK_M_S`, `PAGEIOLATCH_SH`)
- **wait_duration_ms** — how long the wait lasted
- **session_id** — which session experienced the wait
- **blocking_session_id** — the session holding the resource (for lock waits)
- **opcode** — `Begin` (wait started), `End` (wait completed), or `Abort`

## Event Architecture

### wait_info vs. wait_info_external

| Event | Scope | Use Case |
|---|---|---|
| `wait_info` | Internal SQL Server waits (latches, locks, memory, scheduling) | General performance diagnostics |
| `wait_info_external` | External waits (network I/O, disk I/O, CLR, Service Broker) | I/O and external dependency analysis |

For comprehensive coverage, capture both events in the same session.

## Creating a Wait Statistics Capture Session

### Lightweight Session — All Waits Above Threshold

```sql
-- Capture all wait events exceeding 100 ms — ring buffer for live diagnostics
CREATE EVENT SESSION [wait_stats_live]
ON SERVER
ADD EVENT sqlos.wait_info
(
    ACTION
    (
        sqlserver.session_id,
        sqlserver.database_name,
        sqlserver.sql_text,
        sqlserver.client_app_name,
        sqlserver.client_hostname,
        sqlserver.plan_handle
    )
    WHERE
    (
        [opcode] = N'End'                     -- Only capture completed waits
        AND [wait_duration_ms] >= 100          -- Ignore sub-100ms waits
        AND [wait_type] <> N'WAITFOR'          -- Exclude intentional WAITFOR
        AND [wait_type] <> N'BROKER_RECEIVE_WAITFOR'  -- Exclude Service Broker idle
    )
),
ADD EVENT sqlos.wait_info_external
(
    ACTION
    (
        sqlserver.session_id,
        sqlserver.database_name,
        sqlserver.sql_text,
        sqlserver.client_app_name,
        sqlserver.client_hostname
    )
    WHERE
    (
        [opcode] = N'End'
        AND [wait_duration_ms] >= 100
    )
)
ADD TARGET package0.ring_buffer
(
    SET max_events_limit = 10000
)
WITH
(
    MAX_MEMORY = 16384 KB,
    EVENT_RETENTION_MODE = ALLOW_SINGLE_EVENT_LOSS,
    MAX_DISPATCH_LATENCY = 10 SECONDS,
    MAX_EVENT_SIZE = 0 KB,
    MEMORY_PARTITION_MODE = NONE,
    TRACK_CAUSALITY = OFF,
    STARTUP_STATE = OFF
);
GO

ALTER EVENT SESSION [wait_stats_live] ON SERVER STATE = START;
GO
```

### Production-Grade Session with File Output

```sql
-- Persistent wait statistics warehouse for trend analysis
CREATE EVENT SESSION [wait_stats_warehouse]
ON SERVER
ADD EVENT sqlos.wait_info
(
    ACTION (sqlserver.session_id, sqlserver.database_name, sqlserver.sql_text)
    WHERE
    (
        [opcode] = N'End'
        AND [wait_duration_ms] >= 50
        AND [wait_type] <> N'WAITFOR'
        AND [wait_type] <> N'BROKER_RECEIVE_WAITFOR'
        AND [wait_type] <> N'BROKER_TASK_STOP'
        AND [wait_type] <> N'SLEEP_TASK'
    )
),
ADD EVENT sqlos.wait_info_external
(
    ACTION (sqlserver.session_id, sqlserver.sql_text)
    WHERE ([opcode] = N'End' AND [wait_duration_ms] >= 50)
)
ADD TARGET package0.event_file
(
    SET filename = N'D:\XELogs\wait_stats_warehouse.xel',
        max_file_size = 256,
        max_rollover_files = 30
)
WITH
(
    MAX_MEMORY = 16384 KB,
    EVENT_RETENTION_MODE = ALLOW_MULTIPLE_EVENT_LOSS,
    MAX_DISPATCH_LATENCY = 30 SECONDS,
    MAX_EVENT_SIZE = 0 KB,
    MEMORY_PARTITION_MODE = NONE,
    TRACK_CAUSALITY = OFF,
    STARTUP_STATE = ON
);
GO

ALTER EVENT SESSION [wait_stats_warehouse] ON SERVER STATE = START;
GO
```

## Querying Live Wait Data from Ring Buffer

```sql
-- Top wait types by total duration from the live ring buffer
SELECT TOP 25
    event_data.value('(event/data[@name="wait_type"]/text)[1]', 'nvarchar(256)') AS wait_type,
    event_data.value('(event/data[@name="wait_duration_ms"]/value)[1]', 'bigint') AS wait_duration_ms,
    event_data.value('(event/action[@name="session_id"]/value)[1]', 'int') AS session_id,
    event_data.value('(event/action[@name="database_name"]/value)[1]', 'nvarchar(256)') AS database_name,
    event_data.value('(event/action[@name="sql_text"]/value)[1]', 'nvarchar(max)') AS sql_text,
    event_data.value('(event/@timestamp)[1]', 'datetime2') AS event_time
FROM
(
    SELECT CAST(target_data AS XML) AS ring_buffer
    FROM sys.dm_xe_session_targets
    WHERE event_session_address = (
        SELECT [address] FROM sys.dm_xe_sessions WHERE name = 'wait_stats_live'
    )
    AND target_name = 'ring_buffer'
) AS rb
CROSS APPLY rb.ring_buffer.nodes('/RingBufferTarget/event') AS e(event_data)
ORDER BY wait_duration_ms DESC;
```

## Querying the Wait Statistics Warehouse

```sql
-- Top wait types by frequency and total duration from the file archive
WITH WaitData AS
(
    SELECT
        event_data.value('(event/data[@name="wait_type"]/text)[1]', 'nvarchar(256)') AS wait_type,
        event_data.value('(event/data[@name="wait_duration_ms"]/value)[1]', 'bigint') AS wait_duration_ms,
        event_data.value('(event/data[@name="opcode"]/text)[1]', 'nvarchar(50)') AS opcode,
        CAST(event_data.value('(event/@timestamp)[1]', 'datetime2') AS DATETIME2) AS event_time
    FROM
    (
        SELECT event_data
        FROM sys.fn_xe_file_target_read_file
        (
            N'D:\XELogs\wait_stats_warehouse*.xel',
            N'D:\XELogs\wait_stats_warehouse*.xem',
            NULL,
            NULL
        )
    ) AS ft
    CROSS APPLY ft.event_data.nodes('/event') AS e(event_data)
    WHERE event_data.value('local-name(.)', 'varchar(50)') = 'event'
)
SELECT
    wait_type,
    COUNT(*) AS wait_count,
    SUM(wait_duration_ms) AS total_wait_ms,
    AVG(wait_duration_ms) AS avg_wait_ms,
    MAX(wait_duration_ms) AS max_wait_ms,
    SUM(wait_duration_ms) / 1000.0 / 60 AS total_wait_minutes,
    COUNT(*) * 100.0 / SUM(COUNT(*)) OVER () AS pct_of_total_waits
FROM WaitData
WHERE opcode = 'End'
    AND wait_type IS NOT NULL
GROUP BY wait_type
HAVING COUNT(*) > 10
ORDER BY total_wait_ms DESC;
```

### Time-Sliced Wait Analysis

```sql
-- Break down waits into 5-minute buckets for trend visualization
WITH WaitBuckets AS
(
    SELECT
        DATEADD(MINUTE, DATEDIFF(MINUTE, 0, event_time) / 5 * 5, 0) AS bucket_time,
        event_data.value('(event/data[@name="wait_type"]/text)[1]', 'nvarchar(256)') AS wait_type,
        event_data.value('(event/data[@name="wait_duration_ms"]/value)[1]', 'bigint') AS wait_duration_ms
    FROM
    (
        SELECT
            CAST(event_data AS XML) AS event_xml,
            event_data
        FROM sys.fn_xe_file_target_read_file
        (
            N'D:\XELogs\wait_stats_warehouse*.xel',
            N'D:\XELogs\wait_stats_warehouse*.xem',
            NULL,
            NULL
        )
    ) AS ft
    CROSS APPLY ft.event_xml.nodes('/event') AS e(event_data)
)
SELECT
    bucket_time,
    wait_type,
    COUNT(*) AS wait_count,
    SUM(wait_duration_ms) AS total_wait_ms
FROM WaitBuckets
WHERE wait_type IS NOT NULL
GROUP BY bucket_time, wait_type
ORDER BY bucket_time, total_wait_ms DESC;
```

## Correlating Waits with Blocking

When combined with `sqlserver.blocked_process_report`, the wait_info session can identify exactly which blocking chain caused each wait:

```sql
-- Identify lock waits with blocking session details
SELECT
    w.event_time,
    w.session_id AS blocked_session_id,
    w.wait_type,
    w.wait_duration_ms,
    w.sql_text AS blocked_sql_text
FROM
(
    SELECT
        event_data.value('(event/@timestamp)[1]', 'datetime2') AS event_time,
        event_data.value('(event/action[@name="session_id"]/value)[1]', 'int') AS session_id,
        event_data.value('(event/data[@name="wait_type"]/text)[1]', 'nvarchar(256)') AS wait_type,
        event_data.value('(event/data[@name="wait_duration_ms"]/value)[1]', 'bigint') AS wait_duration_ms,
        event_data.value('(event/action[@name="sql_text"]/value)[1]', 'nvarchar(max)') AS sql_text
    FROM
    (
        SELECT CAST(target_data AS XML) AS ring_buffer
        FROM sys.dm_xe_session_targets
        WHERE event_session_address = (
            SELECT [address] FROM sys.dm_xe_sessions WHERE name = 'wait_stats_live'
        )
        AND target_name = 'ring_buffer'
    ) AS rb
    CROSS APPLY rb.ring_buffer.nodes('/RingBufferTarget/event') AS e(event_data)
) AS w
WHERE w.wait_type LIKE 'LCK%'
ORDER BY w.wait_duration_ms DESC;
```

## Performance Overhead Analysis

| Concurrent Workload | Event Volume (waits/sec) | CPU Overhead | Memory Usage |
|---|---|---|---|
| Idle (no user queries) | 5–20 | < 0.1% | 16 MB |
| Light OLTP (100 batches/sec) | 100–500 | 0.5–1% | 16 MB |
| Heavy OLTP (1000+ batches/sec) | 1000–5000 | 2–5% | 16 MB + file I/O |
| With threshold filter ≥ 100ms | 10–100 | < 0.5% | 16 MB |

> **Note:** The overhead drops dramatically when a duration filter is applied. With `wait_duration_ms >= 100`, the session captures only the top ~2% of wait events — the ones that actually matter.

## Comparison: XEvent wait_info vs. sys.dm_os_wait_stats

| Aspect | `wait_info` XEvent | `sys.dm_os_wait_stats` |
|---|---|---|
| **Granularity** | Per-wait, per-session, per-query | Cumulative instance-level |
| **Persistence** | File target stores history | Resets on restart |
| **Duration filter** | Threshold configurable | All waits counted |
| **Overhead** | Adjustable via threshold | Minimal (read from memory) |
| **Root cause** | Links wait to SQL text, plan, session | Aggregate only |

**Use XEvent wait_info when** you need per-query wait analysis, blocking chain investigation, or historical wait trending. **Use `sys.dm_os_wait_stats` when** you want a quick, low-overhead health check of the current wait profile.

## Best Practices

1. **Always filter by `opcode = N'End'`** — the `Begin` event fires before the wait duration is known and provides no useful metric.
2. **Exclude idle waits** — `WAITFOR`, `BROKER_RECEIVE_WAITFOR`, `BROKER_TASK_STOP`, `SLEEP_TASK`, and `SQLTRACE_WAIT_ENTRIES` are not actionable.
3. **Set a duration threshold** — sub-50ms waits account for >95% of event volume but are rarely actionable. Start at 100 ms and tune.
4. **Use `wait_info_external`** separately if focusing on disk I/O or network latency — it isolates external subsystem waits.
5. **Combine with `blocked_process_report`** for comprehensive blocking analysis — the wait_info event captures the blocked side, while blocked_process_report captures the blocker.
6. **Keep the ring buffer session for real-time triage** and the file target session for trending — they serve complementary purposes.
