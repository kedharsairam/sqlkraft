---
name: "sys.sp_change_subscription_properties"
title: "sp_change_subscription_properties"
category: "general"
description: "Updates information for pull subscriptions. This stored procedure is executed at the Subscriber Transact-SQL syntax conventions The name of the Publisher database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_change_subscription_properties
  [ @publisher = ]
  N
  'publisher'
  , [ @publisher_db = ]
  N
  'publisher_db'
  , [ @publication = ]
  N
  'publication'
  , [ @property = ]
  N
  'property'
  , [ @value = ]
  N
  'value'
  [ , [ @publication_type = ] publication_type ]
  [ ; ]
---

## Description

Updates information for pull subscriptions. This stored procedure is executed at the Subscriber Transact-SQL syntax conventions The name of the Publisher database.

## Syntax

```sql
sp_change_subscription_properties
[ @publisher = ]
N
'publisher'
, [ @publisher_db = ]
N
'publisher_db'
, [ @publication = ]
N
'publication'
, [ @property = ]
N
'property'
, [ @value = ]
N
'value'
[ , [ @publication_type = ] publication_type ]
[ ; ]
```

## Permissions

Only members of the fixed server role or fixed database role can execute . View and Modify Pull Subscription Properties sp_addmergepullsubscription (Transact-SQL) sp_addmergepullsubscription_agent (Transact-SQL) sp_addpullsubscription (Transact-SQL) sp_addpullsubscription_agent (Transact-SQL) System stored procedures (Transact-SQL) Related content
