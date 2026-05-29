---
title: "Work with"
topic: "tables"
description: |
  Article

  •

  02/04/2025

  Applies to:

  SQL Server 2016 (13.x) and later

  Azure SQL Managed Instance

  This article discusses how working with a memory-optimized system-versioned temporal table

  is differ
tags:
  - "tables"
  - "work-with"
pubDate: 2025-12-01
---

Article

•

02/04/2025

Applies to:

SQL Server 2016 (13.x) and later

Azure SQL Managed Instance

This article discusses how working with a memory-optimized system-versioned temporal table

is different from working with a disk-based system-versioned temporal table.

To discover metadata about a memory-optimized system-versioned temporal table, you need

to combine information from

sys.tables

and

sys.internal_tables

. A system-versioned temporal

table is presented as parent_object_id of the internal in-memory history table

This example shows how to query and join these tables.

SQL

７

Note

Memory-optimized temporal tables are only available in SQL Server and Azure SQL

Managed Instance. Memory-optimized tables and temporal tables are independently

available in Azure SQL Database.

```sql
SELECT
SCHEMA_NAME(T1.schema_id)
AS
TemporalTableSchema,
OBJECT_NAME(IT.parent_object_id)
AS
TemporalTableName,
T1.object_id
AS
TemporalTableObjectId,
IT.Name
AS
InternalHistoryStagingName,
SCHEMA_NAME(T2.schema_id)
AS
HistoryTableSchema,
OBJECT_NAME(T1.history_table_id)
AS
HistoryTableName
FROM
sys.internal_tables IT
INNER
JOIN
sys.tables T1
ON
IT.parent_object_id = T1.object_id
INNER
JOIN
sys.tables T2
ON
T1.history_table_id = T2.object_id
WHERE
T1.is_memory_optimized = 1
AND
T1.temporal_type = 2;
```
