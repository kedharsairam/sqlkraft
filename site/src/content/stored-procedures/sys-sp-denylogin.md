---
name: "sys.sp_denylogin"
title: "sp_denylogin"
category: "general"
description: "Prevents a Windows user or Windows group from connecting to an instance of SQL Server."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_denylogin [ @loginame = ]
      N
      'loginame'
      [ ; ]
---

## Description

Prevents a Windows user or Windows group from connecting to an instance of SQL Server.

## Syntax

```sql
sp_denylogin [ @loginame = ]
N
'loginame'
[ ; ]
```

## Remarks

Prevents a Windows user or Windows group from connecting to an instance of SQL Server.

The name of a Windows user or group.

, with no default.

(success) or

SQL permission to the server-level principal mapped to the

specified Windows user or Windows group. If the server principal doesn't exist, it's created. The

new principal is visible in the

sys.server_principals

catalog view.

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

## Examples

### Example 1

`sp_denylogin`

### Example 2

`sp_denylogin`

### Example 3

```sql
CORPORATE\GeorgeV
```

### Example 4

```sql
EXECUTE sp_denylogin
'CORPORATE\GeorgeV'
;
```
