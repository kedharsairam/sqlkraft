---
name: "sys.sp_helptracertokenhistory"
title: "sp_helptracertokenhistory"
category: "general"
description: "Returns detailed latency information for specified tracer tokens, with one row being returned for each Subscriber. This stored procedure is executed at the Publisher on the publication database or at the Distributor on the distribution database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_helptracertokenhistory
      [ @publication = ]
      N
      'publication'
      , [ @tracer_id = ] tracer_id
      [ , [ @publisher = ]
      N
      'publisher'
      ]
      [ , [ @publisher_db = ]
      N
      'publisher_db'
      ]
      [ ; ]
---

## Description

Returns detailed latency information for specified tracer tokens, with one row being returned for each Subscriber. This stored procedure is executed at the Publisher on the publication database or at the Distributor on the distribution database.

## Syntax

```sql
sp_helptracertokenhistory
[ @publication = ]
N
'publication'
, [ @tracer_id = ] tracer_id
[ , [ @publisher = ]
N
'publisher'
]
[ , [ @publisher_db = ]
N
'publisher_db'
]
[ ; ]
```

## Permissions

Only members of the fixed server role, the fixed database role in the publication database, or fixed database or roles in the distribution database can execute. Measure Latency and Validate Connections for Transactional Replication sp_deletetracertokenhistory (Transact-SQL)
