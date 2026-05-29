---
name: "sys.sp_dbmmonitorupdate"
title: "sp_dbmmonitorupdate"
category: "general"
description: "Updates the database mirroring monitor status table by inserting a new table row for each mirrored database, and truncates rows older than the current retention period. The default retention period is seven days (168 hours). When evaluates the performance metrics. Transact-SQL syntax conventions The name of the database for which to update mirroring status. isn't specified, the procedure updates t"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_dbmmonitorupdate [ [ @database_name = ]
  N
  'database_name'
  ]
  [ ; ]
---

## Description

Updates the database mirroring monitor status table by inserting a new table row for each mirrored database, and truncates rows older than the current retention period. The default retention period is seven days (168 hours). When evaluates the performance metrics. Transact-SQL syntax conventions The name of the database for which to update mirroring status. isn't specified, the procedure updates the status table

## Syntax

```sql
sp_dbmmonitorupdate [ [ @database_name = ]
N
'database_name'
]
[ ; ]
```

## Examples

### Example 1

```sql
sp_dbmmonitorupdate
```

### Example 2

```sql
msdb
```

### Example 3

```sql
NULL
```

### Example 4

```sql
NULL
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
sp_dbmmonitorupdate
```

### Example 8

```sql
AdventureWorks2022
```

### Example 9

```sql
USE
msdb;
EXECUTE
sp_dbmmonitorupdate AdventureWorks2022;
```
