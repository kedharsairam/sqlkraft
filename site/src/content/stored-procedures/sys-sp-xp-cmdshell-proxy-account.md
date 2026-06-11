---
name: "sys.sp_xp_cmdshell_proxy_account"
title: "sp_xp_cmdshell_proxy_account"
category: "general"
description: "Creates a proxy credential for Transact-SQL syntax conventions Specifies that the proxy credential should be deleted. Specifies the Windows account to be the proxy. is disabled by default. To enable Arguments for extended stored procedures must be entered in the specific order as section."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_xp_cmdshell_proxy_account [
  NULL
  | {
  'account_name'
  ,
  'password'
  } ]
  [ ; ]
---

## Description

Creates a proxy credential for Transact-SQL syntax conventions Specifies that the proxy credential should be deleted. Specifies the Windows account to be the proxy. is disabled by default. To enable Arguments for extended stored procedures must be entered in the specific order as section. If the parameters are entered out of order, an error

## Syntax

```sql
sp_xp_cmdshell_proxy_account [
NULL
| {
'account_name'
,
'password'
} ]
[ ; ]
```
