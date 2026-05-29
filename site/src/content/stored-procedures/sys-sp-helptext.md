---
name: "sys.sp_helptext"
title: "sp_helptext"
category: "general"
description: "SQL database in Microsoft Fabric Displays the definition of a user-defined rule, default, unencrypted Transact-SQL stored procedure, user-defined Transact-SQL function, trigger, computed column, view, or system object such as a system stored procedure. Transact-SQL syntax conventions The qualified or nonqualified name of a user-defined, schema-scoped object. , with no default. Quotation marks are "
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helptext
  [ @objname = ]
  N
  'objname'
  [ , [ @columnname = ]
  N
  'columnname'
  ]
  [ ; ]
---

## Description

SQL database in Microsoft Fabric Displays the definition of a user-defined rule, default, unencrypted Transact-SQL stored procedure, user-defined Transact-SQL function, trigger, computed column, view, or system object such as a system stored procedure. Transact-SQL syntax conventions The qualified or nonqualified name of a user-defined, schema-scoped object. , with no default. Quotation marks are required only if a qualified object is

## Syntax

```sql
sp_helptext
[ @objname = ]
N
'objname'
[ , [ @columnname = ]
N
'columnname'
]
[ ; ]
```
