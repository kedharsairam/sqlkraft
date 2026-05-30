---
name: "sys.sp_replsetoriginator"
title: "sp_replsetoriginator"
category: "general"
description: "Used to invoke loopback detection and handling in bidirectional transactional replication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the server where the transaction is being applied. The name of the database where the transaction is being applied. Identified for informational purposes only. Not supported. Future com"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_replsetoriginator
  [ @originator_srv = ]
  N
  'originator_srv'
  , [ @originator_db = ]
  N
  'originator_db'
  [ , [ @publication = ]
  N
  'publication'
  ]
  [ ; ]
---

## Description

Used to invoke loopback detection and handling in bidirectional transactional replication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the server where the transaction is being applied. The name of the database where the transaction is being applied. Identified for informational purposes only. Not supported. Future compatibility is not

## Syntax

```sql
sp_replsetoriginator
[ @originator_srv = ]
N
'originator_srv'
, [ @originator_db = ]
N
'originator_db'
[ , [ @publication = ]
N
'publication'
]
[ ; ]
```

## Permissions

is executed by the Distribution Agent to record the source of transactions applied by replication. This information is used to invoke loopback detection for bidirectional transactional subscriptions that have the loopback property set. Only members of the fixed server role at the Publisher, members of the fixed database role on the publication database, or users in the publication access list (PAL) can execute . System stored procedures (Transact-SQL) Related content
