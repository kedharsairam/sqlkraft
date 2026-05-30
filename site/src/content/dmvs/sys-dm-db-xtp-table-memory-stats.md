---
name: "sys.dm_db_xtp_table_memory_stats"
title: "sys.dm_db_xtp_table_memory_stats"
category: "in-memory"
description: "Returns memory usage statistics for each In-Memory OLTP table (user and system) in the current database. The system tables have negative object IDs and are used to store run-time information for the In-Memory OLTP engine. Unlike user objects, system tables are internal and only exist in-memory, therefore, they are not visible through catalog views. System tables are used to store information such "
tags: ["in-memory", "dmv"]
pubDate: 2026-05-29
syntax: |
  -- finding memory for objects
  SELECT
  OBJECT_NAME(object_id), *
  FROM
  sys.dm_db_xtp_table_memory_stats;
  SELECT
  SUM
  ( memory_allocated_for_indexes_kb + memory_allocated_for_table_kb)
  AS
  memoryallocated_objects_in_kb
  FROM
  sys.dm_db_xtp_table_memory_stats;
---

## Description

Returns memory usage statistics for each In-Memory OLTP table (user and system) in the current database. The system tables have negative object IDs and are used to store run-time information for the In-Memory OLTP engine. Unlike user objects, system tables are internal and only exist in-memory, therefore, they are not visible through catalog views. System tables are used to store information such as metadata for all data/delta files in storage, merge requests,

## Syntax

```sql
-- finding memory for objects
SELECT
OBJECT_NAME(object_id), *
FROM sys.dm_db_xtp_table_memory_stats;
SELECT
SUM ( memory_allocated_for_indexes_kb + memory_allocated_for_table_kb)
AS memoryallocated_objects_in_kb
FROM sys.dm_db_xtp_table_memory_stats;
```

## Permissions

Article • 03/05/2024 SQL Server Azure SQL Database Azure SQL Managed Instance Returns memory usage statistics for each In-Memory OLTP table (user and system) in the current database. The system tables have negative object IDs and are used to store run-time information for the In-Memory OLTP engine. Unlike user objects, system tables are internal and only exist in-memory, therefore, they are not visible through catalog views. System tables are used to store information such as metadata for all data/delta files in storage, merge requests, watermarks for delta files to filter rows, dropped tables, and relevant information for recovery and backups. Given that the In-Memory OLTP engine can have up to 8,192 data and delta file pairs, for large in-memory databases, the memory taken by system tables can be a few megabytes. For more information, see In-Memory OLTP (In-Memory Optimization) . object_id The object ID of the table. for In-Memory OLTP system tables. memory_allocated_for_table_kb Memory allocated for this table. memory_used_by_table_kb Memory used by table, including row versions. memory_allocated_for_indexes_kb Memory allocated for indexes on this table. memory_used_by_indexes_kb Memory consumed for indexes on this table. All rows are returned if you have VIEW DATABASE STATE permission on the current database. Otherwise, an empty rowset is returned. If you do not have VIEW DATABASE permission, all columns will be returned for rows in tables that you have SELECT permission on. System tables are returned only for users with VIEW DATABASE STATE permission. ﾉ
