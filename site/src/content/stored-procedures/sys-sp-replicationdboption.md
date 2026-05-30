---
name: "sys.sp_replicationdboption"
title: "sp_replicationdboption"
category: "general"
description: "Sets a replication database option for the specified database. This stored procedure is executed at the Publisher or Subscriber on any database. Transact-SQL syntax conventions The database for which the replication database option is being set. The replication database option to enable or disable. Database can be used for merge publications. Database can be used for other types of publications."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_replicationdboption
  [ @dbname = ]
  N
  'dbname'
  , [ @optname = ]
  N
  'optname'
  , [ @value = ] {
  N
  'true'
  |
  N
  'false'
  }
  [ , [ @ignore_distributor = ] ignore_distributor ]
  [ , [ @from_scripting = ] from_scripting ]
  [ ; ]
---

## Description

Sets a replication database option for the specified database. This stored procedure is executed at the Publisher or Subscriber on any database. Transact-SQL syntax conventions The database for which the replication database option is being set. The replication database option to enable or disable. Database can be used for merge publications. Database can be used for other types of publications.

## Syntax

```sql
sp_replicationdboption
[ @dbname = ]
N
'dbname'
, [ @optname = ]
N
'optname'
, [ @value = ] {
N
'true'
|
N
'false'
}
[ , [ @ignore_distributor = ] ignore_distributor ]
[ , [ @from_scripting = ] from_scripting ]
[ ; ]
```

## Permissions

Only members of the fixed server role or fixed database role can execute . Windows authentication logins must have a user account in the database representing their Windows user account. A user account representing a Windows group isn't sufficient. sp_addlogreader_agent (Transact-SQL) sp_addpublication_snapshot (Transact-SQL) sp_changepublication (Transact-SQL) sp_droppublication (Transact-SQL) sp_helppublication (Transact-SQL) sp_replicationdboption (Transact-SQL) Publish Data and Database Objects Related content
