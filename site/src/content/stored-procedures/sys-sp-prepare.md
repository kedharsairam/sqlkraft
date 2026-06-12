---
name: "sys.sp_prepare"
title: "sp_prepare (Transact-SQL)"
category: "general"
description: "Prepares a parameterized Transact-SQL statement and returns a statement in a tabular data stream (TDS) packet. is a required parameter with an Identifies parameterized statements. is a required OUTPUT parameter that calls for an definition of variables is substituted for parameter markers in the statement. Input a value if the stateme"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_prepare
              handle
              OUTPUT
              , params
              , stmt
              , options
              [ ; ]
---

## Description

Analytics Platform System (PDW) Prepares a parameterized Transact-SQL statement and returns a statement in a tabular data stream (TDS) packet. is a required parameter with an Identifies parameterized statements. is a required OUTPUT parameter that calls for an definition of variables is substituted for parameter markers in the statement. Input a value if the statement isn't parameterized.

## Syntax

```sql
sp_prepare handle
OUTPUT
, params
, stmt
, options
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
