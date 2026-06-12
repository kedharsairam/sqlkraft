---
name: "Combining vector indexes with traditional indexes"
title: "Combining vector indexes with traditional indexes"
category: "queries"
description: ""
tags: ["tsql","queries"]
pubDate: "2026-05-29"
---

## Table hints

## for vector search

For large-scale data replacement (for example, deleting most rows and inserting an

entirely new set of embeddings), consider dropping and recreating the vector index after

the data load to ensure optimal search quality.

Vector indexes perform background maintenance to incorporate DML changes. Use the

sys.dm_db_vector_indexes

dynamic management view to monitor index health and

maintenance task status.

Vector indexes work alongside traditional B-tree indexes to provide optimal query

performance. When using iterative filtering with

, consider creating traditional

indexes on columns used in filter predicates.

For detailed information about iterative filtering behavior and how it differs from earlier

versions, see

Iterative filtering behavior.

７

Note

DML support is only available with vector indexes created using the latest version. Earlier

versions require tables to be read-only or use the

database

scoped configuration.



Tip

The query optimizer automatically selects the best execution strategy (approximate

nearest neighbor index vs. kNN search). To force the use of the approximate nearest

neighbor index, use the

table hint. For more information, see.

## Performance benefit:

## vector index

## traditional index

`VECTOR_SEARCH`

`ALLOW_STALE_VECTOR_INDEX`

`FORCE_ANN_ONLY`

```sql
-- Create vector index for similarity search
CREATE
VECTOR
INDEX idx_embeddings_vector
ON product_embeddings(embedding)
WITH (METRIC =
'cosine'
);
```
