---
name: "sys.dm_os_memory_clerks"
title: "sys.dm_os_memory_clerks"
category: "os"
description: "Returns the set of all memory clerks that are currently active in the instance of SQL Server. Specifies the unique memory address of the memory clerk. This is the primary key column. Is not nullable. Specifies the type of memory clerk. Every clerk has a specific type, such as CLR Clerks MEMORYCLERK_SQLCLR. Is not nullable. Specifies the internally assigned name of t"
tags: ["os", "dmv"]
pubDate: 2026-05-29
syntax: |
  SELECT h.type, SUM(mc.pages_kb) AS committed_memory
  FROM sys.dm_os_memory_clerks AS mc
  INNER JOIN sys.dm_os_hosts AS h
  ON mc.memory_clerk_address = h.default_memory_clerk_address
  GROUP BY h.type;
---

## Description

Analytics Platform System (PDW) Returns the set of all memory clerks that are currently active in the instance of SQL Server. Specifies the unique memory address of the memory clerk. This is the primary key column. Is not nullable. Specifies the type of memory clerk. Every clerk has a specific type, such as CLR Clerks MEMORYCLERK_SQLCLR. Is not nullable. Specifies the internally assigned name of this memory

## Syntax

```sql
SELECT h.type, SUM(mc.pages_kb) AS committed_memory
FROM sys.dm_os_memory_clerks AS mc
INNER JOIN sys.dm_os_hosts AS h
ON mc.memory_clerk_address = h.default_memory_clerk_address
GROUP BY h.type;
```
