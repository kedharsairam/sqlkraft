---
name: 'sys.sp_validatemergesubscription'
title: 'sp_validatemergesubscription'
category: 'general'
description: 'Performs a validation for the specified subscription. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the subscription database. The type of validation to perform. , and can be one of these values.'
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

Performs a validation for the specified subscription. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the subscription database. The type of validation to perform. , and can be one of these values.

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
