---
name: "sys.sp_helptracertokens"
title: "sp_helptracertokens"
category: "general"
description: "Returns one row for each tracer token that was inserted into a publication to determine latency. This stored procedure is executed at the Publisher on the publication database or at the Distributor on the distribution database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
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

Returns one row for each tracer token that was inserted into a publication to determine latency. This stored procedure is executed at the Publisher on the publication database or at the Distributor on the distribution database.

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
