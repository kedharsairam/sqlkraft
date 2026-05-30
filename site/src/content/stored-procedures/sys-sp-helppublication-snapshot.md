---
name: "sys.sp_helppublication_snapshot"
title: "sp_helppublication_snapshot"
category: "general"
description: "Returns information on the Snapshot agent for a given publication. Execute this stored procedure at the Publisher on the publication database. Transact-SQL syntax conventions Specifies a non-SQL Server publisher. when you add an article to a SQL Server Publisher."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sys.sp_helppublication_snapshot
  [ @publication = ]
  N
  'publication'
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ ; ]
---

## Description

Returns information on the Snapshot agent for a given publication. Execute this stored procedure at the Publisher on the publication database. Transact-SQL syntax conventions Specifies a non-SQL Server publisher. when you add an article to a SQL Server Publisher.

## Syntax

```sql
sys.sp_helppublication_snapshot
[ @publication = ]
N
'publication'
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```
