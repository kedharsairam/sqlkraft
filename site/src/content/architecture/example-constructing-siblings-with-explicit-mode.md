---
title: "Example: Constructing Siblings with EXPLICIT Mode"
topic: "xml-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  Assume that you want to construct XML that provides sales order information. In this example,
tags:
  - "xml-data"
  - "example-constructing-siblings-with-explicit-mode"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Assume that you want to construct XML that provides sales order information. In this example,

and

elements are siblings. Each Order has one

element, one

element, and one or more

elements.

XML

The following EXPLICIT mode query constructs this XML. The query specifies

values of 1 for

the

element, 2 for the

element, and 3 for the

element. Because

and

are siblings, the query specifies the same

tag value of 1 identifying the

element.

```sql
<SalesPerson>
<OrderDetail>
<OrderHeader>
<SalesPerson>
<OrderDetail>
Tag
<OrderHeader>
<SalesPerson>
<OrderDetail>
<SalesPerson>
<OrderDetail>
Parent
<OrderHeader>
<OrderHeader
SalesOrderID
=.
OrderDate
=.
CustomerID
=.
>
<SalesPerson
SalesPersonID
=.
/>
<OrderDetail
SalesOrderID
=.
LineTotal
=.
ProductID
=.
OrderQty
=.
/>
<OrderDetail
SalesOrderID
=.
LineTotal
=.
ProductID
=.
OrderQty
=./
>.
</OrderHeader>
<OrderHeader.
</
OrderHeader
>
USE
AdventureWorks2022;
GO
SELECT
1 as
Tag,
0 as
Parent
,
SalesOrderID as
[OrderHeader!1!SalesOrderID],
OrderDate as
[OrderHeader!1!OrderDate],
CustomerID as
[OrderHeader!1!CustomerID],
NULL as
[SalesPerson!2!SalesPersonID],
NULL as
[OrderDetail!3!SalesOrderID],
NULL as
[OrderDetail!3!LineTotal],
NULL as
[OrderDetail!3!ProductID],
NULL as
[OrderDetail!3!OrderQty]
FROM
Sales.SalesOrderHeader
WHERE
SalesOrderID=43659 or
SalesOrderID=43661
UNION
ALL
SELECT
2 as
Tag,
1 as
Parent
,
SalesOrderID,
NULL
,
NULL
,
SalesPersonID,
```
