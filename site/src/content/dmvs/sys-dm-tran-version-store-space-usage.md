---
name: "sys.dm_tran_version_store_space_usage"
title: "sys.dm_tran_version_store_space_usage"
category: "io"
description: "SQL Server 2016 (13.x) SP2 and later versions SQL database in Microsoft Fabric Returns a table that displays total space in used by version store records for each is efficient and not expensive to run, as it doesn't navigate through individual version store records, and returns aggregated version store space consumed in tempdb per database. Each versioned record is stored as binary data, together"
tags: ["io", "dmv"]
pubDate: 2026-05-29
syntax: |
  SELECT
  DB_NAME(database_id)
  as
  'Database Name'
  ,
  reserved_page_count,
  reserved_space_kb
  FROM
  sys.dm_tran_version_store_space_usage;
  Database Name            reserved_page_count reserved_space_kb
  ------------------------ -------------------- -----------
  msdb                      0                    0
  AdventureWorks2022        10                   80
  AdventureWorks2022DW      0                    0
  WideWorldImporters        20                   160
---

## Description

SQL Server 2016 (13.x) SP2 and later versions SQL database in Microsoft Fabric Returns a table that displays total space in used by version store records for each is efficient and not expensive to run, as it doesn't navigate through individual version store records, and returns aggregated version store space consumed in tempdb per database. Each versioned record is stored as binary data, together with some tracking or status

## Syntax

```sql
SELECT
DB_NAME(database_id) as
'Database Name'
,
reserved_page_count,
reserved_space_kb
FROM sys.dm_tran_version_store_space_usage;
Database Name            reserved_page_count reserved_space_kb
------------------------ -------------------- -----------
msdb                      0                    0
AdventureWorks2022        10                   80
AdventureWorks2022DW      0                    0
WideWorldImporters        20                   160
```

## Permissions

SQL Server 2016 (13.x) SP2 and later versions Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric Returns a table that displays total space in used by version store records for each database. is efficient and not expensive to run, as it doesn't navigate through individual version store records, and returns aggregated version store space consumed in tempdb per database. Each versioned record is stored as binary data, together with some tracking or status information. Similar to records in database tables, version-store records are stored in 8192- byte pages. If a record exceeds 8,192 bytes, the record is split across two different records. Because the versioned record is stored as binary, there are no problems with different collations from different databases. Use to monitor and plan size based on the version store space usage of databases in a SQL Server instance. Database ID of the database. In Azure SQL Database, the values are unique within a single database or an elastic pool, but not within a logical server. Total count of the pages reserved in for version store records of the database. Total space used in kilobytes in for version store records of the database. On SQL Server, requires permission. Requires VIEW SERVER PERFORMANCE STATE permission on the server. ﾉ
