---
name: 'sys.fn_get_sql'
title: 'sys.fn_get_sql'
category: 'system'
description: 'Returns the text of the SQL statement for the specified SQL handle.'
tags: ["function"]
pubDate: 2026-05-29
---

The user needs VIEW SERVER STATE permission on the server.

Database administrators can use the fn_get_sql function, as shown in the following example, to

help diagnose problem processes. After an administrator identifies a problem session ID, the

administrator can retrieve the SQL handle for that session, call fn_get_sql with the handle, and

then use the start and end offsets to determine the SQL text of the problem session ID.

DBCC INPUTBUFFER (Transact-SQL)

sys.sysprocesses (Transact-SQL)

sys.dm_exec_requests (Transact-SQL)

See Also

```sql
DECLARE @Handle varbinary(64);
SELECT @Handle = sql_handle
FROM sys.dm_exec_requests
WHERE session_id = 52 and request_id = 0;
SELECT * FROM sys.fn_get_sql(@Handle);
GO
```
