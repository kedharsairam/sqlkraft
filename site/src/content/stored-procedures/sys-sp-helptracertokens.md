---
name: "sys.sp_helptracertokens"
title: "sp_helptracertokens"
category: "general"
description: "Returns one row for each tracer token that was inserted into a publication to determine latency. This stored procedure is executed at the Publisher on the publication database or at the Distributor on the distribution database. Transact-SQL syntax conventions The name of the publication in which tracer tokens were inserted. should only be specified for non-SQL Server Publishers. The name of the pu"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helptracertokens
  [ @publication = ]
  N
  'publication'
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

Returns one row for each tracer token that was inserted into a publication to determine latency. This stored procedure is executed at the Publisher on the publication database or at the Distributor on the distribution database. Transact-SQL syntax conventions The name of the publication in which tracer tokens were inserted. should only be specified for non-SQL Server Publishers. The name of the publication database.

## Syntax

```sql
sp_helptracertokens
[ @publication = ]
N
'publication'
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
