---
name: "sys.sp_helpuser"
title: "sp_helpuser"
category: "general"
description: "Reports information about database-level principals in the current database. Transact-SQL syntax conventions The name of database user or database role in the current database. must exist in the current database. If returns information about all database principals. The following table shows the result set when no user account, SQL Server, or Windows user is doesn't return information about secura"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_helpuser [ [ @name_in_db = ]
  N
  'name_in_db'
  ]
  [ ; ]
---

## Description

Reports information about database-level principals in the current database. Transact-SQL syntax conventions The name of database user or database role in the current database. must exist in the current database. If returns information about all database principals. The following table shows the result set when no user account, SQL Server, or Windows user is doesn't return information about securables that were introduced in SQL

## Syntax

```sql
sp_helpuser [ [ @name_in_db = ]
N
'name_in_db'
]
[ ; ]
```

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

_(... and 1 more examples)_
