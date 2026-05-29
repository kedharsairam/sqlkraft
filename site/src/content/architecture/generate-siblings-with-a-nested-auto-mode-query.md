---
title: "Generate Siblings with a Nested AUTO Mode Query"
topic: "xml-data"
description: |
  Article
  
  •
  
  02/28/2023
  
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  The following example shows how to generate siblings by using a nested AUTO mode query.
  
  The only other
tags:
  - "xml-data"
  - "generate-siblings-with-a-nested-auto-mode-query"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

The following example shows how to generate siblings by using a nested AUTO mode query.

The only other way to generate such XML is to use the EXPLICIT mode. However, this can be

cumbersome.

This query constructs XML that provides sales order information. This includes the following:

Sales order header information,

,

, and

.

stores this information in the

table.

Sales order detail information. This includes one or more products ordered, the unit price,

and the quantity ordered. This information is stored in the

table.

Sales person information. This is the salesperson who took the order. The

table provides the

. For this query, you have to join this table to the

table to find the name of the sales person.

The two distinct

queries that follow generate XML with a small difference in shape.

The first query generates XML in which

and

appear as

sibling children of

:

SQL

```sql
SalesOrderID
SalesPersonID
OrderDate
AdventureWorks2022
SalesOrderHeader
SalesOrderDetail
SalesPerson
SalesPersonID
Employee
SELECT
<SalesPerson>
<SalesOrderHeader>
<SalesOrder>
SELECT
(
SELECT
top 2 SalesOrderID, SalesPersonID, CustomerID,
(
select
top 3 SalesOrderID, ProductID, OrderQty, UnitPrice
from
Sales.SalesOrderDetail
WHERE
SalesOrderDetail.SalesOrderID =
SalesOrderHeader.SalesOrderID
FOR
XML
AUTO
,
TYPE
)
FROM
Sales.SalesOrderHeader
WHERE
SalesOrderHeader.SalesOrderID = SalesOrder.SalesOrderID
for
xml
auto
,
type
),
(
SELECT
*
FROM
(
SELECT
SalesPersonID, EmployeeID
FROM
Sales.SalesPerson, HumanResources.Employee
WHERE
SalesPerson.SalesPersonID = Employee.EmployeeID)
As
```