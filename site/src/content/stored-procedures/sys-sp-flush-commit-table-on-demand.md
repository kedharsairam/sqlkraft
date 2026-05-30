---
name: "sys.sp_flush_commit_table_on_demand"
title: "sys.sp_flush_commit_table_on_demand"
category: "general"
description: "Transact-SQL syntax conventions Specifies the number of rows you want to delete from syscommittab. is an OUTPUT parameter of type is an OUTPUT parameter of type is an OUTPUT parameter of type"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_flush_commit_table_on_demand
  [ @numrows = ] numrows
  , [ @deleted_rows = ] deleted_rows
  OUTPUT
  , [ @date_cleanedup = ] date_cleanedup
  OUTPUT
  , [ @cleanup_ts = ] cleanup_ts
  OUTPUT
  [ ; ]
---

## Description

Transact-SQL syntax conventions Specifies the number of rows you want to delete from syscommittab. is an OUTPUT parameter of type is an OUTPUT parameter of type is an OUTPUT parameter of type

## Syntax

```sql
sp_flush_commit_table_on_demand
[ @numrows = ] numrows
, [ @deleted_rows = ] deleted_rows
OUTPUT
, [ @date_cleanedup = ] date_cleanedup
OUTPUT
, [ @cleanup_ts = ] cleanup_ts
OUTPUT
[ ; ]
```
