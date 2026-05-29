---
name: 'sys.sp_query_store_reset_exec_stats'
title: 'sp_query_store_reset_exec_stats'
category: 'general'
description: 'SQL Server 2016 (13.x) and later versions Azure SQL Database SQL Managed Instance SQL database in Microsoft Fabric Clears the runtime stats for a specific query plan from the Query Store. Transact-SQL syntax conventions The ID of the query plan to be cleared. , with no default. Requires the ALTER permission on the database. Arguments for extended stored procedures must be entered in the specific o'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_query_store_reset_exec_stats [ @plan_id = ] plan_id
  [ ; ]
---

## Description

SQL Server 2016 (13.x) and later versions Azure SQL Database SQL Managed Instance SQL database in Microsoft Fabric Clears the runtime stats for a specific query plan from the Query Store. Transact-SQL syntax conventions The ID of the query plan to be cleared. , with no default. Requires the ALTER permission on the database. Arguments for extended stored procedures must be entered in the specific order as described in the section. If the parameters are entered out of order, an error message occurs.

## Syntax

```sql
sp_query_store_reset_exec_stats [ @plan_id = ] plan_id
[ ; ]
```

## Remarks

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

SQL Managed Instance

SQL database in Microsoft Fabric

Clears the runtime stats for a specific query plan from the Query Store.

Transact-SQL syntax conventions

The ID of the query plan to be cleared.

, with no default.

(success) or

Requires the ALTER permission on the database.

Arguments for extended stored procedures must be entered in the specific order as

described in the

section. If the parameters are entered out of order, an error

message occurs.

## Examples

### Example 1

```sql
sp_query_store_reset_exec_stats
```

### Example 2

```sql
SELECT
txt.query_text_id,
txt.query_sql_text,
pl.plan_id,
qry.*
FROM
sys.query_store_plan
AS
pl
INNER
JOIN
sys.query_store_query
AS
qry
ON
pl.query_id = qry.query_id
INNER
JOIN
sys.query_store_query_text
AS
txt
ON
qry.query_text_id = txt.query_text_id;
EXECUTE
sp_query_store_reset_exec_stats 3;
```
