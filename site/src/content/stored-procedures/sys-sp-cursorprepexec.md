---
name: 'sys.sp_cursorprepexec'
title: 'sp_cursorprepexec'
category: 'general'
description: 'Analytics Platform System (PDW) Compiles a plan for the submitted cursor statement or batch, then creates and populates the This procedure is invoked by specifying in a tabular data stream (TDS) packet. Transact-SQL syntax conventions parameter is a required parameter that must be supplied on all subsequent procedures that act upon this cursor, for example, Arguments for extended stored procedures'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_cursorprepexec prepared handle
  OUTPUT
  , cursor
  OUTPUT
  , params , statement ,
  options
  [ , scrollopt [ , ccopt [ , rowcount ] ] ]
  [ ,
  '@parameter_name [ , ...n ]'
  ]
---

## Description

Analytics Platform System (PDW) Compiles a plan for the submitted cursor statement or batch, then creates and populates the This procedure is invoked by specifying in a tabular data stream (TDS) packet. Transact-SQL syntax conventions parameter is a required parameter that must be supplied on all subsequent procedures that act upon this cursor, for example, Arguments for extended stored procedures must be entered in the specific order as

## Syntax

```sql
sp_cursorprepexec prepared handle
OUTPUT
, cursor
OUTPUT
, params , statement ,
options
[ , scrollopt [ , ccopt [ , rowcount ] ] ]
[ ,
'@parameter_name [ , ...n ]'
]
```

## Examples

### Example 1

```sql
sp_cursorprepexec
```

### Example 2

```sql
Person
```

### Example 3

```sql
AdventureWorks2025
```

### Example 4

```sql
USE
AdventureWorks2022;
GO
DECLARE
@prep_handle
INT
,
@
cursor
INT
,
@scrollopt
INT
= 4104,
@ccopt
INT
= 8193,
@rowcnt
INT
;
EXECUTE
sp_cursorprepexec
@prep_handle
OUTPUT
,
@
cursor
OUTPUT
,
N
'@fName nvarchar(100)'
,
N
'SELECT FirstName, LastName FROM Person.Person WHERE FirstName = @fName'
,
@scrollopt,
@ccopt,
@rowcnt
OUTPUT
,
'Kirby'
;
EXECUTE
sp_cursorfetch @
cursor
;
```
