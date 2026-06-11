---
name: "sys.sp_requestpeerresponse"
title: "sp_requestpeerresponse"
category: "general"
description: "When executed from a node in a peer-to-peer topology, this procedure requests a response from every other node in the topology. By executing this procedure and reviewing the corresponding responses, you can guarantee that all previous commands are delivered to the responding nodes. This stored procedure is executed at the requesting node on any database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_requestpeerresponse
  [ @publication = ]
  N
  'publication'
  [ , [ @description = ]
  N
  'description'
  ]
  [ , [ @request_id = ] request_id
  OUTPUT
  ]
  [ ; ]
---

## Description

When executed from a node in a peer-to-peer topology, this procedure requests a response from every other node in the topology. By executing this procedure and reviewing the corresponding responses, you can guarantee that all previous commands are delivered to the responding nodes. This stored procedure is executed at the requesting node on any database. Transact-SQL syntax conventions The name of the publication in a peer-to-peer topology for which the status is being verified.

## Syntax

```sql
sp_requestpeerresponse
[ @publication = ]
N
'publication'
[ , [ @description = ]
N
'description'
]
[ , [ @request_id = ] request_id
OUTPUT
]
[ ; ]
```
