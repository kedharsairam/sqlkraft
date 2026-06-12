---
name: "sys.sp_droppullsubscription"
title: "sp_droppullsubscription"
category: "general"
description: "Drops a subscription at the current database of the Subscriber. This stored procedure is executed at the Subscriber on the pull subscription database. dropped at all the Publishers."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_droppullsubscription
  [ @publisher = ]
  N
  'publisher'
  [ , [ @publisher_db = ]
  N
  'publisher_db'
  ]
  , [ @publication = ]
  N
  'publication'
  [ , [ @reserved = ] reserved ]
  [ , [ @from_backup = ] from_backup ]
  [ ; ]
---

## Description

Drops a subscription at the current database of the Subscriber. This stored procedure is executed at the Subscriber on the pull subscription database. dropped at all the Publishers.

## Syntax

```sql
sp_droppullsubscription
[ @publisher = ]
N
'publisher'
[ , [ @publisher_db = ]
N
'publisher_db'
]
, [ @publication = ]
N
'publication'
[ , [ @reserved = ] reserved ]
[ , [ @from_backup = ] from_backup ]
[ ; ]
```

## Permissions

Only members of the fixed server role or the user who created the pull subscription can execute. The fixed database role is only able to execute if the user who created the pull subscription belongs to this role. Delete a Pull Subscription sp_addpullsubscription (Transact-SQL) sp_change_subscription_properties (Transact-SQL) sp_helppullsubscription (Transact-SQL) sp_dropsubscription (Transact-SQL)
