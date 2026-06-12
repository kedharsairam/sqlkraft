---
name: "sys.sp_kill_filestream_non_transacted_handles"
title: "sp_kill_filestream_non_transacted_handles"
category: "general"
description: "Closes nontransactional file handles to FileTable data."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_kill_filestream_non_transacted_handles [
  [ @table_name = ]
  'table_name'
  , [ [ @handle_id = ] handle_id ]
  ]
---

## Description

Closes nontransactional file handles to FileTable data.

## Syntax

```sql
sp_kill_filestream_non_transacted_handles [
[ @table_name = ]
'table_name'
, [ [ @handle_id = ] handle_id ]
]
```
