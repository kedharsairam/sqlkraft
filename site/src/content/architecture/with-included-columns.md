---
title: "With included columns"
topic: "filestream"
description: ""
tags: ["filestream","with-included-columns"]
pubDate: 2025-12-01
---

This article describes how to add included (or nonkey) columns to extend the functionality of

nonclustered indexes in SQL Server by using SQL Server Management Studio or Transact-SQL.

By including nonkey columns, you can create nonclustered indexes that cover more queries.

This is because the nonkey columns have the following benefits:

They can be data types not allowed as index key columns.

They aren't considered by the Database Engine when calculating the number of index key

columns or index key size.

An index with nonkey columns can significantly improve query performance when all columns

in the query are included in the index either as key or nonkey columns. Performance gains are

achieved because the query optimizer can locate all the column values within the index; table

or clustered index data isn't accessed resulting in fewer disk I/O operations.

Redesign nonclustered indexes that have a large index key size so that only columns used

for searching and lookups are key columns. Make all other columns that cover the query

into nonkey columns. In this way, you'll have all columns needed to cover the query, but

the index key itself is small and efficient.

Include nonkey columns in a nonclustered index to avoid exceeding the current index size

limitations of a maximum of 32 key columns and a maximum index key size of 1,700 bytes

(16 key columns and 900 bytes prior to SQL Server 2016 (13.x)). The Database Engine

doesn't consider nonkey columns when calculating the number of index key columns or

index key size.

The order of nonkey columns in the index definition doesn't affect the performance of

queries that use the index.

Avoid very wide nonclustered indexes where the included columns don't represent a

narrow enough subset of the underlying table columns. If adding wide indexes, always

７

Note

When an index contains all the columns referenced by a query it's typically referred to as

covering the query.
