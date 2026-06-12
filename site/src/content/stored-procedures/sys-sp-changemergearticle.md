---
name: "sys.sp_changemergearticle"
title: "sp_changemergearticle"
category: "general"
description: "Changes the properties of a merge article. This stored procedure is executed at the Publisher The name of the publication in which the article exists."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_changemergearticle
  [ @publication = ]
  N
  'publication'
  , [ @article = ]
  N
  'article'
  [ , [ @property = ]
  N
  'property'
  ]
  [ , [ @value = ]
  N
  'value'
  ]
  [ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
  [ , [ @force_reinit_subscription = ] force_reinit_subscription ]
  [ ; ]
---

## Description

Changes the properties of a merge article. This stored procedure is executed at the Publisher The name of the publication in which the article exists.

## Syntax

```sql
sp_changemergearticle
[ @publication = ]
N
'publication'
, [ @article = ]
N
'article'
[ , [ @property = ]
N
'property'
]
[ , [ @value = ]
N
'value'
]
[ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
[ , [ @force_reinit_subscription = ] force_reinit_subscription ]
[ ; ]
```

## Permissions

Only members of the fixed server role or fixed database role can execute. View and Modify Article Properties Change Publication and Article Properties sp_addmergearticle (Transact-SQL) sp_dropmergearticle (Transact-SQL) sp_helpmergearticle (Transact-SQL) Replication stored procedures (Transact-SQL)
