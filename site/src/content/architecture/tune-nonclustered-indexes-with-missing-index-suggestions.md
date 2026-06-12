---
title: "Tune nonclustered indexes with missing index suggestions"
topic: "filestream"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The missing indexes feature is a lightweight tool for finding missing indexes that might

  sig
tags:
  - "filestream"
  - "tune-nonclustered-indexes-with-missing-index-suggestions"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The missing indexes feature is a lightweight tool for finding missing indexes that might

significantly improve query performance. This article describes how to use missing index

suggestions to effectively tune indexes and improve query performance.

When the query optimizer generates a query plan, it analyzes what the best indexes are for a

particular filter condition. If the best indexes don't exist, the query optimizer still generates a

query plan using the least-costly access methods available, but also stores information about

these indexes. The missing indexes feature enables you to access that information about best

possible indexes so you can decide whether they should be implemented.

Query optimization is a time sensitive process, so there are limitations to the missing index

feature. Limitations include:

Missing index suggestions are based on estimates made during the optimization of a

single query, prior to query execution. Missing index suggestions aren't tested or updated

after query execution.

The missing index feature suggests only nonclustered disk-based rowstore indexes.

Unique

and

Filtered indexes

aren't suggested.

Key columns are suggested, but the suggestion doesn't specify an order for those

columns. For information on ordering columns, see the

Apply missing index suggestions

section of this article.

Included columns

are suggested, but SQL Server performs no cost-benefit analysis

regarding the size of the resulting index when a large number of included columns are

suggested.

Missing index requests might offer similar variations of indexes on the same table and

column(s) across queries. It's important to

review index suggestions and combine where

possible.

Suggestions aren't made for trivial query plans.

Cost information is less accurate for queries involving only inequality predicates.

Suggestions are gathered for a maximum of 600 missing index groups. After this

threshold is reached, no more missing index group data is gathered.
