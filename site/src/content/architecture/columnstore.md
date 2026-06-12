---
title: "columnstore"
topic: "query-processing"
description: "When the columnstore index compresses a rowgroup, it compresses each column segment"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

When the columnstore index compresses a rowgroup, it compresses each column segment

separately. To uncompress an entire column, the columnstore index only needs to uncompress

one column segment from each rowgroup.

A columnstore index improves columnstore compression and performance by compressing at

least 102,400 rows at a time into the columnstore index. To compress rows in bulk, the

columnstore index accumulates small loads and inserts in the deltastore. The deltastore

operations are handled in the background. To return query results, the clustered columnstore

index combines query results from both the columnstore and the deltastore.

Rows go to the deltastore when they are:

Inserted with the

statement.

At the end of a bulk load, and they number less than 102,400.

Updated. Each update is implemented as a delete and an insert.

The deltastore also stores a list of IDs for deleted rows that have been marked as deleted but

not yet physically deleted from the columnstore.

Clustered columnstore indexes collect up to 1,048,576 rows in each delta rowgroup before

compressing the rowgroup into the columnstore. This improves the compression of the

columnstore index. When a delta rowgroup reaches the maximum number of rows, it

```sql
INSERT INTO. VALUES
```
