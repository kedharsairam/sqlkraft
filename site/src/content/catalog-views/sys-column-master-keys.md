---
name: "sys.column_master_keys"
title: "sys.column_master_keys"
category: "compatibility"
description: "2016 (13.x) and later Returns a row for each database master key added by using the statement. Each row represents a single column master key (CMK). Date the column master key was created. Date the column master key was last modified."
tags: ["compatibility","catalog-view"]
pubDate: 2026-05-29
syntax: "'CurrentUser/Personal/'<thumbprint>"
---

## Description

2016 (13.x) and later Returns a row for each database master key added by using the statement. Each row represents a single column master key (CMK). Date the column master key was created. Date the column master key was last modified.

## Syntax

```sql
'CurrentUser/Personal/'<thumbprint>
```
