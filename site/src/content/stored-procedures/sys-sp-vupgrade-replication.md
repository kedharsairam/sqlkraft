---
name: "sys.sp_vupgrade_replication"
title: "sp_vupgrade_replication"
category: "general"
description: "Activated by setup when upgrading a replication server. Upgrades schema and system data as needed to support replication at the current product level. Creates new replication system objects in system and user databases. This stored procedure is executed at the machine where the replication upgrade is to occur."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_vupgrade_replication
      [ [ @login = ]
      N
      'login'
      ]
      [ , [ @password = ]
      N
      'password'
      ]
      [ , [ @ver_old = ] ver_old ]
      [ , [ @force_remove = ] force_remove ]
      [ , [ @security_mode = ] security_mode ]
      [ , [ @db_id = ] db_id ]
      [ ; ]
---

## Description

Activated by setup when upgrading a replication server. Upgrades schema and system data as needed to support replication at the current product level. Creates new replication system objects in system and user databases. This stored procedure is executed at the machine where the replication upgrade is to occur. The system administrator login to use when creating new system objects in the Distribution

## Syntax

```sql
sp_vupgrade_replication
[ [ @login = ]
N
'login'
]
[ , [ @password = ]
N
'password'
]
[ , [ @ver_old = ] ver_old ]
[ , [ @force_remove = ] force_remove ]
[ , [ @security_mode = ] security_mode ]
[ , [ @db_id = ] db_id ]
[ ; ]
```
