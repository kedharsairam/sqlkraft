---
name: "sys.sp_droplogin"
title: "sp_droplogin"
category: "general"
description: "Removes a SQL Server login, which prevents access to an instance of SQL Server under that The login to be removed. , with no default. exist in SQL Server. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_droplogin [ @loginame = ]
              N
              'loginame'
              [ ; ]
---

## Description

Removes a SQL Server login, which prevents access to an instance of SQL Server under that The login to be removed. , with no default. exist in SQL Server. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_droplogin [ @loginame = ]
N
'loginame'
[ ; ]
```

## Remarks

Removes a SQL Server login, which prevents access to an instance of SQL Server under that

login name.

The login to be removed.

, with no default.

must already

exist in SQL Server.

(success) or

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

## Examples

### Example 1

`sp_droplogin`

### Example 2

```sql
ALTER ANY LOGIN
```

### Example 3

```sql
DROP LOGIN
```

### Example 4

`Victoria`

### Example 5

```sql
DROP
LOGIN Victoria;
GO
```
