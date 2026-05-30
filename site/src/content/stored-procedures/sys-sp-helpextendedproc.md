---
name: "sys.sp_helpextendedproc"
title: "sp_helpextendedproc"
category: "general"
description: "Reports the currently defined extended stored procedures and the name of the dynamic-link library (DLL) to which the procedure (function) belongs. Transact-SQL syntax conventions The name of the extended stored procedure for which information is reported. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify application"
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

Reports the currently defined extended stored procedures and the name of the dynamic-link library (DLL) to which the procedure (function) belongs. Transact-SQL syntax conventions The name of the extended stored procedure for which information is reported. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_helpextendedproc [ [ @funcname = ]
N
'funcname'
]
[ ; ]
```
