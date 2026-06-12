---
name: "sys.sp_showrowreplicainfo"
title: "sp_showrowreplicainfo"
category: "general"
description: "Displays information about a row in a table that is being used as an article in merge replication. This stored procedure is executed at the Publisher on the publication database. is useful to differentiate tables if a database contains multiple tables with the same name, but each table has a different owner."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_showrowreplicainfo
      [ [ @ownername = ]
      N
      'ownername'
      ]
      [ , [ @tablename = ]
      N
      'tablename'
      ]
      , [ @rowguid = ]
      'rowguid'
      [ , [ @show = ]
      N
      'show'
      ]
      [ ; ]
---

## Description

Displays information about a row in a table that is being used as an article in merge replication. This stored procedure is executed at the Publisher on the publication database. is useful to differentiate tables if a database contains multiple tables with the same name, but each table has a different owner.

## Syntax

```sql
sp_showrowreplicainfo
[ [ @ownername = ]
N
'ownername'
]
[ , [ @tablename = ]
N
'tablename'
]
, [ @rowguid = ]
'rowguid'
[ , [ @show = ]
N
'show'
]
[ ; ]
```
