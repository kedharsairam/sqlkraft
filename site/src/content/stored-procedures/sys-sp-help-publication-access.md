---
name: "sys.sp_help_publication_access"
title: "sp_help_publication_access"
category: "general"
description: "Returns a list of all granted logins for a publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication to access. is specified and SQL Server Authentication is used, the available logins that appear at the Publisher but not at the Distributor are returned. is specified and Windows Authentication is used, t"
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

Returns a list of all granted logins for a publication. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication to access. is specified and SQL Server Authentication is used, the available logins that appear at the Publisher but not at the Distributor are returned. is specified and Windows Authentication is used, the logins that aren't specifically denied

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

Only members of the fixed server role or the fixed database role can execute . sp_grant_publication_access (Transact-SQL) sp_revoke_publication_access (Transact-SQL) System stored procedures (Transact-SQL) Related content
