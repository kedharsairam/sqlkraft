---
name: "sys.database_files"
title: "sys.database_files"
category: "databases-files"
description: "Contains a row per file of a database as stored in the database itself. This is a per-database ID of the file within database. = Database was upgraded from an earlier version of SQL Server (Valid for SQL Server 2005 and earlier 3 = Identified for informational purposes only. Not supported. Future compatibility is not guaranteed."
tags: ["databases-files","catalog-view"]
pubDate: 2026-05-29
syntax: |
  ROWS
              LOG
              FILESTREAM
              FULLTEXT
              data_space_id
---

## Description

Analytics Platform System (PDW) Contains a row per file of a database as stored in the database itself. This is a per-database ID of the file within database. = Database was upgraded from an earlier version of SQL Server (Valid for SQL Server 2005 and earlier 3 = Identified for informational purposes only. Not supported. Future compatibility is not guaranteed. Value can be zero or greater than zero.

## Syntax

```sql
ROWS
LOG
FILESTREAM
FULLTEXT data_space_id
```

## Examples

### Example 1

```sql
SELECT name
,
size
/128.0 FileSizeInMB,
size
/128.0 -
CAST (FILEPROPERTY(
name
,
'SpaceUsed'
)
AS int
)/128.0
AS
EmptySpaceInMB
FROM sys.database_files;
```

### Example 2

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
