---
name: "sys.sp_helpntgroup"
title: "sp_helpntgroup"
category: "general"
description: "Reports information about Windows groups with accounts in the current database. Transact-SQL syntax conventions The name of the Windows group. be a valid Windows group with access to the current database. If Windows groups with access to the current database are included in the output."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpntgroup [ [ @ntname = ]
  N
  'ntname'
  ]
  [ ; ]
---

## Description

Reports information about Windows groups with accounts in the current database. Transact-SQL syntax conventions The name of the Windows group. be a valid Windows group with access to the current database. If Windows groups with access to the current database are included in the output.

## Syntax

```sql
sp_helpntgroup [ [ @ntname = ]
N
'ntname'
]
[ ; ]
```
