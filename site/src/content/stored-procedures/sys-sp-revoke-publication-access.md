---
name: "sys.sp_revoke_publication_access"
title: "sp_revoke_publication_access"
category: "general"
description: "Removes the login from a publications access list. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication to access. Identified for informational purposes only. Not supported."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_revoke_publication_access
  [ @publication = ]
  N
  'publication'
  , [ @login = ]
  N
  'login'
  [ , [ @publisher = ]
  N
  'publisher'
  ]
  [ ; ]
---

## Description

Removes the login from a publications access list. This stored procedure is executed at the Publisher on the publication database. Transact-SQL syntax conventions The name of the publication to access. Identified for informational purposes only. Not supported. Future compatibility is not

## Syntax

```sql
sp_revoke_publication_access
[ @publication = ]
N
'publication'
, [ @login = ]
N
'login'
[ , [ @publisher = ]
N
'publisher'
]
[ ; ]
```

## Permissions

is used in snapshot, transactional, and merge replication. can be called repeatedly. Only members of the fixed server role or the fixed database role can execute . sp_grant_publication_access (Transact-SQL) sp_help_publication_access (Transact-SQL) Secure the Publisher System stored procedures (Transact-SQL) Related content
