---
name: "sys.sp_kill_filestream_non_transacted_handles"
title: "sp_kill_filestream_non_transacted_handles"
category: "general"
description: "Closes nontransactional file handles to FileTable data. Transact-SQL syntax conventions The name of the table in which to close nontransactional handles. to close all open nontransactional handles for the to close all open nontransactional handles for all FileTables in the current database. The optional ID of the individual handle to be closed. You can get the sys.dm_filestream_non_transacted_hand"
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

Closes nontransactional file handles to FileTable data. Transact-SQL syntax conventions The name of the table in which to close nontransactional handles. to close all open nontransactional handles for the to close all open nontransactional handles for all FileTables in the current database. The optional ID of the individual handle to be closed. You can get the sys.dm_filestream_non_transacted_handles

## Syntax

```sql
sp_kill_filestream_non_transacted_handles [
[ @table_name = ]
'table_name'
, [ [ @handle_id = ] handle_id ]
]
```
