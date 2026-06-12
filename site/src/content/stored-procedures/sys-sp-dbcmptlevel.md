---
name: "sys.sp_dbcmptlevel"
title: "sp_dbcmptlevel"
category: "general"
description: "Sets certain database behaviors to be compatible with the specified version of SQL Server."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_dbcmptlevel
      [ [ @dbname = ]
      N
      'dbname'
      ]
      [ , [ @new_cmptlevel = ] new_cmptlevel
      OUTPUT
      ]
      [ ; ]
---

## Description

Sets certain database behaviors to be compatible with the specified version of SQL Server.

## Syntax

```sql
sp_dbcmptlevel
[ [ @dbname = ]
N
'dbname'
]
[ , [ @new_cmptlevel = ] new_cmptlevel
OUTPUT
]
[ ; ]
```
