---
name: 'sys.database_files'
title: 'sys.database_files'
category: 'databases-files'
description: 'Requires membership in the'
tags: ["catalog-view", "databases-files"]
pubDate: 2026-05-29
---

Requires membership in the

role. For more information, see

Metadata Visibility

Configuration

.

The following statement returns the name, file size, and the amount of empty space for each

database file.

SQL

Find example queries using SQL Database, in

Manage file space for databases in Azure SQL

Database

. You can:

Query a single database for storage space information

.

Query an elastic pool for storage space information

.

Databases and Files Catalog Views (Transact-SQL)

File States

sys.databases (Transact-SQL)

sys.master_files (Transact-SQL)

Database Files and Filegroups

sys.data_spaces (Transact-SQL)

Manage file space for databases in Azure SQL Database

Manage file space for databases in Azure SQL Managed Instance

Last updated on 11/18/2025

Related content

```sql
SELECT
name
,
size
/128.0 FileSizeInMB,
size
/128.0 -
CAST
(FILEPROPERTY(
name
,
'SpaceUsed'
)
AS
int
)/128.0
AS
EmptySpaceInMB
FROM
sys.database_files;
```
