---
name: "sys.sp_posttracertoken"
title: "sp_posttracertoken"
category: "general"
description: "This procedure posts a tracer token into the transaction log at the Publisher and begins the process of tracking latency statistics. when the tracer token is written to the transaction log; when the Log Reader Agent picks it up; and when the Distribution Agent applies it. This stored procedure is executed at the Publisher on the publication database. For more Measure Latency and Validate Connectio"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_posttracertoken
  [ @publication = ]
  N
  'publication'
  [ , [ @tracer_token_id = ] tracer_token_id
  OUTPUT
  ]
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ ; ]
---

## Description

This procedure posts a tracer token into the transaction log at the Publisher and begins the process of tracking latency statistics. when the tracer token is written to the transaction log; when the Log Reader Agent picks it up; and when the Distribution Agent applies it. This stored procedure is executed at the Publisher on the publication database. For more Measure Latency and Validate Connections for Transactional Replication

## Syntax

```sql
sp_posttracertoken
[ @publication = ]
N
'publication'
[ , [ @tracer_token_id = ] tracer_token_id
OUTPUT
]
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```

## Permissions

Only members of the fixed server role or the fixed database role can execute. Measure Latency and Validate Connections for Transactional Replication
