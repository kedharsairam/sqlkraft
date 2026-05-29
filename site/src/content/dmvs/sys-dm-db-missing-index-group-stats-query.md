---
title: sys.dm_db_missing_index_group_stats_query
name: sys.dm_db_missing_index_group_stats_query
category: execution
description:
pubDate: 2026-05-29
---

One missing index group may have several queries that needed the same index. For more

information about individual queries that needed a specific index in this DMV, see

sys.dm_db_missing_index_group_stats_query

.

To query this dynamic management view, users must be granted the VIEW SERVER STATE

permission or any permission that implies the VIEW SERVER STATE permission.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.

The following examples illustrate how to use the

dynamic management view. Learn more about guidance for using missing indexes in

tune

nonclustered indexes with missing index suggestions

.

The following query determines which 10 missing indexes would produce the highest

anticipated cumulative improvement, in descending order, for user queries.

SQL

The following query determines which missing indexes comprise a particular missing index

group, and displays their column details. For the sake of this example, the missing index

is 24.

SQL

This query provides the name of the database, schema, and table where an index is missing. It

also provides the names of the columns that should be used for the index key. When writing

the CREATE INDEX DDL statement to implement missing indexes, list equality columns first and

then inequality columns in the ON <

table_name

> clause of the CREATE INDEX statement.

Included columns should be listed in the INCLUDE clause of the CREATE INDEX statement. To

determine an effective order for the equality columns, order them based on their selectivity,

listing the most selective columns first (leftmost in the column list). Learn how to

apply missing

index suggestions

.

Learn more about the missing index feature in the following articles:

Tune nonclustered indexes with missing index suggestions

sys.dm_db_missing_index_columns (Transact-SQL)

sys.dm_db_missing_index_details (Transact-SQL)

sys.dm_db_missing_index_groups (Transact-SQL)

sys.dm_db_missing_index_group_stats_query (Transact-SQL)

CREATE INDEX (Transact-SQL)

sys.dm_os_sys_info (Transact-SQL)

Last updated on 11/18/2025

## Applies to:

SQL Server 2019 (15.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

## Returns information about queries that needed a missing index from groups of missing

indexes, excluding spatial indexes. More than one query might be returned per missing index

group. One missing index group might have several queries that needed the same index.

In Azure SQL Database, dynamic management views can't expose information that would affect

database containment, or expose information about other databases the user has access to. To

avoid exposing this information, every row that contains data that doesn't belong to the

connected tenant is filtered out.

Identifies a group of missing indexes. This identifier is

unique across the server.

The other columns provide information about all queries

for which the index in the group is considered missing.

An index group contains only one index.

Can be joined to

in

sys.dm_db_missing_index_groups

.

Binary hash value calculated on the query and used to

identify queries with similar logic. You can use the query

hash to determine the aggregate resource usage for

queries that differ only by literal values.

Binary hash value calculated on the query execution plan

and used to identify similar query execution plans. You

can use query plan hash to find the cumulative cost of

queries with similar execution plans.

Always

when a natively compiled stored procedure

queries a memory-optimized table.

A token that uniquely identifies the batch or stored

procedure of the last compiled statement that needed

this index.

ﾉ

The

can be used to retrieve the SQL text

of the query by calling the dynamic management

function

sys.dm_exec_sql_text

.

Indicates, in bytes, beginning with 0, the starting position

of the query that the row describes within the text of its

batch or persisted object for the last compiled statement

that needed this index in its SQL batch.

Indicates, in bytes, beginning with

, the ending position

of the query that the row describes within the text of its

batch or persisted object, for the last compiled statement

that needed this index in its SQL batch.

A token that uniquely identifies the batch or stored

procedure of the last compiled statement that needed

this index. Used by Query Store. Unlike

,

references the

used by the Query Store catalog

view

sys.query_store_query_text

.

## Returns

if Query Store wasn't enabled when the query

was compiled.

Number of seeks caused by user queries that the

recommended index in the group could have been used

for.

Number of scans caused by user queries that the

recommended index in the group could have been used

for.

Date and time of last seek caused by user queries that

the recommended index in the group could have been

used for.

Date and time of last scan caused by user queries that

the recommended index in the group could have been

used for.

Average cost of the user queries that could be reduced

by the index in the group.

Average percentage benefit that user queries could

experience if this missing index group was implemented.

The value means that the query cost would on average

drop by this percentage if this missing index group was

implemented.

Number of seeks caused by system queries, such as auto

stats queries, that the recommended index in the group

could have been used for. For more information, see

Auto Stats Event Class

.

Number of scans caused by system queries that the

recommended index in the group could have been used

for.

Date and time of last system seek caused by system

queries that the recommended index in the group could

have been used for.

Date and time of last system scan caused by system

queries that the recommended index in the group could

have been used for.

Average cost of the system queries that could be reduced

by the index in the group.

Average percentage benefit that system queries could

experience if this missing index group was implemented.

The value means that the query cost would on average

drop by this percentage if this missing index group was

implemented.

Information returned by

is updated by every

query execution, not by every query compilation or recompilation. Usage statistics aren't

persisted and are kept only until the database engine is restarted.

Database administrators should periodically make backup copies of the missing index

information if they want to keep the usage statistics after server recycling. Use the

column in

sys.dm_os_sys_info

to find the last database engine startup

time. You can also

persist missing indexes with Query Store

.

To query this dynamic management view, users must be granted the

permission or any permission that implies the

permission, for SQL Server

2019 (15.x) and previous versions.

```sql
sys.dm_db_missing_index_group_stats
```

```sql
group_handle
```

```sql
SELECT
TOP 10 *
FROM
sys.dm_db_missing_index_group_stats
ORDER
BY
avg_total_user_cost * avg_user_impact * (user_seeks + user_scans)
DESC
;
```

```sql
SELECT
migs.group_handle, mid.*
FROM
sys.dm_db_missing_index_group_stats
AS
migs
INNER
JOIN
sys.dm_db_missing_index_groups
AS
mig
ON
(migs.group_handle = mig.index_group_handle)
INNER
JOIN
sys.dm_db_missing_index_details
AS
mid
ON
(mig.index_handle = mid.index_handle)
WHERE
migs.group_handle = 24;
```

```sql
group_handle
```

```sql
index_group_handle
```

```sql
query_hash
```

```sql
query_plan_hash
```

```sql
0x000
```

```sql
last_sql_handle
```

```sql
last_sql_handle
```

```sql
last_statement_start_offset
```

```sql
last_statement_end_offset
```

```sql
0
```

```sql
last_statement_sql_handle
```

```sql
last_sql_handle
```

```sql
sys.query_store_query_text
```

```sql
statement_sql_handle
```

```sql
0
```

```sql
user_seeks
```

```sql
user_scans
```

```sql
last_user_seek
```

```sql
last_user_scan
```

```sql
avg_total_user_cost
```

```sql
avg_user_impact
```

```sql
system_seeks
```

```sql
system_scans
```

```sql
last_system_seek
```

```sql
last_system_scan
```

```sql
avg_total_system_cost
```

```sql
avg_system_impact
```

```sql
sys.dm_db_missing_index_group_stats_query
```

```sql
sqlserver_start_time
```

```sql
VIEW SERVER STATE
```

```sql
VIEW SERVER STATE
```
