---
name: "sys.sp_dropmergepublication"
title: "sp_dropmergepublication"
category: "general"
description: "Drops a merge publication and its associated Snapshot Agent. All subscriptions must be dropped before dropping a merge publication. The articles in the publication are dropped automatically. This stored procedure is executed at the Publisher on the publication database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dropmergepublication
              [ @publication = ]
              N
              'publication'
              [ , [ @ignore_distributor = ] ignore_distributor ]
              [ , [ @reserved = ] reserved ]
              [ , [ @ignore_merge_metadata = ] ignore_merge_metadata ]
              [ ; ]
---

## Description

Drops a merge publication and its associated Snapshot Agent. All subscriptions must be dropped before dropping a merge publication. The articles in the publication are dropped automatically. This stored procedure is executed at the Publisher on the publication database.

## Syntax

```sql
sp_dropmergepublication
[ @publication = ]
N
'publication'
[ , [ @ignore_distributor = ] ignore_distributor ]
[ , [ @reserved = ] reserved ]
[ , [ @ignore_merge_metadata = ] ignore_merge_metadata ]
[ ; ]
```

## Permissions

Only members of the fixed server role or the fixed database role can execute. Delete a Publication sp_addmergepublication (Transact-SQL) sp_changemergepublication (Transact-SQL) sp_helpmergepublication (Transact-SQL) Replication stored procedures (Transact-SQL)
