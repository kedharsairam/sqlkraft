---
name: "sys.dm_exec_compute_nodes"
title: "sys.dm_exec_compute_nodes"
category: "execution"
description: "2016 (13.x) and later versions Holds information about nodes used with PolyBase data management. It lists one row per Use this DMV to see the list of all nodes in the scale-out cluster with their role, name and IP Unique numeric id associated with PolyBase troubleshooting with dynamic management views Dynamic Management Views and Functions (Transact-SQL) Database Related Dynamic Managem"
tags: ["execution","dmv"]
pubDate: "2026-05-29"
syntax: |
  EXECUTE
      sys.dm_exec_compute_nodes;
---

## Description

2016 (13.x) and later versions Holds information about nodes used with PolyBase data management. It lists one row per Use this DMV to see the list of all nodes in the scale-out cluster with their role, name and IP Unique numeric id associated with PolyBase troubleshooting with dynamic management views Dynamic Management Views and Functions (Transact-SQL) Database Related Dynamic Management Views (Transact-SQL)

## Syntax

```sql
EXECUTE sys.dm_exec_compute_nodes;
```

## Examples

### Example 1

```sql
EXECUTE sys.dm_exec_compute_nodes;
```

### Example 2

```sql
EXECUTE sp_polybase_leave_group;
```
