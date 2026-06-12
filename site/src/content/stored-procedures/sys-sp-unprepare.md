---
name: "sys.sp_unprepare"
title: "sp_unprepare"
category: "general"
description: "Discards the execution plan created by the in a tabular data stream (TDS) packet. The following example prepares, executes, and unprepares a basic statement. Arguments for extended stored procedures must be entered in the specific order as section."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_unprepare handle
      [ ; ]
---

## Description

Analytics Platform System (PDW) Discards the execution plan created by the in a tabular data stream (TDS) packet. The following example prepares, executes, and unprepares a basic statement. Arguments for extended stored procedures must be entered in the specific order as section.

## Syntax

```sql
sp_unprepare handle
[ ; ]
```

## Examples

### Example 1

`sp_prepare`

### Example 2

`sp_unprepare`

### Example 3

```sql
ID = 15
```

### Example 4

`sp_prepare`

### Example 5

```sql
sp_unprepare handle
[ ; ]
```

### Example 6

```sql
DECLARE
@P1
AS
INT
;
EXECUTE sp_prepare
@P1
OUTPUT
, N
'@P1 NVARCHAR(128), @P2 NVARCHAR(100)'
,
N
'SELECT database_id, name FROM sys.databases WHERE name = @P1 AND state_desc
= @P2'
;
```

### Example 7

```sql
EXECUTE sp_execute @P1, N
'tempdb'
, N
'ONLINE'
;
EXECUTE sp_unprepare @P1;
```
