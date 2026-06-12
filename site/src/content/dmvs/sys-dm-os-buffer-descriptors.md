---
name: "sys.dm_os_buffer_descriptors"
title: "sys.dm_os_buffer_descriptors"
category: "os"
description: "Returns information about all the data pages that are currently in the SQL Server buffer pool. The output of this view can be used to determine the distribution of database pages in the buffer pool according to database, object, or type."
tags: ["os", "dmv"]
pubDate: 2026-05-29
syntax: |
  SELECT COUNT(*)AS cached_pages_count
  ,CASE database_id
  WHEN 32767 THEN 'ResourceDb'
  ELSE db_name(database_id)
  END AS database_name
  FROM sys.dm_os_buffer_descriptors
  GROUP BY DB_NAME(database_id) ,database_id
  ORDER BY cached_pages_count DESC;
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns information about all the data pages that are currently in the SQL Server buffer pool. The output of this view can be used to determine the distribution of database pages in the buffer pool according to database, object, or type. In SQL Server, this dynamic management view also returns information about the data pages in the buffer pool extension file.

## Syntax

```sql
SELECT COUNT(*)AS cached_pages_count
,CASE database_id
WHEN 32767 THEN 'ResourceDb'
ELSE db_name(database_id)
END AS database_name
FROM sys.dm_os_buffer_descriptors
GROUP BY DB_NAME(database_id) ,database_id
ORDER BY cached_pages_count DESC;
```
