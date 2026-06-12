---
name: "sys.sp_flush_commit_table_on_demand"
title: "sys.sp_flush_commit_table_on_demand"
category: "general"
description: "Specifies the number of rows you want to delete from syscommittab."
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
