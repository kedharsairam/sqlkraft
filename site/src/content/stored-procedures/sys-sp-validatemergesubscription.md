---
name: "sys.sp_validatemergesubscription"
title: "sp_validatemergesubscription"
category: "general"
description: "Performs a validation for the specified subscription. This stored procedure is executed at the Publisher on the publication database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_validatemergesubscription
  [ @publication = ]
  N
  'publication'
  , [ @subscriber = ]
  N
  'subscriber'
  , [ @subscriber_db = ]
  N
  'subscriber_db'
  , [ @level = ] level
  [ ; ]
---

## Description

Performs a validation for the specified subscription. This stored procedure is executed at the Publisher on the publication database.

## Syntax

```sql
sp_validatemergesubscription
[ @publication = ]
N
'publication'
, [ @subscriber = ]
N
'subscriber'
, [ @subscriber_db = ]
N
'subscriber_db'
, [ @level = ] level
[ ; ]
```
