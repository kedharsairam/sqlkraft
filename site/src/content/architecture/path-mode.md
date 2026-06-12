---
title: "PATH Mode"
topic: "xml-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  As described in

  FOR XML (SQL Server)

  , the

  mode provides a simpler way to mix elements

  an
tags:
  - "xml-data"
  - "path-mode"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

As described in

FOR XML (SQL Server)

, the

mode provides a simpler way to mix elements

and attributes.

mode is also a simpler way to introduce more nesting for representing

complex properties. You can use

mode queries to construct such XML from a

rowset, but the

mode provides a simpler alternative to the potentially cumbersome

mode queries.

mode, together with the ability to write nested

queries

and the

directive to return

type instances, allows you to write queries with less

complexity.

In

mode, column names or column aliases are treated as XPath expressions. These

expressions indicate how the values are being mapped to XML. Each XPath expression is a

relative XPath that provides the item type. Types include the attribute, element, scalar value,

and the name and hierarchy of the node that is generated, relative to the row element.

This section describes mapping columns in a rowset under various conditions, and provides

examples.

Columns without a name

Columns with a name

Columns with a name specified as a wildcard character

Columns with the name of an XPath node test

Column names with the path specified as data()

Columns that contain a null value by default

Namespace support in PATH mode

Examples: Use PATH mode

Add namespaces to queries using WITH XMLNAMESPACES

SELECT (Transact-SQL)

FOR XML (SQL Server)

```sql
PATH
PATH
FOR XML EXPLICIT
PATH
EXPLICIT
PATH
FOR XML
TYPE
PATH
```
