---
title: "Example: Specifying the ID & IDREF Directives"
topic: "xml-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  This example is almost the same as the

  Specifying the ELEMENTXSINIL Directive

  example. The

tags:
  - "xml-data"
  - "example-specifying-the-id-idref-directives"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

This example is almost the same as the

Specifying the ELEMENTXSINIL Directive

example. The

only difference is that the query specifies the

and

directives. These directives

overwrite the types of the

attribute in the

and

elements, and form intra-document links. You need the schema to see the overwritten types.

Therefore, the query specifies the

option in the FOR XML clause to retrieve the

schema.

SQL

```sql
<OrderHeader>
<OrderDetail>
USE
AdventureWorks2022;
GO
SELECT
1
as
Tag,
0
as
Parent
,
SalesOrderID
as
[OrderHeader!1!SalesOrderID!
id
],
OrderDate
as
[OrderHeader!1!OrderDate],
CustomerID
as
[OrderHeader!1!CustomerID],
NULL
as
[SalesPerson!2!SalesPersonID],
NULL
as
[OrderDetail!3!SalesOrderID!idref],
NULL
as
[OrderDetail!3!LineTotal],
NULL
as
[OrderDetail!3!ProductID],
NULL
as
[OrderDetail!3!OrderQty]
FROM
Sales.SalesOrderHeader
WHERE
SalesOrderID
IN
(43659, 43661)
UNION
ALL
SELECT
2
as
Tag,
1
as
Parent
,
SalesOrderID,
NULL
,
NULL
,
SalesPersonID,
NULL
,
NULL
,
NULL
,
NULL
FROM
Sales.SalesOrderHeader
WHERE
SalesOrderID
IN
(43659, 43661)
UNION
ALL
SELECT
3
as
Tag,
1
as
Parent
,
SOD.SalesOrderID,
NULL
,
NULL
,
```
