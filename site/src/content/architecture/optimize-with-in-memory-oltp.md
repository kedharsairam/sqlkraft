---
title: "Optimize with in-memory OLTP"
topic: "json-data"
description: |
  Applies to:
  
  SQL Server 2017 (14.x) and later versions
  
  Azure SQL Database
  
  Azure
  
  SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  SQL Server and Azure SQL Database let you work with text form
tags:
  - "json-data"
  - "optimize-with-in-memory-oltp"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2017 (14.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

SQL Server and Azure SQL Database let you work with text formatted as JSON. To increase the

performance of queries that process JSON data, you can store JSON documents in memory-

optimized tables using standard string columns (

type). Storing JSON data in memory-

optimized tables increases query performance by using lock-free, in-memory data access.

The following example shows a memory-optimized

table with two JSON columns,

and

:

SQL

You can fully integrate JSON functionality with existing in-memory OLTP technologies. For

example, you can do the following things:

Validate the structure of JSON documents

stored in memory-optimized tables by using

natively compiled CHECK constraints.

Expose and strongly type values

stored in JSON documents by using computed columns.

Index values

in JSON documents by using memory-optimized indexes.

```sql
Product
Tags
Data
CREATE
SCHEMA
xtp;
GO
CREATE
TABLE
xtp.Product (
ProductID
INT
PRIMARY
KEY
NONCLUSTERED,
--standard column
Name
NVARCHAR
(400)
NOT
NULL
,
--standard column
Price
FLOAT
,
--standard column
Tags
NVARCHAR
(400),
--JSON stored in string column
Data
NVARCHAR
(4000)
--JSON stored in string column
)
WITH
(MEMORY_OPTIMIZED =
ON
);
GO
```