---
title: "Isolate the object causing latch contention"
topic: "io-fundamentals"
description: ""
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

Once we determined that latch contention was problematic, we then set out to determine what

was causing the latch contention.

The following script uses the resource_description column to isolate which index was causing

the

contention:

７

Note

The resource_description column returned by this script provides the resource description

in the format

, where the name of the database associated

with

can be determined by passing the value of

to the

function.

As shown here, the contention is on the table

and index name

. Note

names have been changed to anonymize the workload.

`PAGELATCH_EX`

```sql
<DatabaseID,FileID,PageID>
```

`DatabaseID`

`DatabaseID`

`DB_NAME()`

`LATCHTEST`

`CIX_LATCHTEST`

```sql
SELECT wt.session_id,
wt.wait_type,
wt.wait_duration_ms,
s.name
AS schema_name,
o.name
AS object_name,
i.name
AS index_name
FROM sys.dm_os_buffer_descriptors
AS bd
INNER
JOIN (
SELECT
*,
--resource_description
CHARINDEX (
':'
, resource_description)
AS file_index,
CHARINDEX (
':'
, resource_description,
CHARINDEX (
':'
,
resource_description) + 1)
AS page_index,
resource_description
AS rd
FROM sys.dm_os_waiting_tasks
AS wt
WHERE wait_type
LIKE
'PAGELATCH%'
)
AS wt
ON bd.database_id =
SUBSTRING (wt.rd, 0, wt.file_index)
AND bd.file_id =
SUBSTRING (wt.rd, wt.file_index + 1, 1)
--wt.page_index)
AND bd.page_id =
SUBSTRING (wt.rd, wt.page_index + 1,
LEN (wt.rd))
INNER
JOIN sys.allocation_units
AS au
ON bd.allocation_unit_id = au.allocation_unit_id
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
ON o.schema_id = s.schema_id
ORDER
BY wt.wait_duration_ms
DESC
;
```
