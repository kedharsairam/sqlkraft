---
title: "contention"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals","architecture"]
pubDate: 2026-05-29
---

The following script queries buffer descriptors to determine which objects are associated with

the longest latch wait times.

```sql
'SQLTRACE_INCREMENTAL_FLUSH_SLEEP'
)
ORDER
BY (e.wait_time_ms - s.wait_time_ms)
DESC
;
--clean up table
DELETE
FROM
#_wait_stats
WHERE snap_time = @previous_snap_time;
```

```sql
IF EXISTS (
SELECT
*
FROM tempdb.sys.objects
WHERE
[
name
]
LIKE
'#WaitResources%'
)
DROP
TABLE
#WaitResources;
CREATE
TABLE
#WaitResources (
session_id
INT
,
wait_type
NVARCHAR (1000),
wait_duration_ms
INT
,
resource_description sysname
NULL
,
db_name
NVARCHAR (1000),
schema_name
NVARCHAR (1000),
object_name
NVARCHAR (1000),
index_name
NVARCHAR (1000)
);
GO
DECLARE
@WaitDelay
AS
VARCHAR (16), @Counter
AS
INT
, @MaxCount
AS
INT
, @Counter2
AS
INT
;
SELECT
@Counter = 0, @MaxCount = 600, @WaitDelay =
'00:00:00.100'
;
-- 600x.1=60 seconds
SET
NOCOUNT
ON
;
WHILE @Counter < @MaxCount
BEGIN
INSERT
INTO
#WaitResources (session_id, wait_type, wait_duration_ms,
resource_description)
--, db_name, schema_name, object_name, index_name)
SELECT wt.session_id,
wt.wait_type,
wt.wait_duration_ms,
wt.resource_description
FROM sys.dm_os_waiting_tasks
AS wt
WHERE wt.wait_type
LIKE
'PAGELATCH%'
AND wt.session_id <> @@SPID;
```

```sql
-- SELECT * FROM sys.dm_os_buffer_descriptors;
SET
@Counter = @Counter + 1;
WAITFOR DELAY @WaitDelay;
END
--SELECT * FROM #WaitResources;
UPDATE
#WaitResources
SET db_name = DB_NAME(bd.database_id),
schema_name = s.name,
object_name = o.name,
index_name = i.name
FROM
#WaitResources
AS wt
INNER
JOIN sys.dm_os_buffer_descriptors
AS bd
ON bd.database_id =
SUBSTRING (wt.resource_description, 0,
CHARINDEX (
':'
,
wt.resource_description))
AND bd.file_id =
SUBSTRING (wt.resource_description,
CHARINDEX (
':'
,
wt.resource_description) + 1,
CHARINDEX (
':'
, wt.resource_description,
CHARINDEX (
':'
, wt.resource_description) + 1) -
CHARINDEX (
':'
,
wt.resource_description) - 1)
AND bd.page_id =
SUBSTRING (wt.resource_description,
CHARINDEX (
':'
,
wt.resource_description,
CHARINDEX (
':'
, wt.resource_description) + 1) + 1,
LEN (wt.resource_description) + 1)
-- AND wt.file_index > 0 AND wt.page_index > 0
INNER
JOIN sys.allocation_units
AS au
ON bd.allocation_unit_id = AU.allocation_unit_id
INNER
JOIN sys.partitions
AS p
ON au.container_id = p.partition_id
INNER
JOIN sys.indexes
AS i
ON p.index_id = i.index_id
AND p.object_id = i.object_id
INNER
JOIN sys.objects
AS o
ON i.object_id = o.object_id
INNER
JOIN sys.schemas
AS s
ON o.schema_id = s.schema_id;
SELECT
*
FROM
#WaitResources
ORDER
BY wait_duration_ms
DESC
;
GO
/*
--Other views of the same information
SELECT wait_type, db_name, schema_name, object_name, index_name,
SUM(wait_duration_ms) [total_wait_duration_ms] FROM #WaitResources
GROUP BY wait_type, db_name, schema_name, object_name, index_name;
SELECT session_id, wait_type, db_name, schema_name, object_name, index_name,
SUM(wait_duration_ms) [total_wait_duration_ms] FROM #WaitResources
GROUP BY session_id, wait_type, db_name, schema_name, object_name, index_name;
*/
--SELECT * FROM #WaitResources
--DROP TABLE #WaitResources;
```
