---
name: "sys.sp_who"
title: "sp_who"
category: "general"
description: "Provides information about current users, sessions, and processes in an instance of the SQL Server Database Engine. The information can be filtered to return only those processes that aren't idle, that belong to a specific user, or that belong to a specific session. Used to filter the result set. that identifies processes belonging to a particular login. is a sessio"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_who [ [ @loginame = ] {
              'login'
              | *session_id* |
              'ACTIVE'
              } ]
              [ ; ]
---

## Description

Provides information about current users, sessions, and processes in an instance of the SQL Server Database Engine. The information can be filtered to return only those processes that aren't idle, that belong to a specific user, or that belong to a specific session. Used to filter the result set. that identifies processes belonging to a particular login. is a session identification number belonging to the SQL Server instance.

## Syntax

```sql
sp_who [ [ @loginame = ] {
'login'
| *session_id* |
'ACTIVE'
} ]
[ ; ]
```

## Examples

### Example 1

```sql
@@
SPID
```

### Example 2

```sql
SELECT
@@SPID
AS
'ID'
,
SYSTEM_USER
AS
'Login Name'
,
USER
AS
'User Name'
;
ID Login Name User Name
------ ------------------------------ ------------------------------
54 SEATTLE\joanna dbo
```
