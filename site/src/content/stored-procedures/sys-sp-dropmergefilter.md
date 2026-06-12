---
name: "sys.sp_dropmergefilter"
title: "sp_dropmergefilter"
category: "general"
description: "drops all the merge filter columns defined on the merge filter that is to be dropped. This stored procedure is executed at the Publisher on the The name of the filter to be dropped."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dropmergefilter
  [ @publication = ]
  N
  'publication'
  , [ @article = ]
  N
  'article'
  , [ @filtername = ]
  N
  'filtername'
  [ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
  [ , [ @force_reinit_subscription = ] force_reinit_subscription ]
  [ ; ]
---

## Description

drops all the merge filter columns defined on the merge filter that is to be dropped. This stored procedure is executed at the Publisher on the The name of the filter to be dropped.

## Syntax

```sql
sp_dropmergefilter
[ @publication = ]
N
'publication'
, [ @article = ]
N
'article'
, [ @filtername = ]
N
'filtername'
[ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
[ , [ @force_reinit_subscription = ] force_reinit_subscription ]
[ ; ]
```
