---
name: 'sys.dm_exec_sessions'
title: 'sys.dm_exec_sessions'
category: 'execution'
description: 'On SQL Database, if the user is the database owner, the user will see all executing sessions on'
pubDate: 2026-05-29
---

On SQL Database, if the user is the database owner, the user will see all executing sessions on

the SQL Database; otherwise, the user will see only the current session.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.

This dynamic management function can be used in conjunction with sys.dm_exec_sessions or

sys.dm_exec_requests by doing

.

The following example demonstrates passing a session ID (SPID) and a request ID to the

function.

SQL

The following example lists the input buffer for user sessions.

）

Running this DMV outside of SQL Server Management Studio against SQL Server without

VIEW SERVER STATE permissions (such as in a trigger, stored procedure, or function)

throws a permission error on the master database.

）

Running this DMV outside of SQL Server Management Studio against Azure SQL Database

without owner permissions (such as in a trigger, stored procedure, or function) throws a

permission error on the master database.

SQL

Execution Related Dynamic Management Views and Functions (Transact-SQL)

sys.dm_exec_sessions (Transact-SQL)

sys.dm_exec_requests (Transact-SQL)

DBCC INPUTBUFFER (Transact-SQL)

Last updated on 11/18/2025

## varbinary(64)

## sys.syscacheobjects

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric


## Returns one row per plan attribute for the plan specified by the plan handle. You can use this
table-valued function to get details about a particular plan, such as the cache key values or the

number of current simultaneous executions of the plan.


## syntaxsql
plan_handle

Uniquely identifies a query plan for a batch that has executed and whose plan resides in the

plan cache.

plan_handle

is

. The plan handle can be obtained from the

sys.dm_exec_cached_plans

dynamic management view.

attribute

Name of the attribute associated with this plan. The table immediately

below this one lists the possible attributes, their data types, and their


## descriptions.
value

Value of the attribute that is associated with this plan.

７

Some of the information returned through this function maps to the

backward compatibility view.

ﾉ

is_cache_key

Indicates whether the attribute is used as part of the cache lookup key for

the plan.

From the above table,

can have the following values:

set_options

Indicates the option values that the plan was compiled with.

objectid

One of the main keys used for looking up an object in the

cache. This is the object ID stored in

sys.objects

for database

objects (procedures, views, triggers, and so on). For plans of

type "Adhoc" or "Prepared", it is an internal hash of the

batch text.

dbid

Is the ID of the database containing the entity the plan

refers to.

For ad hoc or prepared plans, it is the database ID from

which the batch is executed.

dbid_execute

For system objects stored in the

database, the

database ID from which the cached plan is executed. For all

other cases, it is 0.

user_id

Value of -2 indicates that the batch submitted does not

depend on implicit name resolution and can be shared

among different users. This is the preferred method. Any

other value represents the user ID of the user submitting the

query in the database.

language_id

ID of the language of the connection that created the cache

object. For more information, see

sys.syslanguages

(Transact-SQL)

.

date_format

Date format of the connection that created the cache object.

For more information, see

SET DATEFORMAT (Transact-SQL)

.

date_first

Date first value. For more information, see

SET DATEFIRST

(Transact-SQL)

.

compat_level

Represents the compatibility level set in the database in

whose context the query plan was compiled. The

compatibility level returned is the compatibility level of the

current database context for adhoc statements, and is

ﾉ

unaffected by the query hint

QUERY_OPTIMIZER_COMPATIBILITY_LEVEL_n

. For statements

contained in a stored procedure or function it corresponds

to the compatibility level of the database in which the

stored procedure or function is created.

status

Internal status bits that are part of the cache lookup key.

required_cursor_options

Cursor options specified by the user such as the cursor type.

acceptable_cursor_options

Cursor options that SQL Server may implicitly convert to in

order to support the execution of the statement. For

example, the user may specify a dynamic cursor, but the

query optimizer is permitted to convert this cursor type to a

static cursor.

merge_action_type

The type of trigger execution plan used as the result of a

MERGE statement.

0 indicates a non-trigger plan, a trigger plan that does not

execute as the result of a MERGE statement, or a trigger

plan that executes as the result of a MERGE statement that

only specifies a DELETE action.

1 indicates an INSERT trigger plan that runs as the result of a

MERGE statement.

2 indicates an UPDATE trigger plan that runs as the result of

a MERGE statement.

3 indicates a DELETE trigger plan that runs as the result of a

MERGE statement containing a corresponding INSERT or

UPDATE action.

For nested triggers run by cascading actions, this value is

the action of the MERGE statement that caused the cascade.

is_replication_specific

Represents that the session from which this plan was

compiled is one that connected to the instance of SQL

Server using an undocumented connection property which

allows the server to identify the session as one created by

replication components, so that the behavior of certain

functional aspects of the server are changed according to

what such replication component expects.

optional_spid

The connection session_id (spid) becomes part of the cache

key in order to reduce the number of re-compiles. This

prevents recompilations for a single session's re-use of a

plan involving non-dynamically bound temp tables.

optional_clr_trigger_dbid

Only populated in the case of a CLR DML trigger. The ID of

the database containing the entity.

For any other object type, returns zero.

optional_clr_trigger_objid

Only populated in the case of a CLR DML trigger. The object

ID stored in

sys.objects

.

For any other object type, returns zero.

parent_plan_handle

Always NULL.

is_azure_user_plan

1 for queries executed in an Azure SQL Database from a

session initiated by a user.

0 for queries that have been executed from a session not

initiated by an end user, but by applications running from

within Azure infrastructure that issue queries for other

purposes of collecting telemetry or executing administrative

tasks. Customers are not charged for resources consumed

by queries where is_azure_user_plan = 0.

only.

inuse_exec_context

Number of currently executing batches that are using the

query plan.

free_exec_context

Number of cached execution contexts for the query plan

that are not being currently used.

hits_exec_context

Number of times the execution context was obtained from

the plan cache and reused, saving the overhead of

recompiling the SQL statement. The value is an aggregate

for all batch executions so far.

misses_exec_context

Number of times that an execution context could not be

found in the plan cache, resulting in the creation of a new

execution context for the batch execution.

removed_exec_context

Number of execution contexts that have been removed

because of memory pressure on the cached plan.

inuse_cursors

Number of currently executing batches containing one or

more cursors that are using the cached plan.

free_cursors

Number of idle or free cursors for the cached plan.

## set_options

## set_options

## set_options

```sql
SELECT
*
FROM
sys.dm_exec_input_buffer (52, 0);
GO
```

```sql
SELECT
es.session_id, ib.event_info
FROM
sys.dm_exec_sessions
AS
es
CROSS
APPLY
sys.dm_exec_input_buffer(es.session_id,
NULL
)
AS
ib
WHERE
es.is_user_process = 1;
GO
```

```sql
sys.dm_exec_plan_attributes ( plan_handle )
```
