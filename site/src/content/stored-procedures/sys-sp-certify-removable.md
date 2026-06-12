---
name: "sys.sp_certify_removable"
title: "sp_certify_removable"
category: "general"
description: "Verifies that a database is correctly configured for distribution on removable media and reports Specifies the database to be verified. Gives ownership of the database and all database objects to the system administrator, and drops any user-created database users and nondefault permissions. This feature will be removed in a future version of SQL Server."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_certify_removable
              [ @dbname = ]
              N
              'dbname'
              [ , [ @autofix = ]
              N
              'autofix'
              ]
              [ ; ]
---

## Description

Verifies that a database is correctly configured for distribution on removable media and reports Specifies the database to be verified. Gives ownership of the database and all database objects to the system administrator, and drops any user-created database users and nondefault permissions. This feature will be removed in a future version of SQL Server.

## Syntax

```sql
sp_certify_removable
[ @dbname = ]
N
'dbname'
[ , [ @autofix = ]
N
'autofix'
]
[ ; ]
```
