---
name: "sys.sp_helpmergedeleteconflictrows"
title: "sp_helpmergedeleteconflictrows"
category: "general"
description: "Returns information on data rows that lost delete conflicts. This stored procedure is executed at the Publisher on the publication database or at the Subscriber on the subscription database when decentralized conflict logging is used. specified, all conflicts qualified by the publication are returned."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpmergedeleteconflictrows
  [ [ @publication = ]
  N
  'publication'
  ]
  [ , [ @source_object = ]
  N
  'source_object'
  ]
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ , [ @publisher_db = ]
  N
  'publisher_db'
  ]
  [ , [ @logical_record_conflicts = ] logical_record_conflicts ]
  [ ; ]
---

## Description

Returns information on data rows that lost delete conflicts. This stored procedure is executed at the Publisher on the publication database or at the Subscriber on the subscription database when decentralized conflict logging is used. specified, all conflicts qualified by the publication are returned.

## Syntax

```sql
sp_helpmergedeleteconflictrows
[ [ @publication = ]
N
'publication'
]
[ , [ @source_object = ]
N
'source_object'
]
[ , [ @publisher = ]
N
'publisher'
]
[ , [ @publisher_db = ]
N
'publisher_db'
]
[ , [ @logical_record_conflicts = ] logical_record_conflicts ]
[ ; ]
```
