---
name: "sys.sp_enum_proxy_for_subsystem"
title: "sp_enum_proxy_for_subsystem"
category: "general"
description: "Lists permissions for SQL Server Agent proxies to access subsystems. Transact-SQL syntax conventions The identification number of the proxy to list information for."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_enum_proxy_for_subsystem
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

Lists permissions for SQL Server Agent proxies to access subsystems. Transact-SQL syntax conventions The identification number of the proxy to list information for. The name of the proxy to list information for. The identification number of the subsystem to list information for.

## Syntax

```sql
sp_enum_proxy_for_subsystem
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
