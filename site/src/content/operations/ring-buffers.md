---
title: "Ring buffers"
topic: "high-availability"
description: "Some diagnostic Always On availability group (AG) information can be obtained from the SQL Server ring buffers, or the dynamic management view (DMV)."
tags: ["high-availability","ring-buffers"]
pubDate: "2025-12-01"
---

Some diagnostic Always On availability group (AG) information can be obtained from the SQL

Server ring buffers, or the

dynamic management view (DMV). The ring

buffers are created during SQL Server startup, and record alerts within the SQL Server system

for internal diagnostics. They aren't supported, but you can still extract valuable information

from them when troubleshooting issues. These ring buffers provide another source of

diagnostics when SQL Server hangs or has crashed.

The following Transact-SQL (T-SQL) query retrieves all event records from the AG ring buffers.

To make the data more manageable, filter the data by date and the ring buffer type. The

following query retrieves records from the specified ring buffer that occurred today.

```cmd
sys.dm_os_ring_buffers
SELECT
*
FROM sys.dm_os_ring_buffers
WHERE ring_buffer_type
LIKE
'%HADR%'
DECLARE
@start_of_today DATETIME,
@start_of_tomorrow DATETIME;
SET
@start_of_today =
CAST (
FLOOR (
CAST (
GETDATE ()
AS
FLOAT
))
AS
DATETIME);
SET
@start_of_tomorrow =
DATEADD (
DAY
, 1, @start_of_today);
DECLARE
@runtime DATETIME;
SET
@runtime =
GETDATE ();
SELECT
CONVERT (
VARCHAR (30), @runtime, 121)
AS data_collection_runtime,
DATEADD (ms, - 1 * (inf.ms_ticks - ring.timestamp),
GETDATE ())
AS ring_buffer_record_time,
ring.timestamp
AS record_timestamp,
inf.ms_ticks
AS cur_timestamp,
ring.*
FROM sys.dm_os_ring_buffers ring
CROSS
JOIN sys.dm_os_sys_info inf
WHERE ring_buffer_type =
'<RING_BUFFER_TYPE>'
AND
DATEADD (ms, - 1 * (inf.ms_ticks - ring.timestamp),
GETDATE ()) >=
@start_of_today
```
