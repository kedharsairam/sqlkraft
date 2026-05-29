---
name: 'sys.sp_helppublication'
title: 'sp_helppublication'
category: 'general'
description: 'Returns information about a publication. For a SQL Server publication, execute this stored procedure at the Publisher on the publication database. For an Oracle publication, execute this stored procedure at the Distributor on any database. Transact-SQL syntax conventions The name of the publication to view. returns information about all publications. is an OUTPUT parameter of type means that no pu'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_helppublication
  [ [ @publication = ]
  N
  'publication'
  ]
  [ , [ @found = ] found
  OUTPUT
  ]
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ ; ]
---

## Description

Returns information about a publication. For a SQL Server publication, execute this stored procedure at the Publisher on the publication database. For an Oracle publication, execute this stored procedure at the Distributor on any database. Transact-SQL syntax conventions The name of the publication to view. returns information about all publications. is an OUTPUT parameter of type means that no publication matching

## Syntax

```sql
sys.sp_helppublication
[ [ @publication = ]
N
'publication'
]
[ , [ @found = ] found
OUTPUT
]
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```
