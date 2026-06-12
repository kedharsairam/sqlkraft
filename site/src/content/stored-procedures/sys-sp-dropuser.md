---
name: "sys.sp_dropuser"
title: "sp_dropuser"
category: "general"
description: "Removes a database user from the current database. provides compatibility with earlier versions of SQL Server."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_dropuser [ @name_in_db = ]
      N
      'name_in_db'
      [ ; ]
---

## Description

Removes a database user from the current database. provides compatibility with earlier versions of SQL Server.

## Syntax

```sql
sp_dropuser [ @name_in_db = ]
N
'name_in_db'
[ ; ]
```

## Remarks

Removes a database user from the current database.

provides compatibility with

earlier versions of SQL Server.

The name of the user to remove.

@name_in_db

, with no default.

@name_in_db

must exist in the current database. When specifying a Windows account, use the name by

which the database knows that account.

(success) or

to remove the user from the current database.

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

## Examples

### Example 1

`sp_helpuser`

### Example 2

`sp_dropuser`

### Example 3

`INFORMATION_SCHEMA`

### Example 4

`master`

### Example 5

`tempdb`

### Example 6

```sql
EXECUTE sp_dropuser 'guest'
```

### Example 7

`CONNECT`

### Example 8

`sp_dropuser`

### Example 9

```sql
ALTER ANY USER
```

### Example 10

`Albert`

_(. and 1 more examples)_
