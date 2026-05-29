---
name: 'To Generate Script to Move Tempdb files'
title: 'To Generate Script to Move Tempdb files'
description: 'SQL Server diagnostic script for database operations.'
category: database
tags: ["database"]
pubDate: 2025-03-15
---

```sql
USE master;
GO
DECLARE @newfilepath NVARCHAR(260) = ''; -- Update this with your new file path

DECLARE @stmt NVARCHAR(MAX) = '';
SELECT @stmt += 'ALTER DATABASE tempdb MODIFY FILE (NAME = ' + name + ', FILENAME = ''' + @newfilepath + REPLACE(physical_name, '', '') + ''') '  + CHAR(13)
FROM tempdb.sys.database_files;
PRINT @stmt
```
