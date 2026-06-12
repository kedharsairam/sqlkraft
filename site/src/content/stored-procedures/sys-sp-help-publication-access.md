---
name: "sys.sp_help_publication_access"
title: "sp_help_publication_access"
category: "general"
description: "Returns a list of all granted logins for a publication. This stored procedure is executed at the Publisher on the publication database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_help_publication_access
  [ @publication = ]
  N
  'publication'
  [ , [ @return_granted = ] return_granted ]
  [ , [ @login = ]
  N
  'login'
  ]
  [ , [ @initial_list = ] initial_list ]
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ ; ]
---

## Description

Returns a list of all granted logins for a publication. This stored procedure is executed at the Publisher on the publication database.

## Syntax

```sql
sp_help_publication_access
[ @publication = ]
N
'publication'
[ , [ @return_granted = ] return_granted ]
[ , [ @login = ]
N
'login'
]
[ , [ @initial_list = ] initial_list ]
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```

## Permissions

Only members of the fixed server role or the fixed database role can execute. sp_grant_publication_access (Transact-SQL) sp_revoke_publication_access (Transact-SQL) System stored procedures (Transact-SQL)
