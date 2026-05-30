---
name: "sys.sp_resetstatus"
title: "sp_resetstatus"
category: "general"
description: "Resets the status of a suspect database. Transact-SQL syntax conventions The name of the database to reset. , with no default. turns off the suspect flag on a database. This procedure updates the mode and status columns of the named database in . The SQL Server error log should be consulted and all problems resolved before running this procedure. Stop and restart the instance of SQL Server after y"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_resetstatus [ @
  DBN
  ame = ]
  N
  'DBName'
  [ ; ]
---

## Description

Resets the status of a suspect database. Transact-SQL syntax conventions The name of the database to reset. , with no default. turns off the suspect flag on a database. This procedure updates the mode and status columns of the named database in . The SQL Server error log should be consulted and all problems resolved before running this procedure. Stop and restart the instance of SQL Server after you execute This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_resetstatus [ @
DBN ame = ]
N
'DBName'
[ ; ]
```

## Remarks

Applies to:

Resets the status of a suspect database.

Transact-SQL syntax conventions

The name of the database to reset.

, with no default.

(success) or

turns off the suspect flag on a database. This procedure updates the mode and

status columns of the named database in

. The SQL Server error log should be

consulted and all problems resolved before running this procedure. Stop and restart the

instance of SQL Server after you execute

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

## Examples

### Example 1

`AdventureWorks2022`

### Example 2

```sql
EXECUTE sp_resetstatus
'AdventureWorks2022'
;
```
