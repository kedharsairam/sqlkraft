---
name: "sys.sp_dbremove"
title: "sp_dbremove"
category: "general"
description: "Removes a database and all files associated with that database. Transact-SQL syntax conventions The name of the database to be removed. A flag provided for backward compatibility only and is currently ignored. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature."
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

Removes a database and all files associated with that database. Transact-SQL syntax conventions The name of the database to be removed. A flag provided for backward compatibility only and is currently ignored. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

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
