---
name: "sys.sp_execute"
title: "sp_execute"
category: "general"
description: "Analytics Platform System (PDW) Executes a prepared Transact-SQL statement using a specified handle and optional parameter in a tabular data stream (TDS) packet. Transact-SQL syntax conventions Signifies the use of extra parameters."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_execute handle
  OUTPUT
  [ , bound_param ] [ , ...n ]
  [ ; ]
---

## Description

Analytics Platform System (PDW) Executes a prepared Transact-SQL statement using a specified handle and optional parameter in a tabular data stream (TDS) packet. Transact-SQL syntax conventions Signifies the use of extra parameters. The parameter is any data type, to signify more parameters for the procedure, and can't be Arguments for extended stored procedures must be entered in the specific order as

## Syntax

```sql
sp_execute handle
OUTPUT
[ , bound_param ] [ , ...n ]
[ ; ]
```
