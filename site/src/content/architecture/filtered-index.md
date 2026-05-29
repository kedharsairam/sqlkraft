---
title: "Filtered index"
topic: "filestream"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  This article describes how to create a filtered index using SQL Server Management Studio
  
  (SS
tags:
  - "filestream"
  - "filtered-index"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

This article describes how to create a filtered index using SQL Server Management Studio

(SSMS) or Transact-SQL. A filtered index is an optimized disk-based rowstore nonclustered

index especially suited to cover queries that select from a well-defined subset of data. It uses a

filter predicate to index a portion of rows in the table. A well-designed filtered index can

improve query performance and reduce index maintenance and storage costs compared with

full-table indexes.

Filtered indexes can provide the following advantages over full-table indexes:

1. Improved query performance and plan quality.

A well-designed filtered index improves query performance and execution plan quality

because it's smaller than a full-table nonclustered index and has filtered statistics. The

filtered statistics are more accurate than full-table statistics because they cover only the

rows in the filtered index.

2. Reduced index maintenance costs.

An index is maintained only when data manipulation language (DML) statements affect

the data in the index. A filtered index reduces index maintenance costs compared with a

full-table nonclustered index because it's smaller and is only maintained when the data in

the index is changed. It's possible to have a large number of filtered indexes, especially

when they contain data that is changed infrequently. Similarly, if a filtered index contains

only the frequently modified data, the smaller size of the index reduces the cost of

updating the statistics.

3. Reduced index storage costs.

Creating a filtered index can reduce disk storage for nonclustered indexes when a full-

table index isn't necessary. You can replace a full-table nonclustered index with multiple

filtered indexes without significantly increasing the storage requirements.

When a column only has a few relevant values for queries, you can create a filtered index on

the subset of values. The resulting index will be smaller and cost less to maintain than a full-

table nonclustered index defined on the same key columns.