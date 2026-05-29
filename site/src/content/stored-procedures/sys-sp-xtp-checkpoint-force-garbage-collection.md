---
name: 'sys.sp_xtp_checkpoint_force_garbage_collection'
title: 'sys.sp_xtp_checkpoint_force_garbage_collection'
category: 'general'
description: 'Marks source files used in the merge operation with the log sequence number (LSN) after which they aren''t needed and can be garbage collected. Also, moves the files whose associated LSN is lower than the log truncation point to FILESTREAM garbage collection. , which causes the in-memory engine to release memory related to deleted rows of in-memory data that are eligible for garbage collection, whi'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: 'sys.sp_xtp_checkpoint_force_garbage_collection'
---

## Description

Marks source files used in the merge operation with the log sequence number (LSN) after which they aren't needed and can be garbage collected. Also, moves the files whose associated LSN is lower than the log truncation point to FILESTREAM garbage collection. , which causes the in-memory engine to release memory related to deleted rows of in-memory data that are eligible for garbage collection, which

## Syntax

```sql
sys.sp_xtp_checkpoint_force_garbage_collection
```
