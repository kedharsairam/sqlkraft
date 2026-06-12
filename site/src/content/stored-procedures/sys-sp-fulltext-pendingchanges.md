---
name: "sys.sp_fulltext_pendingchanges"
title: "sp_fulltext_pendingchanges"
category: "general"
description: "Returns unprocessed changes, such as pending inserts, updates, and deletes, for a specified table that is using change tracking."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_fulltext_pendingchanges table_id
  [ ; ]
---

## Description

Returns unprocessed changes, such as pending inserts, updates, and deletes, for a specified table that is using change tracking.

## Syntax

```sql
sp_fulltext_pendingchanges table_id
[ ; ]
```
