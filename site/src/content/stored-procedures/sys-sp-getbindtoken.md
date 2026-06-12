---
name: "sys.sp_getbindtoken"
title: "sp_getbindtoken"
category: "general"
description: "returns a valid token only when the stored procedure is executed inside an active transaction. Otherwise, the Database Engine returns an error message. For example: Here's the result set. is used to enlist a distributed transaction connection inside an open transaction, SQL Server returns the same token. For example: sp_getbindtoken (Transact-SQL) srv_getbindtoken (Extended Stored Procedure API) S"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_getbindtoken [ @out_token = ]
  'out_token'
  OUTPUT
  [ ; ]
---

## Description

returns a valid token only when the stored procedure is executed inside an active transaction. Otherwise, the Database Engine returns an error message. For example: Here's the result set. is used to enlist a distributed transaction connection inside an open transaction, SQL Server returns the same token. For example: sp_getbindtoken (Transact-SQL) srv_getbindtoken (Extended Stored Procedure API) System stored procedures (Transact-SQL)
## Syntax

```sql
sp_getbindtoken [ @out_token = ]
'out_token'
OUTPUT
[ ; ]
```

## Remarks

returns a valid token only when the stored procedure is executed inside an

active transaction. Otherwise, the Database Engine returns an error message. For example:

Here's the result set.

is used to enlist a distributed transaction connection inside an open

transaction, SQL Server returns the same token. For example:

sp_getbindtoken (Transact-SQL)

srv_getbindtoken (Extended Stored Procedure API)

System stored procedures (Transact-SQL)
