---
name: "To Generate Script to Attach and Detach all Dat"
title: "To Generate Script to Attach and Detach all Dat"
description: "Generate the Attach and Detach Script"
category: "database"
tags: ["database"]
pubDate: 2025-03-15
---

```sql
--Generate the Attach and Detach Script
WITH CTE AS (
 SELECT dbid,
 DB_NAME(dbid) db_name,
 fileid,
 filename
 FROM master.dbo.sysaltfiles
 WHERE dbid > 4
 AND DATABASEPROPERTYEX(DB_NAME(dbid), 'Status') = 'ONLINE'
)

SELECT db_name AS DBName,
 'exec sp_detach_db @dbname = N''' + db_name + ''';' AS DetachScript,
 'exec sp_attach_db @dbname = N''' + db_name + '''' + (
 SELECT
 ', @filename' + CAST(fileid AS varchar) + '=N''' + filename + ''''
 FROM CTE f
 WHERE f.dbid = d.dbid
 FOR xml PATH('')
 ) + ';' AS AttachScript
FROM (
 SELECT DISTINCT dbid, db_name
 FROM CTE
) d
```
