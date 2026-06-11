---
name: "sys.sp_grant_publication_access"
title: "sp_grant_publication_access"
category: "general"
description: "Adds a login to the access list of the publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication to access. Identified for informational purposes only. Not supported."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_grant_publication_access
  [ @publication = ]
  N
  'publication'
  , [ @login = ]
  N
  'login'
  [ , [ @reserved = ]
  N
  'reserved'
  ]
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ ; ]
---

## Description

Adds a login to the access list of the publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication to access. Identified for informational purposes only. Not supported. Future compatibility is not

## Syntax

```sql
sp_grant_publication_access
[ @publication = ]
N
'publication'
, [ @login = ]
N
'login'
[ , [ @reserved = ]
N
'reserved'
]
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```
