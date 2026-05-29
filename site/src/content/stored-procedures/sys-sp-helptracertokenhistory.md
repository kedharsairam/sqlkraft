---
name: 'sys.sp_helptracertokenhistory'
title: 'sp_helptracertokenhistory'
category: 'general'
description: 'Returns detailed latency information for specified tracer tokens, with one row being returned for each Subscriber. This stored procedure is executed at the Publisher on the publication database or at the Distributor on the distribution database. Transact-SQL syntax conventions The name of the publication in which the tracer token was inserted. The ID of the tracer token in the table, for which his'
tags: ["stored-procedure"]
pubDate: 2026-05-29
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

Returns detailed latency information for specified tracer tokens, with one row being returned for each Subscriber. This stored procedure is executed at the Publisher on the publication database or at the Distributor on the distribution database. Transact-SQL syntax conventions The name of the publication in which the tracer token was inserted. The ID of the tracer token in the table, for which history information is

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

Only members of the fixed server role, the fixed database role in the publication database, or fixed database or roles in the distribution database can execute . Measure Latency and Validate Connections for Transactional Replication sp_deletetracertokenhistory (Transact-SQL) Related content Only members of the fixed server role, the fixed database role in the publication database, or fixed database or roles in the distribution database can execute . Measure Latency and Validate Connections for Transactional Replication sp_deletetracertokenhistory (Transact-SQL) Related content Only members of the fixed server role or the fixed database role can execute . Measure Latency and Validate Connections for Transactional Replication Related content
