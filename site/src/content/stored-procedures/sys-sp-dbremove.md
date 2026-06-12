---
name: "sys.sp_dbremove"
title: "sp_dbremove"
category: "general"
description: "Removes a database and all files associated with that database."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dbremove
  [ [ @dbname = ]
  N
  'dbname'
  ]
  [ , [ @dropdev = ]
  'dropdev'
  ]
  [ ; ]
---

## Description

Removes a database and all files associated with that database.

## Syntax

```sql
sp_dbremove
[ [ @dbname = ]
N
'dbname'
]
[ , [ @dropdev = ]
'dropdev'
]
[ ; ]
```

## Examples

### Example 1

`sales`

### Example 2

```sql
EXECUTE sp_dbremove sales;
```
