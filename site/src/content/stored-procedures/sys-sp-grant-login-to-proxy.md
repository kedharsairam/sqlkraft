---
name: 'sys.sp_grant_login_to_proxy'
title: 'sp_grant_login_to_proxy'
category: 'general'
description: 'Grants a security principal access to a proxy. Transact-SQL syntax conventions The login name to grant access to. must be specified, or the stored The fixed server role to grant access to. must be specified, or the stored'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_grant_login_to_proxy
  [ [ @login_name = ]
  N
  'login_name'
  ]
  [ , [ @fixed_server_role = ]
  N
  'fixed_server_role'
  ]
  [ , [ @msdb_role = ]
  N
  'msdb_role'
  ]
  [ , [ @proxy_id = ] proxy_id ]
  [ , [ @proxy_name = ]
  N
  'proxy_name'
  ]
  [ ; ]
---

## Description

Grants a security principal access to a proxy. Transact-SQL syntax conventions The login name to grant access to. must be specified, or the stored The fixed server role to grant access to. must be specified, or the stored

## Syntax

```sql
sp_grant_login_to_proxy
[ [ @login_name = ]
N
'login_name'
]
[ , [ @fixed_server_role = ]
N
'fixed_server_role'
]
[ , [ @msdb_role = ]
N
'msdb_role'
]
[ , [ @proxy_id = ] proxy_id ]
[ , [ @proxy_name = ]
N
'proxy_name'
]
[ ; ]
```
