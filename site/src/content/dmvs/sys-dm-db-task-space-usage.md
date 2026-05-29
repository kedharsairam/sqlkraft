---
title: sys.dm_db_task_space_usage
name: sys.dm_db_task_space_usage
category: execution
description:
pubDate: 2026-05-29
---

The following query returns the total number of free pages and total free space in megabytes

(MB) available in all data files in

.

SQL

The following query returns the total number of pages used by user objects and the total space

used by user objects in

.

SQL

Dynamic Management Views and Functions (Transact-SQL)

Database Related Dynamic Management Views (Transact-SQL)

sys.dm_db_task_space_usage (Transact-SQL)

sys.dm_db_session_space_usage (Transact-SQL)

Last updated on 11/18/2025

## Applies to:

## Basic

## S0

## S1

## elastic pools

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

## Returns a row for each full-text or semantic index in each table that has an associated full-text

or semantic index.

int

Object ID of the table that contains the index.

Logical size of the extraction in number of index pages.

Logical size of the extraction in number of index pages.

Logical size of the extraction in number of index pages.

For more information, see

Manage and Monitor Semantic Search

.

For information about the status of semantic indexing, query the following dynamic

management views:

sys.dm_fts_index_population (Transact-SQL)

sys.dm_fts_semantic_similarity_population (Transact-SQL)

On SQL Server and SQL Managed Instance, requires

permission.

On SQL Database

,

, and

service objectives, and for databases in

, the

server admin

account, the

Microsoft Entra admin

account, or membership in the

server role

is required. On all other SQL Database service objectives,

ﾉ

```sql
tempdb
```

```sql
tempdb
```

```sql
USE
tempdb;
GO
SELECT
SUM
(unallocated_extent_page_count)
AS
[free pages],
(
SUM
(unallocated_extent_page_count) * 1.0 / 128)
AS
[free
space
in
MB]
FROM
sys.dm_db_file_space_usage;
```

```sql
USE
tempdb;
GO
SELECT
SUM
(user_object_reserved_page_count)
AS
[
user
object
pages used],
(
SUM
(user_object_reserved_page_count) * 1.0 / 128)
AS
[
user
object
space
in
MB]
FROM
sys.dm_db_file_space_usage;
```

```sql
VIEW SERVER STATE
```

```sql
##MS_ServerStateReader##
```
