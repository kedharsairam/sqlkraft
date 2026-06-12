---
name: "To Identify Differential Base LSN"
title: "To Identify Differential Base LSN"
description: "diagnostic script for backup-restore operations."
category: backup-restore
tags: ["backup-restore"]
pubDate: 2025-03-15
---

```sql
select a.name as dbname,
b.name as dbfilename,
b.differential_base_lsn,
b.differential_base_guid,
b.differential_base_time from sys.master_files b join sys.databases a on b.database_id = a.database_id where b.database_id = databaseid and b.file_id <> '2'
```
