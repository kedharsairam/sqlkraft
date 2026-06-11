---
name: "sys.sp_helprole"
title: "sp_helprole"
category: "general"
description: "SQL database in Microsoft Fabric Returns information about the roles in the current database. Transact-SQL syntax conventions The name of a role in the current database. must exist in the current database. If isn't specified, information about all roles in the current database is returned."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helprole [ [ @rolename = ]
  N
  'rolename'
  ]
  [ ; ]
---

## Description

SQL database in Microsoft Fabric Returns information about the roles in the current database. Transact-SQL syntax conventions The name of a role in the current database. must exist in the current database. If isn't specified, information about all roles in the current database is returned. Name of the role in the current database.

## Syntax

```sql
sp_helprole [ [ @rolename = ]
N
'rolename'
]
[ ; ]
```
