---
name: "sys.sp_prepexecrpc"
title: "sp_prepexecrpc"
category: "general"
description: "Prepares and executes a parameterized stored procedure call specified using a remote procedure call (RPC) identifier. Transact-SQL syntax conventions The SQL Server-generated prepared handle identifier. is a required parameter with an Defines the stored procedure call using ODBC canonical syntax. Arguments for extended stored procedures must be entered in the specific order as section."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_prepexecrpc handle
  OUTPUT
  ,
  RPCC
  all
  [ , bound_param ] [ , ...n ]
  [ ; ]
---

## Description

Prepares and executes a parameterized stored procedure call specified using a remote procedure call (RPC) identifier. Transact-SQL syntax conventions The SQL Server-generated prepared handle identifier. is a required parameter with an Defines the stored procedure call using ODBC canonical syntax. Arguments for extended stored procedures must be entered in the specific order as section. If the parameters are entered out of order, an error

## Syntax

```sql
sp_prepexecrpc handle
OUTPUT
,
RPCC all
[ , bound_param ] [ , ...n ]
[ ; ]
```
