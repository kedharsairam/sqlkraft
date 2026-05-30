---
name: "system_health"
title: "The Default System Health Session (system_health)"
category: "system-health"
description: "Comprehensive reference on SQL Server's built-in system_health Extended Events session — how to query, interpret, and export session data for root-cause analysis of critical server events."
tags: ["extended-events", "system-health", "diagnostics", "ring-buffer", "default-session"]
targetVersion: "SQL Server 2012+"
pubDate: 2026-05-30
---

## Overview

The **system_health** session is SQL Server's built-in Extended Events session that runs automatically at instance startup. It collects a lightweight, always-on diagnostic trace of critical server events with minimal overhead — approximately 1–2% CPU overhead under normal conditions.

Unlike custom XEvent sessions, system_health requires no configuration, no startup scripts, and consumes a fixed 5 MB ring buffer target per event type. It is the first place every DBA should look when investigating unexplained failures, crashes, or performance anomalies.

## Events Captured

The system_health session monitors the following event categories:

| Event Category | Key Events Captured | Diagnostic Value |
|---|---|---|
| **Errors** | `error_reported`, `attention` | Critical system errors, query timeouts, killed sessions |
| **Memory Pressure** | `memory_broker_ring_buffer_recorded` | Low-memory notifications, resource rebalancing |
| **Deadlocks** | `xml_deadlock_report` | Full deadlock graphs including involved resources and processes |
| **Scheduling** | `scheduler_monitor_system_health_ring_buffer_recorded` | Non-yielding scheduler detections, SOS scheduling issues |
| **Connectivity** | `connectivity_ring_buffer_recorded` | Login failures, connection closure reasons |
| **Security** | `audit_login`, `audit_logout` | Login and logout events with security context |

## Querying the system_health Session

### Target Type: ring_buffer

The system_health session writes to an in-memory **ring_buffer** target. Each event type has its own ring buffer slot. Use the following T-SQL to extract and parse the XML data:

```sql
-- Read the system_health ring buffer and parse into a relational rowset
SELECT x.event_data.value('(event/@name)[1]', 'varchar(50)') AS event_name,
    x.event_data.value('(event/@package)[1]', 'varchar(50)') AS event_package,
    x.event_data.value('(event/@timestamp)[1]', 'datetime2') AS event_timestamp,
    x.event_data.value('(event/data[@name="category"]/text)[1]', 'int') AS error_category,
    x.event_data.value('(event/data[@name="error_number"]/value)[1]', 'int') AS error_number,
    x.event_data.value('(event/data[@name="severity"]/value)[1]', 'int') AS error_severity,
    x.event_data.value('(event/data[@name="message"]/value)[1]', 'nvarchar(4000)') AS error_message,
    CAST(x.event_data.query('.').value('.', 'nvarchar(max)') AS XML) AS raw_event_xml
FROM (
    SELECT CAST(st.target_data AS XML) AS session_target_data
    FROM sys.dm_xe_session_targets AS st
    INNER JOIN sys.dm_xe_sessions AS s
        ON s.[address] = st.event_session_address
    WHERE s.name = 'system_health'
        AND st.target_name = 'ring_buffer'
) AS sh
CROSS APPLY sh.session_target_data.nodes('/RingBufferTarget/event') AS x(event_data)
ORDER BY x.event_data.value('(event/@timestamp)[1]', 'datetime2') DESC;
```

### Detecting Recent Critical Errors

```sql
-- Retrieve the most recent critical errors (severity ≥ 17) from system_health
SELECT TOP 50 x.event_data.value('(event/@timestamp)[1]', 'datetime2') AS event_time,
    x.event_data.value('(event/data[@name="error_number"]/value)[1]', 'int') AS error_number,
    x.event_data.value('(event/data[@name="severity"]/value)[1]', 'int') AS severity,
    x.event_data.value('(event/data[@name="message"]/value)[1]', 'nvarchar(4000)') AS error_message
FROM (
    SELECT CAST(target_data AS XML) AS session_target_data
    FROM sys.dm_xe_session_targets
    WHERE event_session_address = (
        SELECT [address] FROM sys.dm_xe_sessions WHERE name = 'system_health'
    )
    AND target_name = 'ring_buffer'
) AS sh
CROSS APPLY sh.session_target_data.nodes('/RingBufferTarget/event[@name="error_reported"]') AS x(event_data)
WHERE x.event_data.value('(event/data[@name="severity"]/value)[1]', 'int') >= 17
ORDER BY event_time DESC;
```

### Extracting Scheduler Monitor (Non-Yielding) Events

```sql
-- Find scheduler monitor detections — indicates non-yielding Scheduler or long-running tasks
SELECT x.event_data.value('(event/@timestamp)[1]', 'datetime2') AS event_time,
    x.event_data.value('(event/data[@name="scheduler_address"]/value)[1]', 'varchar(50)') AS scheduler_address,
    x.event_data.value('(event/data[@name="non_yielding_waits"]/value)[1]', 'int') AS non_yielding_waits,
    x.event_data.value('(event/data[@name="non_yielding_yields"]/value)[1]', 'int') AS non_yielding_yields
FROM (
    SELECT CAST(target_data AS XML) AS target_data
    FROM sys.dm_xe_session_targets
    WHERE event_session_address = (
        SELECT [address] FROM sys.dm_xe_sessions WHERE name = 'system_health'
    )
    AND target_name = 'ring_buffer'
) AS sh
CROSS APPLY sh.target_data.nodes('/RingBufferTarget/event[@name="scheduler_monitor_system_health_ring_buffer_recorded"]') AS x(event_data)
ORDER BY event_time DESC;
```

## Checking system_health Session Status

```sql
-- Verify the system_health session is running and review its configuration
SELECT s.name,
    s.[status],
    s.total_regular_buffers,
    s.regular_buffer_size,
    s.total_large_buffer_size,
    s.event_retention_mode_desc,
    st.target_name,
    st.execution_count,
    st.execution_duration_ms
FROM sys.dm_xe_sessions AS s
LEFT JOIN sys.dm_xe_session_targets AS st
    ON s.[address] = st.event_session_address
WHERE s.name = 'system_health';
```

## Exporting to a File Target for Persistence

The ring buffer is ephemeral — events are lost on instance restart. For long-term capture, create a custom session that mirrors system_health events to a file target:

```sql
-- Create a persistent copy of system_health events to a file target
CREATE EVENT SESSION [persistent_system_health]
ON SERVER
ADD EVENT sqlserver.error_reported,
ADD EVENT sqlserver.xml_deadlock_report,
ADD EVENT sqlserver.scheduler_monitor_system_health_ring_buffer_recorded,
ADD EVENT sqlserver.memory_broker_ring_buffer_recorded,
ADD EVENT sqlserver.connectivity_ring_buffer_recorded
ADD TARGET package0.event_file (
    SET filename = N'C:\XELog\persistent_system_health.xel',
        max_file_size = 100,
        max_rollover_files = 10
)
WITH (
    MAX_MEMORY = 4096 KB,
    EVENT_RETENTION_MODE = ALLOW_SINGLE_EVENT_LOSS,
    MAX_DISPATCH_LATENCY = 30 SECONDS,
    MAX_EVENT_SIZE = 0 KB,
    MEMORY_PARTITION_MODE = NONE,
    TRACK_CAUSALITY = OFF,
    STARTUP_STATE = ON
);
ALTER EVENT SESSION [persistent_system_health] ON SERVER STATE = START;
```

## Event Data Retention Behavior

| Aspect | Detail |
|---|---|
| **Buffer size** | 5 MB per ring buffer slot (fixed) |
| **Retention** | Circular — oldest events overwritten when buffer is full |
| **Persistence** | None — lost on service restart |
| **Overhead** | < 2% CPU, < 10 MB memory |
| **Availability** | Always on since SQL Server 2012 |

## Best Practices

1. **Always check system_health first** for unexplained errors, crashes, or performance degradation — it is a zero-configuration diagnostic goldmine.
2. **Do not disable the system_health session** — it is designed for negligible overhead and provides critical diagnostic data when things go wrong.
3. **For long-term retention**, create a parallel persistent session that writes to a file target instead of relying on the ring buffer.
4. **Monitor buffer usage** using `sys.dm_xe_session_targets` to detect if events are being dropped due to ring buffer saturation.
5. **Use the raw XML** (`raw_event_xml`) to capture full event context — many events contain nested XML that single-value `value()` queries miss.
