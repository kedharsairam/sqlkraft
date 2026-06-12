---
name: "sys.dm_exec_requests"
title: "sys.dm_exec_requests"
category: "execution"
description: "Associates up to 128 bytes of binary information with the current session or connection. constant, or a constant that is implicitly convertible to , to associate with the current session or connection. variable holding a context value to associate with the current session , SET CONTEXT_INFO affects the current session. T"
tags: ["execution","dmv"]
pubDate: 2026-05-29
syntax: "applicationintent=readonly"
---

## Description

Associates up to 128 bytes of binary information with the current session or connection. constant, or a constant that is implicitly convertible to , to associate with the current session or connection. variable holding a context value to associate with the current session , SET CONTEXT_INFO affects the current session. The preferred way to retrieve the context information for the current session is to use the CONTEXT_INFO function. Session context information is also stored in the columns in the following system

## Syntax

```sql
applicationintent=readonly
```

## Permissions

## Remarks

Associates up to 128 bytes of binary information with the current session or connection.

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
SELECT t.*
FROM sys.dm_exec_requests
AS r
CROSS
APPLY sys.dm_exec_sql_text(r.sql_handle)
AS t
WHERE session_id = 59
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
