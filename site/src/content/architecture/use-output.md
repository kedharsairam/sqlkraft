---
title: "Use output"
topic: "json-data"
description: |
  Applies to:

  SQL Server 2016 (13.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  Azure Synapse Analytics (serverless SQL pool only)

  SQL

  database in Microsoft Fabric

  The foll
tags:
  - "json-data"
  - "use-output"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

Azure Synapse Analytics (serverless SQL pool only)

database in Microsoft Fabric

The following examples demonstrate some of the ways to use the

clause and its

JSON output in SQL Server or in client apps. For more information, see

Format query results as

JSON with FOR JSON

.

In Fabric Data Warehouse,

must be the last operator in the query, and so is not

allowed inside subqueries, as in the examples in this article.

The output of the

clause is of type

, so you can assign it to any

variable, as shown in the following example.

You can create user-defined functions that format result sets as JSON and return this JSON

output. The following example creates a user-defined function that fetches some sales order

detail rows and formats them as a JSON array.

```sql
FOR JSON
FOR JSON
FOR JSON
DECLARE
@x
NVARCHAR (
MAX
) =
(
SELECT
TOP 10 *
FROM
Sales.SalesOrderHeader
FOR
JSON
AUTO
)
CREATE
FUNCTION
GetSalesOrderDetails(@salesOrderId int
)
RETURNS
NVARCHAR (
MAX
)
AS
BEGIN
RETURN (
SELECT
UnitPrice, OrderQty
FROM
Sales.SalesOrderDetail
```
