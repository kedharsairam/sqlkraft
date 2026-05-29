---
name: 'sys.sp_cursorexecute'
title: 'sp_cursorexecute'
category: 'general'
description: 'Creates and populates a cursor based upon the execution plan created by Transact-SQL syntax conventions The Database Engine-generated cursor identifier. is a required parameter that must be supplied on all subsequent procedures that act upon the cursor, such as Arguments for extended stored procedures must be entered in the specific order as section. If the parameters are entered out of order, an '
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_cursorexecute prepared_handle , cursor
  [ , scrollopt [
  OUTPUT
  ]
  [ , ccopt [
  OUTPUT
  ]
  [ , rowcount
  OUTPUT
  [ , bound param ] [ , ...n ] ] ] ]
  [ ; ]
---

## Description

Creates and populates a cursor based upon the execution plan created by Transact-SQL syntax conventions The Database Engine-generated cursor identifier. is a required parameter that must be supplied on all subsequent procedures that act upon the cursor, such as Arguments for extended stored procedures must be entered in the specific order as section. If the parameters are entered out of order, an error

## Syntax

```sql
sp_cursorexecute prepared_handle , cursor
[ , scrollopt [
OUTPUT
]
[ , ccopt [
OUTPUT
]
[ , rowcount
OUTPUT
[ , bound param ] [ , ...n ] ] ] ]
[ ; ]
```
