---
name: 'sys.sp_helplinkedsrvlogin'
title: 'sp_helplinkedsrvlogin'
category: 'general'
description: 'Provides information about login mappings defined against a specific linked server used for distributed queries and remote stored procedures. Transact-SQL syntax conventions The name of the linked server that the login mapping applies to. , all login mappings defined against all the linked servers defined in the local computer running SQL Server are returned. The SQL Server login on the local serv'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helplinkedsrvlogin
  [ [ @rmtsrvname = ]
  N
  'rmtsrvname'
  ]
  [ , [ @locallogin = ]
  N
  'locallogin'
  ]
  [ ; ]
---

## Description

Provides information about login mappings defined against a specific linked server used for distributed queries and remote stored procedures. Transact-SQL syntax conventions The name of the linked server that the login mapping applies to. , all login mappings defined against all the linked servers defined in the local computer running SQL Server are returned. The SQL Server login on the local server that's a mapping to the linked server

## Syntax

```sql
sp_helplinkedsrvlogin
[ [ @rmtsrvname = ]
N
'rmtsrvname'
]
[ , [ @locallogin = ]
N
'locallogin'
]
[ ; ]
```
