---
name: "sys.sp_revoke_login_from_proxy"
title: "sp_revoke_login_from_proxy"
category: "general"
description: "Removes access to a proxy for a security principal. Transact-SQL syntax conventions The name of the SQL Server login, server role, or database role for which to remove The ID of the proxy for which to remove access. must be specified, but both can't be specified."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_revoke_login_from_proxy
  [ @name = ]
  N
  'name'
  [ , [ @proxy_id = ] proxy_id ]
  [ , [ @proxy_name = ]
  N
  'proxy_name'
  ]
  [ ; ]
---

## Description

Removes access to a proxy for a security principal. Transact-SQL syntax conventions The name of the SQL Server login, server role, or database role for which to remove The ID of the proxy for which to remove access. must be specified, but both can't be specified. The name of the proxy for which to remove access. must be specified, but both can't be specified.

## Syntax

```sql
sp_revoke_login_from_proxy
[ @name = ]
N
'name'
[ , [ @proxy_id = ] proxy_id ]
[ , [ @proxy_name = ]
N
'proxy_name'
]
[ ; ]
```
