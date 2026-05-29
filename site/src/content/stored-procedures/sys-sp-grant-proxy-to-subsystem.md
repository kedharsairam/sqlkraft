---
name: 'sys.sp_grant_proxy_to_subsystem'
title: 'sp_grant_proxy_to_subsystem'
category: 'general'
description: 'Grants a proxy access to a subsystem. Transact-SQL syntax conventions The proxy identification number of the proxy to grant access for. must be specified, but both can''t be specified. The name of the proxy to grant access for. must be specified, but both can''t be specified. The ID number of the subsystem to grant access to.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_grant_proxy_to_subsystem
  [ [ @proxy_id = ] proxy_id ]
  [ , [ @proxy_name = ]
  N
  'proxy_name'
  ]
  [ , [ @subsystem_id = ] subsystem_id ]
  [ , [ @subsystem_name = ]
  N
  'subsystem_name'
  ]
  [ ; ]
---

## Description

Grants a proxy access to a subsystem. Transact-SQL syntax conventions The proxy identification number of the proxy to grant access for. must be specified, but both can't be specified. The name of the proxy to grant access for. must be specified, but both can't be specified. The ID number of the subsystem to grant access to.

## Syntax

```sql
sp_grant_proxy_to_subsystem
[ [ @proxy_id = ] proxy_id ]
[ , [ @proxy_name = ]
N
'proxy_name'
]
[ , [ @subsystem_id = ] subsystem_id ]
[ , [ @subsystem_name = ]
N
'subsystem_name'
]
[ ; ]
```
