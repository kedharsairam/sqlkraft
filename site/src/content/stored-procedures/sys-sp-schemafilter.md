---
name: "sys.sp_schemafilter"
title: "sp_schemafilter"
category: "general"
description: "Modifies and displays information on the schema that is excluded when listing Oracle tables The name of the non-SQL Server Publisher. The action to be taken on this schema. Adds the specified schema to the list of schemas that aren't eligible for publication."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_schemafilter
      [ @publisher = ]
      N
      'publisher'
      [ , [ @schema = ]
      N
      'schema'
      ]
      [ , [ @operation = ]
      N
      'operation'
      ]
      [ ; ]
---

## Description

Modifies and displays information on the schema that is excluded when listing Oracle tables The name of the non-SQL Server Publisher. The action to be taken on this schema. Adds the specified schema to the list of schemas that aren't eligible for publication.

## Syntax

```sql
sp_schemafilter
[ @publisher = ]
N
'publisher'
[ , [ @schema = ]
N
'schema'
]
[ , [ @operation = ]
N
'operation'
]
[ ; ]
```
