---
name: "sys.sp_link_publication"
title: "sp_link_publication"
category: "general"
description: "Sets the configuration and security information used by synchronization triggers of immediate updating subscriptions when connecting to the Publisher. This stored procedure is executed at the Subscriber on the subscription database. Transact-SQL syntax conventions The name of the Publisher to link to. When you configure a Publisher with a remote Distributor, the values supplied for all , are sent "
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_link_publication
  [ @publisher = ]
  N
  'publisher'
  , [ @publisher_db = ]
  N
  'publisher_db'
  , [ @publication = ]
  N
  'publication'
  , [ @security_mode = ] security_mode
  [ , [ @login = ]
  N
  'login'
  ]
  [ , [ @password = ]
  N
  'password'
  ]
  [ , [ @distributor = ]
  N
  'distributor'
  ]
  [ ; ]
---

## Description

Sets the configuration and security information used by synchronization triggers of immediate updating subscriptions when connecting to the Publisher. This stored procedure is executed at the Subscriber on the subscription database. Transact-SQL syntax conventions The name of the Publisher to link to. When you configure a Publisher with a remote Distributor, the values supplied for all , are sent to the Distributor as plain

## Syntax

```sql
sp_link_publication
[ @publisher = ]
N
'publisher'
, [ @publisher_db = ]
N
'publisher_db'
, [ @publication = ]
N
'publication'
, [ @security_mode = ] security_mode
[ , [ @login = ]
N
'login'
]
[ , [ @password = ]
N
'password'
]
[ , [ @distributor = ]
N
'distributor'
]
[ ; ]
```
