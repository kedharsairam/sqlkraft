---
name: 'sys.sp_helpdevice'
title: 'sp_helpdevice'
category: 'general'
description: 'Reports information about SQL Server backup devices. Transact-SQL syntax conventions The name of the backup device for which information is reported. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpdevice [ [ @devname = ]
  N
  'devname'
  ]
  [ ; ]
---

## Description

Reports information about SQL Server backup devices. Transact-SQL syntax conventions The name of the backup device for which information is reported. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_helpdevice [ [ @devname = ]
N
'devname'
]
[ ; ]
```
