---
name: "sys.sp_grantdbaccess"
title: "sp_grantdbaccess"
category: "general"
description: "Adds a database user to the current database."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_grantdbaccess
      [ @loginame = ]
      N
      'loginame'
      [ , [ @name_in_db = ]
      N
      'name_in_db'
      OUTPUT
      ]
      [ ; ]
---

## Description

Adds a database user to the current database.

## Syntax

```sql
sp_grantdbaccess
[ @loginame = ]
N
'loginame'
[ , [ @name_in_db = ]
N
'name_in_db'
OUTPUT
]
[ ; ]
```
