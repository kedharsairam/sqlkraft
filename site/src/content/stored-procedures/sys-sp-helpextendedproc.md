---
name: "sys.sp_helpextendedproc"
title: "sp_helpextendedproc"
category: "general"
description: "Reports the currently defined extended stored procedures and the name of the dynamic-link library (DLL) to which the procedure (function) belongs."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpextendedproc [ [ @funcname = ]
  N
  'funcname'
  ]
  [ ; ]
---

## Description

Reports the currently defined extended stored procedures and the name of the dynamic-link library (DLL) to which the procedure (function) belongs.

## Syntax

```sql
sp_helpextendedproc [ [ @funcname = ]
N
'funcname'
]
[ ; ]
```
