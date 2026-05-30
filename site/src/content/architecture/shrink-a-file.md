---
title: "Shrink a file"
topic: "collation"
description: |
  Article

  •

  07/03/2024

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  This article describes how to shrink a data or log file in SQL Server by using SQL Server

  Management S
tags:
  - "collation"
  - "shrink-a-file"
pubDate: 2025-12-01
---

Article

•

07/03/2024

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

This article describes how to shrink a data or log file in SQL Server by using SQL Server

Management Studio or Transact-SQL.

Shrinking data files recovers space by moving pages of data from the end of the file to

unoccupied space closer to the front of the file. When enough free space is created at the end

of the file, data pages at end of the file can be deallocated and returned to the file system.

The primary data file can't be made smaller than the size of the primary file in the

database.

A shrink operation is most effective after an operation that creates a large amount of

unused storage space, such as a large DELETE statement, truncate table, or a drop table

operation.

Most databases require some free space to be available for regular day-to-day

operations. If you shrink a database file repeatedly and notice that the database size

grows again, this indicates that the free space is required for regular operations. In these

cases, repeatedly shrinking the database file is a wasted operation. Autogrow events

necessary to grow the database file a hinder performance.

Data that is moved to shrink a file can be scattered to any available location in the file.

This causes index fragmentation and can slow the performance of queries that search a

range of the index. To eliminate the fragmentation, consider rebuilding the indexes on the

file after shrinking.

Unless you have a specific requirement, don't set the AUTO_SHRINK database option to

ON.

Shrink operations in progress can block other queries on the database, and can be blocked by

queries already in progress. Introduced in SQL Server 2022 (16.x), shrink file operations have a

`model`
