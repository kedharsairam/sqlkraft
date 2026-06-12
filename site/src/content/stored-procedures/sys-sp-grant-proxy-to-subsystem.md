---
name: "sys.sp_grant_proxy_to_subsystem"
title: "sp_grant_proxy_to_subsystem"
category: "general"
description: "Grants a proxy access to a subsystem. The proxy identification number of the proxy to grant access for. must be specified, but both can't be specified."
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

Grants a proxy access to a subsystem. The proxy identification number of the proxy to grant access for. must be specified, but both can't be specified.

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
