---
name: "sys.sp_dropmergearticle"
title: "sp_dropmergearticle"
category: "general"
description: "Removes an article from a merge publication. This stored procedure is executed at the Publisher on the publication database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dropmergearticle
              [ @publication = ]
              N
              'publication'
              , [ @article = ]
              N
              'article'
              [ , [ @ignore_distributor = ] ignore_distributor ]
              [ , [ @reserved = ] reserved ]
              [ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
              [ , [ @force_reinit_subscription = ] force_reinit_subscription ]
              [ , [ @ignore_merge_metadata = ] ignore_merge_metadata ]
              [ ; ]
---

## Description

Removes an article from a merge publication. This stored procedure is executed at the Publisher on the publication database.

## Syntax

```sql
sp_dropmergearticle
[ @publication = ]
N
'publication'
, [ @article = ]
N
'article'
[ , [ @ignore_distributor = ] ignore_distributor ]
[ , [ @reserved = ] reserved ]
[ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
[ , [ @force_reinit_subscription = ] force_reinit_subscription ]
[ , [ @ignore_merge_metadata = ] ignore_merge_metadata ]
[ ; ]
```
