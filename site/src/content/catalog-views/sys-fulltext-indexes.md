---
name: "sys.fulltext_indexes"
title: "sys.fulltext_indexes"
category: "indexes"
description: "Contains a row per full-text index of a tabular object."
tags: ["indexes","catalog-view"]
pubDate: 2026-05-29
syntax: "change_tracking_state"
---

## Description

Contains a row per full-text index of a tabular object.

## Syntax

`change_tracking_state`

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

### Example 2

```sql
USE AdventureWorks2022;
GO
SELECT property_list_id, name FROM sys.registered_search_property_lists;
GO
```

### Example 3

`JobCandidateProperties`

### Example 4

`AdventureWorks2022`

### Example 5

```sql
DROP
SEARCH
PROPERTY
LIST
JobCandidateProperties;
GO
```
