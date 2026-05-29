---
name: 'sys.sp_dbmmonitorresults'
title: 'sp_dbmmonitorresults'
category: 'general'
description: 'Returns status rows for a monitored database from the status table in which database mirroring monitoring history is stored, and allows you to choose whether the procedure obtains the latest status beforehand. Transact-SQL syntax conventions Specifies the database for which to return mirroring status. Specifies the quantity of rows returned. , and can be one of these values.'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dbmmonitorresults
  [ @database_name = ]
  N
  'database_name'
  [ , [ @mode = ] mode ]
  [ , [ @update_table = ] update_table ]
  [ ; ]
---

## Description

Returns status rows for a monitored database from the status table in which database mirroring monitoring history is stored, and allows you to choose whether the procedure obtains the latest status beforehand. Transact-SQL syntax conventions Specifies the database for which to return mirroring status. Specifies the quantity of rows returned. , and can be one of these values.

## Syntax

```sql
sp_dbmmonitorresults
[ @database_name = ]
N
'database_name'
[ , [ @mode = ] mode ]
[ , [ @update_table = ] update_table ]
[ ; ]
```

## Examples

### Example 1

```sql
local_time
```

### Example 2

```sql
sp_dbmmonitorresults
```

### Example 3

```sql
msdb
```

### Example 4

```sql
msdb
```

### Example 5

```sql
sp_dbmmonitorupdate
```

### Example 6

```sql
msdb
```

### Example 7

```sql
USE
msdb;
EXECUTE
sp_dbmmonitorresults AdventureWorks2022, 2, 0;
```
