---
title: "Unique index"
topic: "filestream"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  This topic describes how to create a unique index on a table in SQL Server by using SQL Serve
tags:
  - "filestream"
  - "unique-index"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

This topic describes how to create a unique index on a table in SQL Server by using SQL Server

Management Studio or Transact-SQL. A unique index guarantees that the index key contains

no duplicate values and therefore every row in the table is in some way unique. There are no

significant differences between creating a UNIQUE constraint and creating a unique index that

is independent of a constraint. Data validation occurs in the same manner, and the query

optimizer does not differentiate between a unique index created by a constraint or manually

created. However, creating a UNIQUE constraint on the column makes the objective of the

index clear. For more information on UNIQUE constraints, see

Unique Constraints and Check

Constraints.

When you create a unique index, you can set an option to ignore duplicate keys. If this option

is set to

and you attempt to create duplicate keys by adding data that affects multiple rows

(with the INSERT statement), the row containing a duplicate is not added. If it is set to

, the

entire insert operation fails and all the data is rolled back.

Benefits of a Unique Index

Typical Implementations

Limitations and Restrictions

Security

Management Studio

Transact-SQL

７

Note

You cannot create a unique index on a single column if that column contains NULL in

more than one row. Similarly, you cannot create a unique index on multiple columns if the

combination of columns contains NULL in more than one row. These are treated as

duplicate values for indexing purposes.
