---
name: "sys.sp_srvrolepermission"
title: "sp_srvrolepermission"
category: "general"
description: "Displays the permissions of a fixed server role. Transact-SQL syntax conventions The name of the fixed server role for which permissions are returned. If no role is specified, the permissions for all fixed server roles can have one of the following values. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applicat"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_srvrolepermission [ [ @srvrolename = ]
  N
  'srvrolename'
  ]
  [ ; ]
---

## Description

Displays the permissions of a fixed server role. Transact-SQL syntax conventions The name of the fixed server role for which permissions are returned. . If no role is specified, the permissions for all fixed server roles can have one of the following values. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_srvrolepermission [ [ @srvrolename = ]
N
'srvrolename'
]
[ ; ]
```
