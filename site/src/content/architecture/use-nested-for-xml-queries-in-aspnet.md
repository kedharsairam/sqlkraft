---
title: "Use Nested FOR XML Queries in ASP.NET"
topic: "xml-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  In this example, an ASP.NET application returns XML to a browser by executing a stored

  proce
tags:
  - "xml-data"
  - "use-nested-for-xml-queries-in-aspnet"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

In this example, an ASP.NET application returns XML to a browser by executing a stored

procedure in SQL Server. The stored procedure generates XML by using nested queries. A

similar SELECT statement is shown in the article

Generating Siblings by Using a Nested AUTO

Mode Query. This example demonstrates one way to use nested FOR XML queries to generate

element-centric XML in SQL Server.

This is the.aspx application. It executes the stored procedure and returns XML in the browser:

```sql
CREATE
PROC GetSalesOrderInfo
AS
SELECT (
SELECT top 2 SalesOrderID, SalesPersonID, CustomerID,
(
select top 3 SalesOrderID, ProductID, OrderQty, UnitPrice from
Sales.SalesOrderDetail
WHERE
SalesOrderDetail.SalesOrderID = SalesOrderHeader.SalesOrderID
FOR
XML
AUTO
,
TYPE
)
FROM
Sales.SalesOrderHeader
WHERE
SalesOrderHeader.SalesOrderID = SalesOrder.SalesOrderID for xml auto
,
type
),
(
SELECT
*
FROM (
SELECT
SalesPersonID, EmployeeID
FROM
Sales.SalesPerson, HumanResources.Employee
WHERE
SalesPerson.SalesPersonID = Employee.EmployeeID)
As
SalesPerson
WHERE
SalesPerson.SalesPersonID = SalesOrder.SalesPersonID
FOR
XML
AUTO
,
TYPE
, ELEMENTS)
FROM (
SELECT
SalesOrderHeader.SalesOrderID, SalesOrderHeader.SalesPersonID
FROM
Sales.SalesOrderHeader, Sales.SalesPerson
WHERE
SalesOrderHeader.SalesPersonID = SalesPerson.SalesPersonID
) as
SalesOrder
ORDER
BY
SalesOrder.SalesOrderID
FOR
XML
AUTO
,
TYPE
GO
<%@LANGUAGE=C
# Debug=true %>
<%@import Namespace=
"System.Xml"
%>
<%@import namespace
=
"Microsoft.Data.SqlClient"
%><%
Response.Expires = -1;
Response.ContentType =
"text/xml"
;
```
