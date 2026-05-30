---
name: "sys.sp_enum_login_for_proxy"
title: "sp_enum_login_for_proxy"
category: "general"
description: "Lists associations between security principals and proxies. Transact-SQL syntax conventions The name of a SQL Server principal, login, server role, or database role to list proxies for. The proxy identification number of the proxy to list information for. The name of the proxy to list information for."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_enum_login_for_proxy
  [ [ @name = ]
  N
  'name'
  ]
  [ , [ @proxy_id = ] proxy_id ]
  [ , [ @proxy_name = ]
  N
  'proxy_name'
  ]
  [ ; ]
---

## Description

Lists associations between security principals and proxies. Transact-SQL syntax conventions The name of a SQL Server principal, login, server role, or database role to list proxies for. The proxy identification number of the proxy to list information for. The name of the proxy to list information for.

## Syntax

```sql
sp_enum_login_for_proxy
[ [ @name = ]
N
'name'
]
[ , [ @proxy_id = ] proxy_id ]
[ , [ @proxy_name = ]
N
'proxy_name'
]
[ ; ]
```
