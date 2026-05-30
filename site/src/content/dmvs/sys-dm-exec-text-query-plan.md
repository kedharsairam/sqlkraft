---
name: "sys.dm_exec_text_query_plan"
title: "sys.dm_exec_text_query_plan"
category: "execution"
description: "Indicates whether the corresponding stored procedure is encrypted. 0 = not encrypted Column is not nullable. Contains the compile-time Showplan representation of the query execution plan that is specified with . The Showplan is in text format. One plan is generated for each batch that contains, for example ad hoc Transact-SQL statements, stored procedure calls, and user-defined function calls. Col"
tags: ["execution", "dmv"]
pubDate: 2026-05-29
syntax: |
  sys.dm_exec_text_query_plan
  (
  plan_handle
  , { statement_start_offset | 0 | DEFAULT }
  , { statement_end_offset | -1 | DEFAULT }
  )
---

## Description

Indicates whether the corresponding stored procedure is encrypted. 0 = not encrypted Column is not nullable. Contains the compile-time Showplan representation of the query execution plan that is specified with . The Showplan is in text format. One plan is generated for each batch that contains, for example ad hoc Transact-SQL statements, stored procedure calls, and user-defined function calls. Column is nullable. Under the following conditions, no Showplan output is returned in the returned table for If the query plan that is specified by using has been evicted from the plan column of the returned table is null. For example, this condition may occur if there is a time delay between when the plan handle was captured and when it was used with Some Transact-SQL statements are not cached, such as bulk operation statements or

## Syntax

```sql
sys.dm_exec_text_query_plan (
plan_handle
, { statement_start_offset | 0 | DEFAULT }
, { statement_end_offset | -1 | DEFAULT }
)
```

## Arguments

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Returns the Showplan in text format for a Transact-SQL batch or for a specific statement within

the batch. The query plan specified by the plan handle can either be cached or currently

executing. This table-valued function is similar to

sys.dm_exec_query_plan (Transact-SQL)

has the following differences:

The output of the query plan is returned in text format.

The output of the query plan is not limited in size.

Individual statements within the batch can be specified.

: SQL Server (SQL Server 2008 (10.0.x) and later), Azure SQL Database.

Transact-SQL syntax conventions

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

Indicates whether the corresponding stored procedure is encrypted.

0 = not encrypted

1 = encrypted

Column is not nullable.

Contains the compile-time Showplan representation of the query

execution plan that is specified with

plan_handle

. The Showplan is in text

format. One plan is generated for each batch that contains, for example

ad hoc Transact-SQL statements, stored procedure calls, and user-defined

function calls.

Column is nullable.

Under the following conditions, no Showplan output is returned in the

column of the

returned table for

If the query plan that is specified by using

plan_handle

has been evicted from the plan

column of the returned table is null. For example, this condition

may occur if there is a time delay between when the plan handle was captured and when

it was used with

Some Transact-SQL statements are not cached, such as bulk operation statements or

statements containing string literals larger than 8 KB in size. Showplans for such

statements cannot be retrieved by using

because they do

not exist in the cache.

If a Transact-SQL batch or stored procedure contains a call to a user-defined function or a

call to dynamic SQL, for example using EXEC (

), the compiled XML Showplan for the

user-defined function is not included in the table returned by

for the batch or stored procedure. Instead, you must make

a separate call to

plan_handle

that corresponds to

the user-defined function.

When an ad hoc query uses

forced parameterization

column will

contain only the statement text and not the actual query plan. To return the query plan, call

for the plan handle of the prepared parameterized query. You

can determine whether the query was parameterized by referencing the

column of the
