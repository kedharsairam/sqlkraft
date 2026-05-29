---
name: 'sys.dm_exec_requests'
title: 'sys.dm_exec_requests'
category: 'execution'
description: 'Azure SQL Database Azure SQL Managed Instance Associates up to 128 bytes of binary information with the current session or connection. Transact-SQL syntax conventions constant, or a constant that is implicitly convertible to , to associate with the current session or connection. variable holding a context value to associate with the current session , SET CONTEXT_INFO affects the current session. T'
tags: ["execution", "dmv"]
pubDate: 2026-05-29
syntax: 'applicationintent=readonly'
---

## Description

Azure SQL Database Azure SQL Managed Instance Associates up to 128 bytes of binary information with the current session or connection. Transact-SQL syntax conventions constant, or a constant that is implicitly convertible to , to associate with the current session or connection. variable holding a context value to associate with the current session , SET CONTEXT_INFO affects the current session. The preferred way to retrieve the context information for the current session is to use the CONTEXT_INFO function. Session context information is also stored in the columns in the following system

## Syntax

```sql
applicationintent=readonly
```

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric This function returns the value either set for the current session or batch, or derived through use of the SET CONTEXT_INFO statement. Transact-SQL syntax conventions syntaxsql The value. If was not set: SQL Server returns NULL. SQL Database returns a unique session-specific GUID. The Multiple Active Result Sets (MARS) feature enables applications to run multiple batches, or requests, at the same time, on the same connection. When one of the MARS connection batches runs SET CONTEXT_INFO, the function returns the new context value, when the function runs in the same batch as the SET statement. If the function runs in one or more of the other connection batches, the function does not return the new value unless those batches started after completion of the batch that ran the SET statement. Requires no special permissions. The following system views store the context information, but querying these views directly requires SELECT and VIEW SERVER STATE permissions: Backup Devices Media sets, media families, and backup sets Tail-log backups ALTER DATABASE (Transact-SQL) DBCC SQLPERF (Transact-SQL) RESTORE statements (Transact-SQL) RESTORE FILELISTONLY (Transact-SQL) RESTORE HEADERONLY (Transact-SQL) RESTORE LABELONLY (Transact-SQL) RESTORE VERIFYONLY (Transact-SQL) sp_addumpdevice sp_configure sp_helpfile sp_helpfilegroup Server configuration options Piecemeal Restore of Databases With Memory-Optimized Tables Last updated on 03/02/2026 Related content

## Remarks

Applies to:

Azure SQL Database

Azure SQL Managed Instance

Associates up to 128 bytes of binary information with the current session or connection.

Transact-SQL syntax conventions

constant, or a constant that is implicitly convertible to

, to associate with the

current session or connection.

variable holding a context value to associate with the current session

or connection.

SET Statements

, SET CONTEXT_INFO affects the current session. The preferred way to

retrieve the context information for the current session is to use the CONTEXT_INFO function.

Session context information is also stored in the

columns in the following system

(deprecated)

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

### Example 3

```sql
DECLARE @Handle varbinary(64);
SELECT @Handle = sql_handle
FROM sys.dm_exec_requests
WHERE session_id = 52 and request_id = 0;
SELECT * FROM sys.fn_get_sql(@Handle);
GO
```
