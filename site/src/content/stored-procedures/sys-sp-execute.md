---
name: "sys.sp_execute"
title: "sp_execute"
category: "general"
description: "Executes a prepared Transact-SQL statement using a specified handle and optional parameter in a tabular data stream (TDS) packet. Signifies the use of extra parameters."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_execute handle
  OUTPUT
  [ , bound_param ] [ , ...n ]
  [ ; ]
---

## Description

Analytics Platform System (PDW) Executes a prepared Transact-SQL statement using a specified handle and optional parameter in a tabular data stream (TDS) packet. Signifies the use of extra parameters.

## Syntax

```sql
sp_execute handle
OUTPUT
[ , bound_param ] [ ,.n ]
[ ; ]
```
