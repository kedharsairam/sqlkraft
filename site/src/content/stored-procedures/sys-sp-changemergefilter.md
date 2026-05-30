---
name: "sys.sp_changemergefilter"
title: "sp_changemergefilter"
category: "general"
description: "Changes some merge filter properties. This stored procedure is executed at the Publisher on Transact-SQL syntax conventions The current name of the filter. The name of the property to change."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_changemergefilter
  [ @publication = ]
  N
  'publication'
  , [ @article = ]
  N
  'article'
  , [ @filtername = ]
  N
  'filtername'
  , [ @property = ]
  N
  'property'
  , [ @value = ]
  N
  'value'
  [ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
  [ , [ @force_reinit_subscription = ] force_reinit_subscription ]
  [ ; ]
---

## Description

Changes some merge filter properties. This stored procedure is executed at the Publisher on Transact-SQL syntax conventions The current name of the filter. The name of the property to change.

## Syntax

```sql
sp_changemergefilter
[ @publication = ]
N
'publication'
, [ @article = ]
N
'article'
, [ @filtername = ]
N
'filtername'
, [ @property = ]
N
'property'
, [ @value = ]
N
'value'
[ , [ @force_invalidate_snapshot = ] force_invalidate_snapshot ]
[ , [ @force_reinit_subscription = ] force_reinit_subscription ]
[ ; ]
```
