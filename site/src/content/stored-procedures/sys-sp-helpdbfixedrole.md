---
name: "sys.sp_helpdbfixedrole"
title: "sp_helpdbfixedrole"
category: "general"
description: "Returns a list of the fixed database roles."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_helpdbfixedrole [ [ @rolename = ]
      N
      'rolename'
      ]
      [ ; ]
---

## Description

Returns a list of the fixed database roles.

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
