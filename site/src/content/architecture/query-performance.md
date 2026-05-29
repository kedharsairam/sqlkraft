---
title: "Query performance"
topic: "filestream"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  Azure Synapse Analytics
  
  Analytics Platform System (PDW)
  
  SQL database in Microsoft
  
  Fabric
  
  This article includes recommendati
tags:
  - "filestream"
  - "query-performance"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

This article includes recommendations for achieving the fast query performance with

columnstore indexes.

Columnstore indexes can achieve up to 100 times better performance on analytics and data

warehousing workloads, and up to 10 times better data compression than traditional rowstore

indexes. These recommendations help your queries achieve the fast query performance that

columnstore indexes are designed to provide.

Here are some recommendations for achieving the high-performance columnstore indexes are

designed to provide.

In common case in traditional data warehouse, the data is

indeed inserted in time order and analytics is done in time dimension. For example,

analyzing sales by quarter. For this kind of workload, the rowgroup elimination happens

automatically. In SQL Server 2016 (13.x), you can find out number rowgroups skipped as

part of query processing.

If the common query predicate is on a column (for

example,

) unrelated to the insert order, create a rowstore clustered index on column

. Then, drop the rowstore clustered index and create a clustered columnstore index. If

you create the clustered columnstore index explicitly using

, the resulting

clustered columnstore index is perfectly ordered on column

. If you specify

,

then you see overlap of values across eight rowgroups. For a nonclustered columnstore

index (NCCI), if the table has a rowstore clustered index, the rows are already ordered by

the clustered index key. In this case, the nonclustered columnstore index is also

automatically ordered. A columnstore index doesn't inherently maintain the order of

rows. As new rows are inserted or older rows are updated, you might need to repeat the

process as the analytics query performance might deteriorate.

```sql
C1
C1
MAXDOP = 1
C1
MAXDOP = 8
```