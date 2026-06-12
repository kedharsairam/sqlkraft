---
name: "sys.sp_deletetracertokenhistory"
title: "sp_deletetracertokenhistory"
category: "general"
description: "Removes tracer token records from the This stored procedure is executed at the Publisher on the publication database or at the Distributor on the distribution database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_deletetracertokenhistory
  [ @publication = ]
  N
  'publication'
  [ , [ @tracer_id = ] tracer_id ]
  [ , [ @cutoff_date = ] cutoff_date ]
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

Removes tracer token records from the This stored procedure is executed at the Publisher on the publication database or at the Distributor on the distribution database.

## Syntax

```sql
sp_deletetracertokenhistory
[ @publication = ]
N
'publication'
[ , [ @tracer_id = ] tracer_id ]
[ , [ @cutoff_date = ] cutoff_date ]
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
