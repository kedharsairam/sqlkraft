---
name: "sys.sp_helptext"
title: "sp_helptext"
category: "general"
description: "Displays the definition of a user-defined rule, default, unencrypted Transact-SQL stored procedure, user-defined Transact-SQL function, trigger, computed column, view, or system object such as a system stored procedure. The qualified or nonqualified name of a user-defined, schema-scoped object. , with no default."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
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

Displays the definition of a user-defined rule, default, unencrypted Transact-SQL stored procedure, user-defined Transact-SQL function, trigger, computed column, view, or system object such as a system stored procedure. The qualified or nonqualified name of a user-defined, schema-scoped object. , with no default.

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
