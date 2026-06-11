---
name: "sys.sp_helpdbfixedrole"
title: "sp_helpdbfixedrole"
category: "general"
description: "Returns a list of the fixed database roles. Transact-SQL syntax conventions The name of a fixed database role. is specified, only information about that role is returned; otherwise, a list and description of all fixed database roles is returned."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpdbfixedrole [ [ @rolename = ]
  N
  'rolename'
  ]
  [ ; ]
---

## Description

Returns a list of the fixed database roles. Transact-SQL syntax conventions The name of a fixed database role. is specified, only information about that role is returned; otherwise, a list and description of all fixed database roles is returned. Name of the fixed database role.

## Syntax

```sql
sp_helpdbfixedrole [ [ @rolename = ]
N
'rolename'
]
[ ; ]
```

## Examples

### Example 1

```sql
EXECUTE sp_helpdbfixedrole;
GO
```
