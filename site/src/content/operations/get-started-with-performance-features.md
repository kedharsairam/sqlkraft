---
title: "Get started with performance features"
topic: "linux-operations"
description: |
  Applies to:
  
  SQL Server
  
  on Linux
  
  If you're a Linux user who is new to SQL Server, the following tasks walk you through some of the
  
  performance features. These aren't unique or specific to Linux, bu
tags:
  - "linux-operations"
  - "get-started-with-performance-features"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

If you're a Linux user who is new to SQL Server, the following tasks walk you through some of the

performance features. These aren't unique or specific to Linux, but it helps to give you an idea of

areas to investigate further. In each example, a link is provided to the depth documentation for

that area.

A columnstore index is a technology for storing and querying large stores of data in a columnar

data format, called a columnstore.

1. Add a columnstore index to the

table by executing the following

Transact-SQL commands:

SQL

2. Execute the following query that uses the columnstore index to scan the table:

SQL

７

Note

The following examples use the

sample database. For instructions on

how to obtain and install this sample database, see

.

```cmd
SalesOrderDetail
AdventureWorks2022
CREATE
NONCLUSTERED COLUMNSTORE
INDEX
[IX_SalesOrderDetail_ColumnStore]
ON
Sales.SalesOrderDetail(UnitPrice, OrderQty, ProductID);
GO
SELECT
ProductID,
SUM
(UnitPrice)
AS
SumUnitPrice,
AVG
(UnitPrice)
AS
AvgUnitPrice,
SUM
(OrderQty)
AS
SumOrderQty,
AVG
(OrderQty)
AS
AvgOrderQty
FROM
Sales.SalesOrderDetail
```