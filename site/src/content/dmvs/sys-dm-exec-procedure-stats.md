---
name: 'sys.dm_exec_procedure_stats'
title: 'sys.dm_exec_procedure_stats'
category: 'execution'
description: 'sys.dm_exec_procedure_stats (Transact-SQL)'
pubDate: 2026-05-29
---

sys.dm_exec_procedure_stats (Transact-SQL)

sys.dm_exec_trigger_stats (Transact-SQL)

ID of database.

For static SQL in a stored procedure, the ID of the database containing the

stored procedure. Null otherwise.

ID of object.

Is NULL for ad hoc and prepared SQL statements.

For a numbered stored procedure, this column returns the number of the

stored procedure. For more information, see

sys.numbered_procedures

(Transact-SQL)

.

Is NULL for ad hoc and prepared SQL statements.

1 = SQL text is encrypted.

0 = SQL text is not encrypted.

Text of the SQL query.

Is NULL for encrypted objects.

Requires

permission on the server.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.

ﾉ

## CROSS

## APPLY

## CROSS APPLY

## sys.dm_exec_requests

## sys.dm_exec_sql_text

## CROSS APPLY

## dbid

## dbid

```sql
VIEW SERVER STATE
```
