---
name: 'sys.sp_dropuser'
title: 'sp_dropuser'
category: 'general'
description: 'Removes a database user from the current database. provides compatibility with earlier versions of SQL Server. Transact-SQL syntax conventions The name of the user to remove. , with no default. must exist in the current database. When specifying a Windows account, use the name by which the database knows that account. to remove the user from the current database. This feature will be removed in a '
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dropuser [ @name_in_db = ]
  N
  'name_in_db'
  [ ; ]
---

## Description

Removes a database user from the current database. provides compatibility with earlier versions of SQL Server. Transact-SQL syntax conventions The name of the user to remove. , with no default. must exist in the current database. When specifying a Windows account, use the name by which the database knows that account. to remove the user from the current database. This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature.

## Syntax

```sql
sp_dropuser [ @name_in_db = ]
N
'name_in_db'
[ ; ]
```

## Remarks

Applies to:

Removes a database user from the current database.

provides compatibility with

earlier versions of SQL Server.

Transact-SQL syntax conventions

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

```sql
sp_helpuser
```

### Example 2

```sql
sp_dropuser
```

### Example 3

```sql
INFORMATION_SCHEMA
```

### Example 4

```sql
master
```

### Example 5

```sql
tempdb
```

### Example 6

```sql
EXECUTE
sp_dropuser 'guest'
```

### Example 7

```sql
CONNECT
```

### Example 8

```sql
sp_dropuser
```

### Example 9

```sql
ALTER ANY USER
```

### Example 10

```sql
Albert
```


*(... and 1 more examples)*
