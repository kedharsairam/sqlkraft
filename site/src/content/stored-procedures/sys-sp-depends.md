---
name: "sys.sp_depends"
title: "sp_depends"
category: "general"
description: "Displays information about database object dependencies, such as the views and procedures that depend on a table or view, and the tables and views that are depended on by the view or procedure. References to objects outside the current database aren't reported. This feature will be removed in a future version of SQL Server. Avoid using this feature in new developmen"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_depends [ @objname = ]
              N
              'objname'
              <objname>
              ::=
              {
              [ database_name. [ schema_name ] . | schema_name. ]
              object_name
              }
              [ ; ]
---

## Description

Displays information about database object dependencies, such as the views and procedures that depend on a table or view, and the tables and views that are depended on by the view or procedure. References to objects outside the current database aren't reported. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_depends [ @objname = ]
N
'objname'
<objname>
::=
{
[ database_name. [ schema_name ]. | schema_name. ]
object_name
}
[ ; ]
```
