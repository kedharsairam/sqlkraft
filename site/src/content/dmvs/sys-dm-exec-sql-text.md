---
title: sys.dm_exec_sql_text
name: sys.dm_exec_sql_text
category: execution
description:
pubDate: 2026-05-29
---

In SQL Database, dynamic management views cannot expose information that would impact

database containment or expose information about other databases the user has access to. To

avoid exposing this information, every row that contains data that doesn't belong to the

connected tenant is filtered out.

Statistics in the view are updated when a query is completed.

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

either the

permission on the database, or membership in the

server role is required.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.

The following example returns information about the top five triggers identified by average

elapsed time.

SQL

Execution Related Dynamic Management Views and Functions (Transact-SQL)

sys.dm_exec_sql_text (Transact-SQL)

sys.dm_exec_query_stats (Transact-SQL)

sys.dm_exec_procedure_stats (Transact-SQL)

sys.dm_exec_cached_plans (Transact-SQL)

Last updated on 11/18/2025

## Applies to:

## sp_xml_preparedocument

Article

•

12/16/2024

SQL Server

Azure SQL Managed Instance

## Returns information about active handles that have been opened by

.

session_id

| 0,

ID of the session. If

session_id

is specified, this function returns information about XML handles

in the specified session.

If 0 is specified, the function returns information about all XML handles for all sessions.

Session ID of the session that holds this

XML document handle.

XML document handle ID returned by

.

Internal handle ID used for the associated

namespace document that has been passed

as the third parameter to

. NULL if there is

no namespace document.

Handle to the text of the SQL code where

the handle has been defined.

ﾉ

## sql_handles

## sp_xml_preparedocument

Number of characters into the currently

executing batch or stored procedure at

which the

call

occurs. Can be used together with the

, the

, and

the

dynamic

management function to retrieve the

currently executing statement for the

request.

Number of characters into the currently

executing batch or stored procedure at

which the

call

occurs. Can be used together with the

, the

, and

the

dynamic

management function to retrieve the

currently executing statement for the

request.

Timestamp when

was called.

Size of the unparsed XML document in

bytes.

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

t call.

The lifetime of

used to retrieve the SQL text that executed a call to

outlives the cached plan used to execute the query. If the query text

```sql
VIEW SERVER STATE
```

```sql
##MS_ServerStateReader##
```

```sql
VIEW DATABASE STATE
```

```sql
##MS_ServerStateReader##
```

```sql
SELECT
TOP 5 d.object_id, d.database_id, DB_NAME(database_id)
AS
'database_name'
,
OBJECT_NAME(object_id, database_id)
AS
'trigger_name'
, d.cached_time,
d.last_execution_time, d.total_elapsed_time,
d.total_elapsed_time/d.execution_count
AS
[avg_elapsed_time],
d.last_elapsed_time, d.execution_count
FROM
sys.dm_exec_trigger_stats
AS
d
ORDER
BY
[total_worker_time]
DESC
;
```

```sql
dm_exec_xml_handles (session_id | 0 )
```
