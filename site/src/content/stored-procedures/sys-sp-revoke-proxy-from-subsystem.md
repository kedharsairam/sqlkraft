---
name: 'sys.sp_revoke_proxy_from_subsystem'
title: 'sp_revoke_proxy_from_subsystem'
category: 'general'
description: 'Revokes access to a subsystem from a proxy. Transact-SQL syntax conventions The proxy identification number of the proxy to revoke access from. must be specified, but both can''t be specified. The name of the proxy to revoke access from. must be specified, but both can''t be specified. The ID number of the subsystem to revoke access to.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_revoke_proxy_from_subsystem
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

Revokes access to a subsystem from a proxy. Transact-SQL syntax conventions The proxy identification number of the proxy to revoke access from. must be specified, but both can't be specified. The name of the proxy to revoke access from. must be specified, but both can't be specified. The ID number of the subsystem to revoke access to.

## Syntax

```sql
sp_revoke_proxy_from_subsystem
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

## Examples

### Example 1

```sql
Catalog application
proxy
```

### Example 2

```sql
USE
msdb;
GO
EXECUTE
dbo.sp_revoke_proxy_from_subsystem
@proxy_name =
'Catalog application proxy'
,
@subsystem_name = N
'Dts'
;
```
