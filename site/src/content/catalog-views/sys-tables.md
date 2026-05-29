---
name: 'sys.tables'
title: 'sys.tables'
category: 'objects'
description: '## A. Return all user tables without a primary key'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## A. Return all user tables without a primary key

## B. List temporal data related tables


## Description
: SQL Server 2022 (16.x) and later

versions, and Azure SQL Database

When


## returns
of

the ledger view, otherwise returns

.

: SQL Server 2022 (16.x) and later

versions, and Azure SQL Database

Indicates a ledger table that was dropped.

: SQL Server 2022 (16.x) and later

versions, and Azure SQL Database

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

The following example returns all of the user tables that don't have a primary key.

SQL

The following example shows how related temporal data can be exposed.

## C. List information about temporal history retention

: SQL Server 2016 (13.x) and later versions, and Azure SQL Database.

SQL

The following example shows how information on temporal history retention can be exposed.

: SQL Server 2017 (14.x) and later versions, and Azure SQL Database.

SQL

Object Catalog Views (Transact-SQL)

System catalog views (Transact-SQL)

DBCC CHECKDB (Transact-SQL)

DBCC CHECKTABLE (Transact-SQL)

Querying the SQL Server System Catalog FAQ

Related content

In-Memory OLTP overview and usage scenarios

Last updated on 11/18/2025

```sql
HISTORY_TABLE
UPDATABLE_LEDGER_TABLE
APPEND_ONLY_LEDGER_TABLE
```

```sql
ledger_view_id
```

```sql
ledger_type IN (2, 3)
```

```sql
object_id
```

```sql
NULL
```

```sql
is_dropped_ledger_table
```

```sql
SELECT
SCHEMA_NAME(schema_id)
AS
schema_name,
name
AS
table_name
FROM
sys.tables
WHERE
OBJECTPROPERTY(object_id,
'TableHasPrimaryKey'
) = 0
ORDER
BY
schema_name, table_name;
GO
```

```sql
SELECT
T1.object_id,
T1.name
AS
TemporalTableName,
SCHEMA_NAME(T1.schema_id)
AS
TemporalTableSchema,
T2.name
AS
HistoryTableName,
SCHEMA_NAME(T2.schema_id)
AS
HistoryTableSchema,
T1.temporal_type_desc
FROM
sys.tables T1
LEFT
JOIN
sys.tables T2
ON
T1.history_table_id = T2.object_id
ORDER
BY
T1.temporal_type
DESC
;
```

```sql
SELECT
DB.is_temporal_history_retention_enabled,
SCHEMA_NAME(T1.schema_id)
AS
TemporalTableSchema,
T1.name
AS
TemporalTableName,
SCHEMA_NAME(T2.schema_id)
AS
HistoryTableSchema,
T2.name
AS
HistoryTableName,
T1.history_retention_period,
T1.history_retention_period_unit_desc
FROM
sys.tables T1
OUTER
APPLY
(
SELECT
is_temporal_history_retention_enabled
FROM
sys.databases
WHERE
name
= DB_NAME()
) DB
LEFT
JOIN
sys.tables T2
ON
T1.history_table_id = T2.object_id
WHERE
T1.temporal_type = 2;
```
