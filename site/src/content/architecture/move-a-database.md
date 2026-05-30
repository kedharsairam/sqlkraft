---
title: "Move a Database"
topic: "filestream"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  This article shows how to move a FILESTREAM-enabled database.

  1. In SQL Server Management Studio, select

  to open the Query Editor.

  2. Copy the follo
tags:
  - "filestream"
  - "move-a-database"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

This article shows how to move a FILESTREAM-enabled database.

1. In SQL Server Management Studio, select

to open the Query Editor.

2. Copy the following Transact-SQL script into the Query Editor, and then select

.

This script displays the location of the physical database files that the FILESTREAM

database uses.

3. Copy the following Transact-SQL script into the Query Editor, and then select

.

This code takes the

database offline.

4. Create the folder

, and then move the files and folders that are listed in

step 2 into it.

5. Copy the following Transact-SQL script into the Query Editor, and then select

.

This script sets the

database online.

７

Note

The examples in this topic require the

database that is created in

.

```sql
Archive
C:\moved_location
Archive
Archive
USE
[
Archive
]
GO
SELECT type_desc,
name
, physical_name from sys.database_files;
USE
[
master
]
EXEC sp_detach_db [
Archive
];
GO
```
