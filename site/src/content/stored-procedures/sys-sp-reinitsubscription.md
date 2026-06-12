---
name: "sys.sp_reinitsubscription"
title: "sp_reinitsubscription"
category: "general"
description: "Marks the subscription for reinitialization. This stored procedure is executed at the Publisher ."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_reinitsubscription
      [ [ @publication = ]
      N
      'publication'
      ]
      [ , [ @article = ]
      N
      'article'
      ]
      , [ @subscriber = ]
      N
      'subscriber'
      [ , [ @destination_db = ]
      N
      'destination_db'
      ]
      [ , [ @for_schema_change = ] for_schema_change ]
      [ , [ @publisher = ]
      N
      'publisher'
      ]
      [ , [ @ignore_distributor_failure = ] ignore_distributor_failure ]
      [ , [ @invalidate_snapshot = ] invalidate_snapshot ]
      [ ; ]
---

## Description

Marks the subscription for reinitialization. This stored procedure is executed at the Publisher.

## Syntax

```sql
sp_reinitsubscription
[ [ @publication = ]
N
'publication'
]
[ , [ @article = ]
N
'article'
]
, [ @subscriber = ]
N
'subscriber'
[ , [ @destination_db = ]
N
'destination_db'
]
[ , [ @for_schema_change = ] for_schema_change ]
[ , [ @publisher = ]
N
'publisher'
]
[ , [ @ignore_distributor_failure = ] ignore_distributor_failure ]
[ , [ @invalidate_snapshot = ] invalidate_snapshot ]
[ ; ]
```

## Permissions

Only members of the fixed server role, members of the fixed database role, or the creator of the subscription can execute. Reinitialize a Subscription Reinitialize Subscriptions Replication stored procedures (Transact-SQL)
## Examples

### Example 1

`sp_reinitsubscription`

### Example 2

`MessageInterval`

### Example 3

`sp_reinitsubscription`

### Example 4

`all`

### Example 5

`NULL`

### Example 6

`drop`

### Example 7

```sql
-- This script uses sqlcmd scripting variables. They are in the form
-- $(MyVariable). For information about how to use scripting variables
-- on the command line and in SQL Server Management Studio, see the
-- "Executing Replication Scripts" section in the topic
-- "Programming Replication Using System Stored Procedures".
DECLARE
@subscriptionDB
AS sysname;
```
