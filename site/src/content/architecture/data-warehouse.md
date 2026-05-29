---
title: "Data warehouse"
topic: "filestream"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  Analytics Platform System (PDW)
  
  SQL database in Microsoft Fabric
  
  Columnstore indexes, in conjunction with partitioning, are e
tags:
  - "filestream"
  - "data-warehouse"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Analytics Platform System (PDW)

SQL database in Microsoft Fabric

Columnstore indexes, in conjunction with partitioning, are essential for building a SQL Server

data warehouse. This article focuses on key use cases and examples for data warehousing

designs with the SQL Database Engine.

SQL Server 2016 (13.x) introduced these features for columnstore performance enhancements:

Always On availability groups support querying a columnstore index on a readable

secondary replica.

Multiple Active Result Sets (MARS) supports columnstore indexes.

A new dynamic management view

sys.dm_db_column_store_row_group_physical_stats

(Transact-SQL)

provides performance troubleshooting information at the row group level.

All queries on columnstore indexes can run in batch mode. Previously, only parallel

queries could run in batch mode.

The

,

, and

operators run in batch mode.

Window aggregates now runs in batch mode for database compatibility level 130 and

higher.

Aggregate pushdown for efficient processing of aggregates. This is supported on all

database compatibility levels.

String predicate pushdown for efficient processing of string predicates. This is supported

on all database compatibility levels.

Snapshot isolation for database compatibility level 130 and higher.

Ordered clustered columnstore indexes were introduced with SQL Server 2022 (16.x). For

more information, see

CREATE COLUMNSTORE INDEX

and

Performance tuning with

ordered columnstore indexes

. For ordered columnstore index availability, see

Ordered

column index availability

.

For more information about new features in versions and platforms of SQL Server and Azure

SQL, see

What's new in columnstore indexes

.

Starting with SQL Server 2016 (13.x), you can create rowstore nonclustered indexes on a

clustered columnstore index.