---
name: "sys.sp_prepexec"
title: "sp_prepexec"
category: "general"
description: "Prepares and executes a parameterized Transact-SQL statement. Transact-SQL syntax conventions is a required parameter with an Identifies parameterized statements. The definition of variables is substituted for parameter markers in the statement. is a required parameter that calls for an value if the statement isn't parameterized."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_prepexec handle
  OUTPUT
  , params , stmt
  [ , bound param ] [ , ...n ]
  [ ; ]
---

## Description

Prepares and executes a parameterized Transact-SQL statement. Transact-SQL syntax conventions is a required parameter with an Identifies parameterized statements. The definition of variables is substituted for parameter markers in the statement. is a required parameter that calls for an value if the statement isn't parameterized. Arguments for extended stored procedures must be entered in the specific order as

## Syntax

```sql
sp_prepexec handle
OUTPUT
, params , stmt
[ , bound param ] [ , ...n ]
[ ; ]
```

## Examples

### Example 1

```sql
DECLARE
@
Out
AS
INT
;
EXECUTE sp_prepexec
@
Out
OUTPUT
, N
'@P1 nvarchar(128), @P2 nvarchar(100)'
,
N
'SELECT database_id, name
FROM sys.databases
WHERE name=@P1 AND state_desc = @P2'
,
@P1 =
'tempdb'
,
@P2 =
'ONLINE'
;
EXECUTE sp_unprepare @
Out
;
```
