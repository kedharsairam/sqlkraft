---
name: 'sys.sp_deletetracertokenhistory'
title: 'sp_deletetracertokenhistory'
category: 'general'
description: 'Removes tracer token records from the This stored procedure is executed at the Publisher on the publication database or at the Distributor on the distribution database. Transact-SQL syntax conventions The name of the publication in which the tracer token was inserted. with no default. This parameter is required. The ID of the tracer token to delete. tokens belonging to the publication are deleted.'
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

Removes tracer token records from the This stored procedure is executed at the Publisher on the publication database or at the Distributor on the distribution database. Transact-SQL syntax conventions The name of the publication in which the tracer token was inserted. with no default. This parameter is required. The ID of the tracer token to delete. tokens belonging to the publication are deleted. Tracer tokens inserted into the publication before this date are deleted.

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
