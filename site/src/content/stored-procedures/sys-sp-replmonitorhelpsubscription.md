---
name: "sys.sp_replmonitorhelpsubscription"
title: "sp_replmonitorhelpsubscription"
category: "general"
description: "Returns current status information for subscriptions belonging to one or more publications at the Publisher and returns one row for each returned subscription. This stored procedure, which is used to monitor replication, is executed at the Distributor on the distribution database. Transact-SQL syntax conventions The name of the Publisher the status of which is being monitored."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_replmonitorhelpsubscription
  [ [ @publisher = ]
  N
  'publisher'
  ]
  [ , [ @publisher_db = ]
  N
  'publisher_db'
  ]
  [ , [ @publication = ]
  N
  'publication'
  ]
  [ , [ @publication_type = ] publication_type ]
  [ , [ @mode = ] mode ]
  [ , [ @topnum = ] topnum ]
  [ , [ @exclude_anonymous = ] exclude_anonymous ]
  [ , [ @refreshpolicy = ] refreshpolicy ]
  [ ; ]
---

## Description

Returns current status information for subscriptions belonging to one or more publications at the Publisher and returns one row for each returned subscription. This stored procedure, which is used to monitor replication, is executed at the Distributor on the distribution database. Transact-SQL syntax conventions The name of the Publisher the status of which is being monitored. , information is returned for all Publishers that use the Distributor.

## Syntax

```sql
sp_replmonitorhelpsubscription
[ [ @publisher = ]
N
'publisher'
]
[ , [ @publisher_db = ]
N
'publisher_db'
]
[ , [ @publication = ]
N
'publication'
]
[ , [ @publication_type = ] publication_type ]
[ , [ @mode = ] mode ]
[ , [ @topnum = ] topnum ]
[ , [ @exclude_anonymous = ] exclude_anonymous ]
[ , [ @refreshpolicy = ] refreshpolicy ]
[ ; ]
```

## Permissions

Only members of the or fixed database role on the distribution database can execute . Programmatically monitor replication Related content
