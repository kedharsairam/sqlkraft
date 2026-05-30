---
name: "sys.sp_fulltext_pendingchanges"
title: "sp_fulltext_pendingchanges"
category: "general"
description: "Returns unprocessed changes, such as pending inserts, updates, and deletes, for a specified table that is using change tracking. Transact-SQL syntax conventions ID of the table. If the table isn't full-text indexed, or change tracking isn't enabled on the table, The full-text key value from the specified table. Arguments for extended stored procedures must be entered in the specific order as secti"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_fulltext_pendingchanges table_id
  [ ; ]
---

## Description

Returns unprocessed changes, such as pending inserts, updates, and deletes, for a specified table that is using change tracking. Transact-SQL syntax conventions ID of the table. If the table isn't full-text indexed, or change tracking isn't enabled on the table, The full-text key value from the specified table. Arguments for extended stored procedures must be entered in the specific order as section. If the parameters are entered out of order, an error

## Syntax

```sql
sp_fulltext_pendingchanges table_id
[ ; ]
```
