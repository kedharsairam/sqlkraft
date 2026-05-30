---
name: "sys.fulltext_index_columns"
title: "sys.fulltext_index_columns"
category: "objects"
description: 'Contains a row for each column that is part of a full-text index. ID of the object of which this is part. ID of the column that is part of the full-text index. ID of the type column that stores the user-supplied document file extension-".doc", ".xls", and so forth-of the document in a given row. The type column is specified only for columns whose data requires filtering during full-text indexing. '
tags: ["objects", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  USE
  AdventureWorks2025;
  GO
  SELECT
  object_id,
  property_list_id,
  stoplist_id
  FROM
  sys.fulltext_indexes
  WHERE
  object_id = object_id(
  'HumanResources.JobCandidate'
  );
---

## Description

Contains a row for each column that is part of a full-text index. ID of the object of which this is part. ID of the column that is part of the full-text index. ID of the type column that stores the user-supplied document file extension-".doc", ".xls", and so forth-of the document in a given row. The type column is specified only for columns whose data requires filtering during full-text indexing. NULL if not applicable. For more information,

## Syntax

```sql
USE
AdventureWorks2025;
GO
SELECT object_id,
property_list_id,
stoplist_id
FROM sys.fulltext_indexes
WHERE object_id = object_id(
'HumanResources.JobCandidate'
);
```

## Permissions

Article • 02/28/2023 Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance Contains a row for each column that is part of a full-text index. Description ID of the object of which this is part. ID of the column that is part of the full-text index. ID of the type column that stores the user-supplied document file extension-".doc", ".xls", and so forth-of the document in a given row. The type column is specified only for columns whose data requires filtering during full-text indexing. NULL if not applicable. For more information, see Configure and Manage Filters for Search . LCID of language whose word breaker is used to index this full-text column. 0 = Neutral. For more information, see sys.fulltext_languages (Transact-SQL) . 1 = This column has statistical semantics enabled in addition to full-text indexing. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. Object Catalog Views (Transact-SQL) Catalog Views (Transact-SQL) ﾉ Expand table See Also SQL sys.fulltext_index_fragments sys.fulltext_index_columns sys.fulltext_index_catalog_usages Object catalog views (Transact-SQL) System catalog views (Transact-SQL) Create and manage full-text indexes DROP FULLTEXT INDEX (Transact-SQL) CREATE FULLTEXT INDEX (Transact-SQL) ALTER FULLTEXT INDEX (Transact-SQL) Last updated on 12/02/2025 For the code example that creates this full-text index, see the section of . Related content

## Examples

### Example 1

```sql
USE
AdventureWorks2025;
GO
SELECT object_id,
property_list_id,
stoplist_id
FROM sys.fulltext_indexes
WHERE object_id = object_id(
'HumanResources.JobCandidate'
);
```
