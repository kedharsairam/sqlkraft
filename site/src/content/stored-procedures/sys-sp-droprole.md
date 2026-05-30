---
name: "sys.sp_droprole"
title: "sp_droprole"
category: "general"
description: "Removes a database role from the current database. Transact-SQL syntax conventions The name of the database role to remove from the current database. with no default. must already exist in the current database. Only database roles can be removed by using In SQL Server 2005 (9.x), was replaced by the DROP ROLE statement. is included only for compatibility with earlier versions of SQL Server and mig"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_droprole [ @rolename = ]
  N
  'rolename'
  [ ; ]
---

## Description

Removes a database role from the current database. Transact-SQL syntax conventions The name of the database role to remove from the current database. with no default. must already exist in the current database. Only database roles can be removed by using In SQL Server 2005 (9.x), was replaced by the DROP ROLE statement. is included only for compatibility with earlier versions of SQL Server and might not be supported in a future release.

## Syntax

```sql
sp_droprole [ @rolename = ]
N
'rolename'
[ ; ]
```

## Remarks

Applies to:

Removes a database role from the current database.

Transact-SQL syntax conventions

The name of the database role to remove from the current database.

with no default.

must already exist in the current database.

(success) or

Only database roles can be removed by using

In SQL Server 2005 (9.x),

was replaced by the DROP ROLE statement.

is included only for compatibility with earlier versions of SQL Server and

might not be supported in a future release.

## Examples

### Example 1

`sp_droprolemember`

### Example 2

`sp_droprole`

### Example 3

```sql
ALTER
AUTHORIZATION
```

### Example 4

`sp_droprole`

### Example 5

`CONTROL`

### Example 6

`Sales`

### Example 7

```sql
EXECUTE sp_droprole
'Sales'
;
GO
```
