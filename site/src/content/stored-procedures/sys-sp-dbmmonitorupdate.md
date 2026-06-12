---
name: "sys.sp_dbmmonitorupdate"
title: "sp_dbmmonitorupdate"
category: "general"
description: "Updates the database mirroring monitor status table by inserting a new table row for each mirrored database, and truncates rows older than the current retention period. The default retention period is seven days (168 hours). When evaluates the performance metrics."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_dbmmonitorupdate [ [ @database_name = ]
      N
      'database_name'
      ]
      [ ; ]
---

## Description

Updates the database mirroring monitor status table by inserting a new table row for each mirrored database, and truncates rows older than the current retention period. The default retention period is seven days (168 hours). When evaluates the performance metrics.

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

`sp_dbmmonitorupdate`

### Example 2

`msdb`

### Example 3

`NULL`

### Example 4

`NULL`

### Example 5

`sp_dbmmonitorupdate`

### Example 6

`msdb`

### Example 7

`sp_dbmmonitorupdate`

### Example 8

`AdventureWorks2022`

### Example 9

```sql
USE msdb;
EXECUTE sp_dbmmonitorupdate AdventureWorks2022;
```
