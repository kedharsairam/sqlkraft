---
name: "To Check How much Memory each Database is Consu"
title: "To Check How much Memory each Database is Consu"
description: "diagnostic script for database operations."
category: "database"
tags: ["database","health-check","memory"]
pubDate: "2025-03-15"
---

```sql
SELECT (CASE WHEN ([is_modified] = 1) THEN 'Dirty' ELSE 'Clean' END) AS 'Page State',
(CASE WHEN ([database_id] = 32767) THEN 'Resource Database' ELSE DB_NAME (database_id) END) AS 'Database Name',
COUNT (*) AS 'Page Count'
FROM sys.dm_os_buffer_descriptors
GROUP BY [database_id], [is_modified]
ORDER BY [database_id], [is_modified];
GO
```
