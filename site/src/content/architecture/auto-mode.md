---
title: "AUTO Mode"
topic: "xml-data"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  As described in

  FOR XML (SQL Server)

  , AUTO mode returns query results as nested XML

  elements. This
tags:
  - "xml-data"
  - "auto-mode"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

As described in

FOR XML (SQL Server)

, AUTO mode returns query results as nested XML

elements. This doesn't provide much control over the shape of the XML generated from a

query result. The AUTO mode queries are useful if you want to generate simple hierarchies.

However,

Use EXPLICIT Mode with FOR XML

and

Use PATH Mode with FOR XML

provide more

control and flexibility in deciding the shape of the XML from a query result.

Each table in the FROM clause, from which at least one column is listed in the SELECT clause, is

represented as an XML element. The columns listed in the SELECT clause are mapped to

attributes or subelements, if the optional ELEMENTS option is specified in the FOR XML clause.

The XML hierarchy, nesting of the elements, in the resulting XML is based on the order of

tables identified by the columns specified in the SELECT clause. Therefore, the order in which

column names are specified in the SELECT clause is significant. The first, leftmost table that is

identified forms the top element in the resulting XML document. The second leftmost table,

identified by columns in the SELECT statement, forms a subelement within the top element,

and so on.

If a column name listed in the SELECT clause is from a table that is already identified by a

previously specified column in the SELECT clause, the column is added as an attribute of the

element already created, instead of opening a new level of hierarchy. If the ELEMENTS option is

specified, the column is added as an attribute.

For example, execute this query:

SQL

This is the partial result:

XML

```sql
SELECT
Cust.CustomerID,
OrderHeader.CustomerID,
OrderHeader.SalesOrderID,
OrderHeader.Status,
Cust.CustomerType
FROM
Sales.Customer Cust, Sales.SalesOrderHeader OrderHeader
WHERE
Cust.CustomerID = OrderHeader.CustomerID
ORDER
BY
Cust.CustomerID
FOR
XML
AUTO
;
```
