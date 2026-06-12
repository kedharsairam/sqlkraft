---
name: "sys.sp_droparticle"
title: "sp_droparticle"
category: "general"
description: "Drops an article from a snapshot or transactional publication. An article can't be removed if one or more subscriptions to it exist. This stored procedure is executed at the Publisher on the The name of the publication that contains the article to be dropped."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_droparticle
              [ @publication = ]
              N
              'publication'
              , [ @article = ]
              N
              'article'
              [ , [ @ignore_distributor = ] ignore_distributor ]
              [ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
              [ , [ @publisher = ]
              N
              'publisher'
              ]
              [ , [ @from_drop_publication = ] from_drop_publication ]
              [ ; ]
---

## Description

Drops an article from a snapshot or transactional publication. An article can't be removed if one or more subscriptions to it exist. This stored procedure is executed at the Publisher on the The name of the publication that contains the article to be dropped.

## Syntax

```sql
sp_droparticle
[ @publication = ]
N
'publication'
, [ @article = ]
N
'article'
[ , [ @ignore_distributor = ] ignore_distributor ]
[ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
[ , [ @publisher = ]
N
'publisher'
]
[ , [ @from_drop_publication = ] from_drop_publication ]
[ ; ]
```

## Permissions

SQL Only members of the fixed server role or fixed database role can execute. Delete an Article Add Articles to and Drop Articles from Existing Publications sp_addarticle (Transact-SQL) sp_changearticle (Transact-SQL) sp_helparticle (Transact-SQL) sp_helparticlecolumns (Transact-SQL) Replication stored procedures (Transact-SQL)
