---
name: "sp_statement_completed"
title: "Query Performance Tracking with sp_statement_completed"
category: "query-performance"
description: "Capture real-time query execution performance metrics using the sp_statement_completed Extended Event — duration, CPU, reads, writes, and row counts for every completed statement within a stored procedure or batch."
tags: ["extended-events","query-performance","sp_statement_completed","duration","cpu","logical-reads","profiling"]
targetVersion: "SQL Server 2012+"
pubDate: 2026-05-30
---

## Overview

The `sp_statement_completed` Extended Event fires when a T-SQL statement inside a stored procedure or batch finishes executing. It exposes critical performance metrics:

- **duration** — total execution time in microseconds
- **cpu_time** — CPU consumption in microseconds
- **logical_reads** — pages read from the buffer pool
- **writes** — pages modified
- **row_count** — rows affected by the statement
- **nest_level** — nesting depth for nested procedure calls
- **object_id** / **object_name** — the containing procedure

This event is the XEvent replacement for SQL Server Profiler's `SP:StmtCompleted` event class and should be the standard tool for all query-level performance tracing.

## Creating a Query Performance Tracking Session

### Lightweight Session for Short-Term Diagnostics

```sql
-- Create a focused session to capture all statement completions
-- Filter by database to minimize volume
CREATE EVENT SESSION [query_performance_trace]
ON SERVER
ADD EVENT sqlserver.sp_statement_completed (
 ACTION (
 sqlserver.database_name,
 sqlserver.client_app_name,
 sqlserver.client_hostname,
 sqlserver.username,
 sqlserver.session_id,
 sqlserver.plan_handle
 )
 WHERE (
 [sqlserver].[database_name] = N'YourDatabaseName'
 AND [duration] >= 1000000 -- 1 second minimum
 )
)
ADD TARGET package0.ring_buffer
WITH (
 MAX_MEMORY = 8192 KB,
 EVENT_RETENTION_MODE = ALLOW_SINGLE_EVENT_LOSS,
 MAX_DISPATCH_LATENCY = 10 SECONDS,
 MAX_EVENT_SIZE = 0 KB,
 MEMORY_PARTITION_MODE = NONE,
 TRACK_CAUSALITY = OFF,
 STARTUP_STATE = OFF
);
GO

ALTER EVENT SESSION [query_performance_trace] ON SERVER STATE = START;
GO
```

### High-Precision Session with File Output for Historical Analysis

```sql
-- Full-featured session with file target for long-term performance warehouse
CREATE EVENT SESSION [query_performance_warehouse]
ON SERVER
ADD EVENT sqlserver.sp_statement_completed (
 ACTION (
 sqlserver.database_name,
 sqlserver.client_app_name,
 sqlserver.client_hostname,
 sqlserver.username,
 sqlserver.session_id,
 sqlserver.plan_handle,
 sqlserver.sql_text,
 sqlserver.tsql_stack
 )
 WHERE (
 [duration] >= 500000 -- 500 ms threshold
 OR [cpu_time] >= 500000 -- 500 ms CPU threshold
 OR [logical_reads] >= 10000 -- 10,000+ logical reads
 )
)
ADD TARGET package0.event_file (
 SET filename = N'D:\XELogs\query_perf_warehouse.xel',
 max_file_size = 256,
 max_rollover_files = 20
)
WITH (
 MAX_MEMORY = 16384 KB,
 EVENT_RETENTION_MODE = ALLOW_SINGLE_EVENT_LOSS,
 MAX_DISPATCH_LATENCY = 5 SECONDS,
 MAX_EVENT_SIZE = 0 KB,
 MEMORY_PARTITION_MODE = NONE,
 TRACK_CAUSALITY = ON,
 STARTUP_STATE = ON
);
GO

ALTER EVENT SESSION [query_performance_warehouse] ON SERVER STATE = START;
GO
```

## Querying Live Ring Buffer Data

Poll the ring buffer during active diagnostics to identify current bottlenecks:

```sql
-- Read the most recent slow statements from the ring buffer
SELECT TOP 100 event_data.value('(event/@timestamp)[1]', 'datetime2') AS event_time,
 event_data.value('(event/action[@name="database_name"]/value)[1]', 'nvarchar(256)') AS database_name,
 event_data.value('(event/action[@name="session_id"]/value)[1]', 'int') AS session_id,
 event_data.value('(event/data[@name="object_name"]/value)[1]', 'nvarchar(256)') AS object_name,
 event_data.value('(event/data[@name="statement"]/value)[1]', 'nvarchar(max)') AS statement_text,
 event_data.value('(event/data[@name="duration"]/value)[1]', 'bigint') AS duration_us,
 event_data.value('(event/data[@name="cpu_time"]/value)[1]', 'bigint') AS cpu_us,
 event_data.value('(event/data[@name="logical_reads"]/value)[1]', 'bigint') AS logical_reads,
 event_data.value('(event/data[@name="writes"]/value)[1]', 'bigint') AS writes,
 event_data.value('(event/data[@name="row_count"]/value)[1]', 'bigint') AS row_count,
 event_data.value('(event/data[@name="nest_level"]/value)[1]', 'int') AS nest_level
FROM (
 SELECT CAST(target_data AS XML) AS ring_buffer
 FROM sys.dm_xe_session_targets
 WHERE event_session_address = (
 SELECT [address] FROM sys.dm_xe_sessions WHERE name = 'query_performance_trace'
 )
 AND target_name = 'ring_buffer'
) AS rb
CROSS APPLY rb.ring_buffer.nodes('/RingBufferTarget/event') AS e(event_data)
ORDER BY duration_us DESC;
```

## Reading Historical File Target Data

```sql
-- Query historical performance data from the file target
-- Group by procedure to identify the most expensive stored procedures
SELECT object_name,
 COUNT(*) AS execution_count,
 AVG(duration_us / 1000.0) AS avg_duration_ms,
 MAX(duration_us / 1000.0) AS max_duration_ms,
 AVG(cpu_us / 1000.0) AS avg_cpu_ms,
 AVG(logical_reads * 1.0) AS avg_logical_reads,
 AVG(writes * 1.0) AS avg_writes,
 AVG(row_count * 1.0) AS avg_row_count,
 SUM(row_count) AS total_rows_affected
FROM (
 SELECT event_data.value('(event/data[@name="object_name"]/value)[1]', 'nvarchar(256)') AS object_name,
 event_data.value('(event/data[@name="duration"]/value)[1]', 'bigint') AS duration_us,
 event_data.value('(event/data[@name="cpu_time"]/value)[1]', 'bigint') AS cpu_us,
 event_data.value('(event/data[@name="logical_reads"]/value)[1]', 'bigint') AS logical_reads,
 event_data.value('(event/data[@name="writes"]/value)[1]', 'bigint') AS writes,
 event_data.value('(event/data[@name="row_count"]/value)[1]', 'bigint') AS row_count
 FROM (
 SELECT event_data
 FROM sys.fn_xe_file_target_read_file (
 N'D:\XELogs\query_perf_warehouse*.xel',
 N'D:\XELogs\query_perf_warehouse*.xem',
 NULL,
 NULL
 )
 ) AS ft
 CROSS APPLY ft.event_data.nodes('/event') AS e(event_data)
 WHERE event_data.value('local-name(.)', 'varchar(50)') = 'event'
) AS stats
WHERE object_name IS NOT NULL
GROUP BY object_name
ORDER BY avg_duration_ms DESC;
```

## Correlating with Query Store and Plan Handles

When the `plan_handle` action is included, you can join `sp_statement_completed` data with Query Store or `sys.dm_exec_query_stats`:

```sql
-- Correlate XEvent data with actual execution plans
SELECT x.event_time,
 x.object_name,
 x.statement_text,
 x.duration_us / 1000.0 AS duration_ms,
 x.logical_reads,
 qp.query_plan
FROM (
 SELECT event_data.value('(event/@timestamp)[1]', 'datetime2') AS event_time,
 event_data.value('(event/data[@name="object_name"]/value)[1]', 'nvarchar(256)') AS object_name,
 event_data.value('(event/data[@name="statement"]/value)[1]', 'nvarchar(max)') AS statement_text,
 event_data.value('(event/data[@name="duration"]/value)[1]', 'bigint') AS duration_us,
 event_data.value('(event/data[@name="logical_reads"]/value)[1]', 'bigint') AS logical_reads,
 event_data.value('(event/action[@name="plan_handle"]/value)[1]', 'varbinary(64)') AS plan_handle
 FROM (
 SELECT CAST(target_data AS XML) AS ring_buffer
 FROM sys.dm_xe_session_targets
 WHERE event_session_address = (
 SELECT [address] FROM sys.dm_xe_sessions WHERE name = 'query_performance_trace'
 )
 AND target_name = 'ring_buffer'
 ) AS rb
 CROSS APPLY rb.ring_buffer.nodes('/RingBufferTarget/event') AS e(event_data)
) AS x
OUTER APPLY sys.dm_exec_query_plan(x.plan_handle) AS qp
ORDER BY x.event_time DESC;
```

## Filtering Strategies to Minimize Overhead

| Filter Condition | Effect | When to Use |
|---|---|---|
| `duration >= 1000000` | Only captures statements running longer than 1 second | General slow-query hunting |
| `logical_reads >= 10000` | High I/O statements regardless of duration | I/O troubleshooting |
| `cpu_time >= 500000` | CPU-intensive queries | CPU pressure investigations |
| `database_name = N'Prod'` | Scoped to a single database | Production triage |
| `object_name LIKE N'%usp_%'` | Filter by procedure naming pattern | Targeted procedure profiling |

## Comparison: sp_statement_completed vs. sp_statement_started

| Aspect | `sp_statement_completed` | `sp_statement_started` |
|---|---|---|
| **Fires when** | Statement finishes | Statement begins |
| **Includes metrics** | Duration, CPU, reads, writes, row_count | None |
| **Overhead** | Slightly higher (must track metrics) | Minimal |
| **Use case** | Performance analysis, bottleneck detection | Execution flow tracking, deadlock identification |

For most performance diagnostics, **`sp_statement_completed` is preferred** because it includes execution metrics. Use `sp_statement_started` only when you need to detect which statement was executing when a blocking or deadlock event occurred.

## Best Practices

1. **Set realistic duration thresholds** — capturing every statement sub-millisecond completion generates excessive event volume. Start with 1 second and reduce as needed.
2. **Include `plan_handle`** to enable plan correlation via `sys.dm_exec_query_plan()`.
3. **Use `sql_text` action** instead of `statement` data field when you need the full batch text rather than the individual statement.
4. **Filter aggressively by database** in multi-tenant instances to focus on the workload you are diagnosing.
5. **Pair with `sql_batch_completed`** at the session level when you need both batch-level and statement-level granularity.
6. **Avoid using `sp_statement_completed` without a duration filter in production** — the event volume on a busy server can overwhelm the XEvent buffer and cause event loss.
