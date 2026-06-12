---
name: "sys.dm_exec_trigger_stats"
title: "sys.dm_exec_trigger_stats"
category: "execution"
description: "sys.dm_exec_procedure_stats (Transact-SQL) sys.dm_exec_trigger_stats (Transact-SQL) ID of database. For static SQL in a stored procedure, the ID of the database containing the stored procedure. Null otherwise. Is NULL for ad hoc and prepared SQL statements. For a numbered stored procedure, this column returns the number of the stored procedure. For more information, see sys.numbered_procedures Is"
tags: ["execution","dmv"]
pubDate: 2026-05-29
---

## Description

sys.dm_exec_procedure_stats (Transact-SQL) sys.dm_exec_trigger_stats (Transact-SQL) ID of database. For static SQL in a stored procedure, the ID of the database containing the stored procedure. Null otherwise. Is NULL for ad hoc and prepared SQL statements. For a numbered stored procedure, this column returns the number of the stored procedure. For more information, see sys.numbered_procedures Is NULL for ad hoc and prepared SQL statements. 1 = SQL text is encrypted. 0 = SQL text is not encrypted. Text of the SQL query. Is NULL for encrypted objects. permission on the server. Requires VIEW SERVER PERFORMANCE STATE permission on the server.

## Remarks

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

Is NULL for ad hoc and prepared SQL statements.

1 = SQL text is encrypted.

0 = SQL text is not encrypted.

Text of the SQL query.

Is NULL for encrypted objects.

permission on the server.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.

## Code Blocks

```sql
VIEW SERVER STATE
```
