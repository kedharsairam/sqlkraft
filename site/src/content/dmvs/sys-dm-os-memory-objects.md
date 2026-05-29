---
name: 'sys.dm_os_memory_objects'
title: 'sys.dm_os_memory_objects'
category: 'os'
description: 'Analytics Platform System (PDW) Returns memory objects that are currently allocated by SQL Server. You can use to analyze memory use and to identify possible memory leaks. Address of the memory object. Is not nullable. Address of the parent memory object. Is nullable. : SQL Server 2008 (10.0.x) through SQL Server Number of pages that are allocated by this object. Is not : SQL Server 2012 (11.x) an'
tags: ["os", "dmv"]
pubDate: 2026-05-29
syntax: |
  SELECT SUM (pages_in_bytes) as 'Bytes Used', type
  FROM sys.dm_os_memory_objects
  GROUP BY type
  ORDER BY 'Bytes Used' DESC;
  GO
---

## Description

Analytics Platform System (PDW) Returns memory objects that are currently allocated by SQL Server. You can use to analyze memory use and to identify possible memory leaks. Address of the memory object. Is not nullable. Address of the parent memory object. Is nullable. : SQL Server 2008 (10.0.x) through SQL Server Number of pages that are allocated by this object. Is not : SQL Server 2012 (11.x) and later.

## Syntax

```sql
SELECT SUM (pages_in_bytes) as 'Bytes Used', type
FROM sys.dm_os_memory_objects
GROUP BY type
ORDER BY 'Bytes Used' DESC;
GO
```
