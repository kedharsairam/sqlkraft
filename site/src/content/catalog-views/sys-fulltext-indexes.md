---
name: "sys.fulltext_indexes"
title: "sys.fulltext_indexes"
category: "indexes"
description: "Contains a row per full-text index of a tabular object. ID of the object to which this full-text index belongs. ID of the corresponding unique, non-full-text index that is used to relate the full-text index to the rows. Version of full-text filter and wordbreaker components that are used to populate and query this index. If you perform an in-place upgrade from SQL Server 2022 (16.x) and earlier ve"
tags: ["indexes", "catalog-view"]
pubDate: 2026-05-29
syntax: "change_tracking_state"
---

## Description

Contains a row per full-text index of a tabular object. ID of the object to which this full-text index belongs. ID of the corresponding unique, non-full-text index that is used to relate the full-text index to the rows. Version of full-text filter and wordbreaker components that are used to populate and query this index. If you perform an in-place upgrade from SQL Server 2022 (16.x) and earlier versions to SQL Server 2025 (17.x) and later versions,

## Syntax

```sql
change_tracking_state
```

## Examples

### Example 1

```sql
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
```

### Example 2

```sql
USE AdventureWorks2022;
GO
SELECT property_list_id, name FROM sys.registered_search_property_lists;
GO
```

### Example 3

```sql
JobCandidateProperties
```

### Example 4

```sql
AdventureWorks2022
```

### Example 5

```sql
DROP
SEARCH
PROPERTY
LIST
JobCandidateProperties;
GO
```
