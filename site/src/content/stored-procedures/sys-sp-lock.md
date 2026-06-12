---
name: "sys.sp_lock"
title: "sp_lock"
category: "general"
description: "Reports information about locks. A Database Engine session ID number from information about the session. If isn't specified, information about all locks is displayed. Another Database Engine session ID number from and about which the user also wants information. This feature will be removed in a future version of SQL Server. Avoid using this feature in new developme"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_lock
              [ [ @spid1 = ] spid1 ]
              [ , [ @spid2 = ] spid2 ]
              [ ; ]
---

## Description

Reports information about locks. A Database Engine session ID number from information about the session. If isn't specified, information about all locks is displayed. Another Database Engine session ID number from and about which the user also wants information. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. To

## Syntax

```sql
sp_lock
[ [ @spid1 = ] spid1 ]
[ , [ @spid2 = ] spid2 ]
[ ; ]
```
