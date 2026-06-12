---
name: "sys.master_files"
title: "sys.master_files"
category: "databases-files"
description: "Contains a row per file of a database as stored in the ID of the database to which this file applies. The ID of the file within database. The primary Unique identifier of the file. = Database was upgraded from an earlier version of SQL Server (Valid for SQL Server 2005 (9.x) and earlier = Identified for informational purposes only. Not supported. Future compatibility is not guaranteed. = Full-text"
tags: ["databases-files","catalog-view"]
pubDate: "2026-05-29"
syntax: |
  ROWS
      LOG
      FILESTREAM
      FULLTEXT
---

## Description

Contains a row per file of a database as stored in the ID of the database to which this file applies. The ID of the file within database. The primary Unique identifier of the file. = Database was upgraded from an earlier version of SQL Server (Valid for SQL Server 2005 (9.x) and earlier = Identified for informational purposes only. Not supported. Future compatibility is not guaranteed. = Full-text (Full-text catalogs earlier than SQL Server

## Syntax

```sql
ROWS
LOG
FILESTREAM
FULLTEXT
```

## Permissions

Description Azure Blob Storage, a credential is configured with the access credentials to the storage location. When you drop or rebuild large indexes, or drop or truncate large tables, the Database Engine defers the actual page deallocations, and their associated locks, until after the transaction commits. Deferred drop operations don't release allocated space immediately. Therefore, the values returned by immediately after dropping or truncating a large object might not reflect the actual disk space available. For the database, shows the initial size. The values are used as a template for creation at startup of SQL Server. growth isn't reflected in this view. To get the current size of files, query instead. The minimum permissions that are required to see the corresponding row are , , or. Databases and Files Catalog Views (Transact-SQL) File States sys.databases (Transact-SQL) sys.database_files (Transact-SQL) Database Files and Filegroups
## Examples

### Example 1

`SpaceUsed`

### Example 2

`sys.master_files`

### Example 3

`sys.database_files`

### Example 4

`IsPrimaryFile`

### Example 5

`AdventureWorks_Data`

### Example 6

```sql
SELECT
FILEPROPERTY(
'AdventureWorks2022_Data'
,
'IsPrimaryFile'
)
AS
[Primary
File
];
GO
Primary File
-------------
1
```

### Example 7

```sql
SELECT s.file_id,
s.type_desc,
s.name,
FILEPROPERTYEX(s.name,
'BlobTier'
)
AS
BlobTier,
FILEPROPERTYEX(s.name,
'AccountType'
)
AS
AccountType,
FILEPROPERTYEX(s.name,
'IsInferredTier'
)
AS
IsInferredTier,
FILEPROPERTYEX(s.name,
'IsPageBlob'
)
AS
IsPageBlob
FROM sys.database_files
AS s
WHERE s.type_desc
IN (
'ROWS'
,
'LOG'
);
file_id type_desc name BlobTier AccountType IsInferredTier IsPageBlob
------------------------------------------------------------------------------------
--
1 ROWS data_0 P30 PremiumBlobStorage 0 1
2 LOG log P30 PremiumBlobStorage 0 1 (2 rows affected)
```
