---
name: "sys.sp_revoke_login_from_proxy"
title: "sp_revoke_login_from_proxy"
category: "general"
description: "Removes access to a proxy for a security principal."
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

Removes access to a proxy for a security principal.

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
