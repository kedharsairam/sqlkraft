---
name: 'sys.dm_exec_sql_text'
title: 'sys.dm_exec_sql_text'
category: 'execution'
description: 'Number of characters into the currently executing batch or stored procedure at occurs. Can be used together with the management function to retrieve the currently executing statement for the Number of characters into the currently executing batch or stored procedure at occurs. Can be used together with the management function to retrieve the currently executing statement for the Size of the unpars'
tags: ["execution", "dmv"]
pubDate: 2026-05-29
syntax: 'sys.dm_exec_sql_text(sql_handle | plan_handle)'
---

## Description

Number of characters into the currently executing batch or stored procedure at occurs. Can be used together with the management function to retrieve the currently executing statement for the Number of characters into the currently executing batch or stored procedure at occurs. Can be used together with the management function to retrieve the currently executing statement for the Size of the unparsed XML document in Size of the unparsed XML namespace document, in bytes. NULL if there is no namespace document. Number of OPENXML calls with this document handle. Number of rows returned by all previous OPENXML calls for this document handle. Milliseconds since the last OPENXML call. If OPENXML has not been called, returns milliseconds since the The lifetime of used to retrieve the SQL text that executed a call to BACKUP DATABASE Execution Related Dynamic Management Views and Functions (Transact-SQL)

## Syntax

```sql
sys.dm_exec_sql_text(sql_handle | plan_handle)
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


## Remarks

Number of characters into the currently

executing batch or stored procedure at

occurs. Can be used together with the

management function to retrieve the

currently executing statement for the

Number of characters into the currently

executing batch or stored procedure at

occurs. Can be used together with the

management function to retrieve the

currently executing statement for the

Timestamp when

was called.

Size of the unparsed XML document in

Size of the unparsed XML namespace

document, in bytes. NULL if there is no

namespace document.

Number of OPENXML calls with this

document handle.

Number of rows returned by all previous

OPENXML calls for this document handle.

Milliseconds since the last OPENXML call. If

OPENXML has not been called, returns

milliseconds since the

The lifetime of

used to retrieve the SQL text that executed a call to

outlives the cached plan used to execute the query. If the query text

Description

BACKUP DATABASE

The text of the request can be retrieved by using

with the corresponding

for the request. Internal system processes

set the command based on the type of task they

perform. Tasks can include the following values:

LOCK MONITOR

CHECKPOINTLAZY

Not nullable.

A token that uniquely identifies the batch or stored

procedure that the query is part of. Nullable.

Indicates, in bytes, beginning with 0, the starting

position of the currently executing statement for the

currently executing batch or persisted object. Can be

used together with the

dynamic management function to retrieve the

currently executing statement for the request.

Indicates, in bytes, starting with 0, the ending position

of the currently executing statement for the currently

executing batch or persisted object. Can be used

together with the

dynamic management function

to retrieve the currently executing statement for the

request. Nullable.

A token that uniquely identifies a query execution plan

for a batch that is currently executing. Nullable.

ID of the database the request is executing against.

Not nullable.

In Azure SQL Database, the values are unique within a

single database or an elastic pool, but not within a

logical server.

Execution Related Dynamic Management Views and Functions (Transact-SQL)

sys.dm_exec_sql_text (Transact-SQL)

sys.dm_exec_query_plan (Transact-SQL)

sys.dm_exec_procedure_stats (Transact-SQL)

sys.dm_exec_trigger_stats (Transact-SQL)

sys.dm_exec_cached_plans (Transact-SQL)

Last updated on 11/18/2025

Related content

## Examples

### Example 1

```sql
59
```

### Example 2

```sql
-- Identify current spid (session_id)
SELECT
@@SPID;
GO
-- Create activity
WAITFOR DELAY '00:02:00';
SELECT
t.*
FROM
sys.dm_exec_requests
AS
r
CROSS
APPLY
sys.dm_exec_sql_text(r.sql_handle)
AS
t
WHERE
session_id = 59
-- modify this value with your actual spid
```
