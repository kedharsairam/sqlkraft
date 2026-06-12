---
name: "To Move TempDB to Different Location"
title: "To Move TempDB to Different Location"
description: "identify where the temp database files are located"
category: "database"
tags: ["database"]
pubDate: 2025-03-15
---

```sql
--identify where the temp database files are located select file_id, name, physical_name from tempdb.sys.database_files
--or select name, physical_name as currentlocation, state_desc from sys.master_files where database_id = db_id('tempdb')

--change the location of each file alter database tempdb modify file (name = tempdev, filename = 'path') alter database tempdb modify file (name = templog, filename = 'path')

--finally restart the instance to finish the process
```
