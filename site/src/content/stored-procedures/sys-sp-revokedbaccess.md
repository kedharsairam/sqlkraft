---
name: "sys.sp_revokedbaccess"
title: "sp_revokedbaccess"
category: "general"
description: "Removes a database user from the current database. Transact-SQL syntax conventions The name of the database user to be removed. , with no default."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_revokedbaccess [ @name_in_db = ]
  N
  'name_in_db'
  [ ; ]
---

## Description

Removes a database user from the current database. Transact-SQL syntax conventions The name of the database user to be removed. , with no default. can be the name of a server login, a Windows login, or a Windows group, and must exist in the current database. When you specify a Windows login or Windows group, specify the name by which it's known in the database. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_revokedbaccess [ @name_in_db = ]
N
'name_in_db'
[ ; ]
```

## Remarks

Applies to:

Removes a database user from the current database.

Transact-SQL syntax conventions

The name of the database user to be removed.

@name_in_db

, with no default.

@name_in_db

can be the name of a server login, a Windows login, or a Windows group, and

must exist in the current database. When you specify a Windows login or Windows group,

specify the name by which it's known in the database.

(success) or

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

## Examples

### Example 1

`sp_revokedbaccess`

### Example 2

`sp_revokedbaccess`

### Example 3

```sql
Edmonds\LolanSo
```

### Example 4

```sql
EXECUTE sp_revokedbaccess
'Edmonds\LolanSo'
;
GO
```
