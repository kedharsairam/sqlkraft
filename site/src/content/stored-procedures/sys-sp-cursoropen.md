---
name: "sys.sp_cursoropen"
title: "sp_cursoropen"
category: "general"
description: "defines the SQL statement associated with the cursor and cursor options, and then populates the cursor. is equivalent to the combination of the Transact-SQL statements . This procedure is invoked by in a tabular data stream (TDS) packet. Transact-SQL syntax conventions A SQL Server-generated cursor identifier. value that must be supplied on all subsequent procedures involving the cursor, such as a"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_cursoropen cursor
  OUTPUT
  , stmt
  [ , scrollopt [
  OUTPUT
  ]
  [ , ccopt [
  OUTPUT
  ]
  [ , rowcount
  OUTPUT
  [ , boundparam ] [ , ...n ] ] ] ]
  [ ; ]
---

## Description

defines the SQL statement associated with the cursor and cursor options, and then populates the cursor. is equivalent to the combination of the Transact-SQL statements . This procedure is invoked by in a tabular data stream (TDS) packet. Transact-SQL syntax conventions A SQL Server-generated cursor identifier. value that must be supplied on all subsequent procedures involving the cursor, such as allows multiple cursors to be active on a single database connection.

## Syntax

```sql
sp_cursoropen cursor
OUTPUT
, stmt
[ , scrollopt [
OUTPUT
]
[ , ccopt [
OUTPUT
]
[ , rowcount
OUTPUT
[ , boundparam ] [ , ...n ] ] ] ]
[ ; ]
```
