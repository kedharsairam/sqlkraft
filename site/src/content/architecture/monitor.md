---
title: "Monitor"
topic: "tables"
description: |
  Article

  •

  02/04/2025

  Applies to:

  SQL Server 2016 (13.x) and later

  Azure SQL Managed Instance

  You can use existing views to track detailed and summarized memory consumption for every

  system-vers
tags:
  - "tables"
  - "monitor"
pubDate: 2025-12-01
---

Article

•

02/04/2025

2016 (13.x) and later

Azure SQL Managed Instance

You can use existing views to track detailed and summarized memory consumption for every

system-versioned memory-optimized table.

Use the following example code to monitor temporal tables that use In-Memory OLTP. These

examples make use of common table expressions (CTEs).

The following query details the memory consumption, split per main system-versioned and

internal history staging table.

```sql
WITH
InMemoryTemporalTables
AS (
SELECT
SCHEMA_NAME(T1.schema_id)
AS
TemporalTableSchema,
T1.object_id
AS
TemporalTableObjectId,
IT.object_id
AS
InternalTableObjectId,
OBJECT_NAME(IT.parent_object_id)
AS
TemporalTableName,
IT.Name
AS
InternalHistoryStagingName
FROM sys.internal_tables IT
INNER
JOIN sys.tables T1
ON
IT.parent_object_id = T1.object_id
WHERE
T1.is_memory_optimized = 1
AND
T1.temporal_type = 2
)
SELECT
TemporalTableSchema,
T.TemporalTableName,
T.InternalHistoryStagingName,
CASE
WHEN
C.object_id = T.TemporalTableObjectId
THEN
'Temporal Table Consumption'
ELSE
'Internal Table Consumption'
END
ConsumedBy,
C.*
FROM sys.dm_db_xtp_memory_consumers C
INNER
JOIN
InMemoryTemporalTables T
ON
C.object_id = T.TemporalTableObjectId
OR
C.object_id = T.InternalTableObjectId
```
