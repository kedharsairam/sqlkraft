---
name: "sys.sp_helpmergepublication"
title: "sp_helpmergepublication"
category: "general"
description: "Returns information about a merge publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions information about all merge publications in the current database. A flag to indicate returning rows. is an OUTPUT parameter of type indicates the publication is found. indicates the publication isn't found."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpmergepublication
  [ [ @publication = ]
  N
  'publication'
  ]
  [ , [ @found = ] found
  OUTPUT
  ]
  [ , [ @publication_id = ]
  'publication_id'
  OUTPUT
  ]
  [ , [ @reserved = ]
  N
  'reserved'
  ]
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

Returns information about a merge publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions information about all merge publications in the current database. A flag to indicate returning rows. is an OUTPUT parameter of type indicates the publication is found. indicates the publication isn't found. The publication identification number.

## Syntax

```sql
sp_helpmergepublication
[ [ @publication = ]
N
'publication'
]
[ , [ @found = ] found
OUTPUT
]
[ , [ @publication_id = ]
'publication_id'
OUTPUT
]
[ , [ @reserved = ]
N
'reserved'
]
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
