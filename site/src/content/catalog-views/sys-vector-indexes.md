---
name: "sys.vector_indexes"
title: "sys.vector_indexes"
category: "indexes"
description: "Contains a row per vector index. Type of vector index (DiskANN only for now) Metric used to create the vector index The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission."
tags: ["indexes","catalog-view"]
pubDate: 2026-05-29
syntax: "[dbo].[wikipedia_articles_embeddings]"
---

## Description

Contains a row per vector index. Type of vector index (DiskANN only for now) Metric used to create the vector index The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission.

## Syntax

```sql
[dbo].[wikipedia_articles_embeddings]
```

## Examples

### Example 1

```sql
[dbo].[wikipedia_articles_embeddings]
```

### Example 2

```sql
SELECT object_id,
index_id,
vector_index_type,
distance_metric,
build_parameters
FROM sys.vector_indexes
AS vi
WHERE object_id = OBJECT_ID(
'[dbo].[wikipedia_articles_embeddings]'
)
```
