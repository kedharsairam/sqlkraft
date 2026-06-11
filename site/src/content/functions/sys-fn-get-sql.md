---
name: "sys.fn_get_sql"
title: "sys.fn_get_sql"
category: "system"
description: "Returns the text of the SQL statement for the specified SQL handle. Transact-SQL syntax conventions Database ID. For ad hoc and prepared SQL statements, the ID of the database where the statements were compiled."
tags: ["system", "function"]
pubDate: 2026-05-29
syntax: "sys.fn_get_sql ( SqlHandle )"
---

## Description

Returns the text of the SQL statement for the specified SQL handle. Transact-SQL syntax conventions Database ID. For ad hoc and prepared SQL statements, the ID of the database where the statements were compiled. ID of the database object. Is NULL for ad hoc SQL statements. Indicates the number of the group, if the procedures are grouped. This feature will be removed in a future version of Microsoft SQL Server. Avoid using this

## Syntax

```sql
sys.fn_get_sql ( SqlHandle )
```

## Arguments

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Returns the text of the SQL batch that is identified by the specified

. This table-

valued function replaces the system function

Is a token that uniquely identifies a batch that has executed or is currently executing.

can be obtained from the following dynamic management objects:

sys.dm_exec_query_stats

sys.dm_exec_requests

sys.dm_exec_cursors

sys.dm_exec_xml_handles

sys.dm_exec_query_memory_grants

sys.dm_exec_connections

plan_handle

Is a token that uniquely identifies a query execution plan for a batch that has executed and its

plan resides in the plan cache, or is currently executing.

plan_handle

plan_handle

can be obtained from the following dynamic management objects:

sys.dm_exec_cached_plans (Transact-SQL)

sys.dm_exec_query_stats (Transact-SQL)

sys.dm_exec_requests (Transact-SQL)

## Examples

### Example 1

```sql
DECLARE @Handle varbinary(64);
SELECT @Handle = sql_handle
FROM sys.dm_exec_requests
WHERE session_id = 52 and request_id = 0;
SELECT * FROM sys.fn_get_sql(@Handle);
GO
```
