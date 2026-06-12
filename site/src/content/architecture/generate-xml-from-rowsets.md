---
title: "Generate XML from rowsets"
topic: "xml-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  You can generate an

  data type instance from a rowset by using FOR XML with the new

  directiv
tags:
  - "xml-data"
  - "generate-xml-from-rowsets"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

You can generate an

data type instance from a rowset by using FOR XML with the new

directive.

The result can be assigned to an

data type column, variable, or parameter. Also, FOR XML

can be nested to generate any hierarchical structure. This makes nested FOR XML much more

convenient to write than FOR XML EXPLICIT, but it may not perform as well for deep

hierarchies. FOR XML also introduces a new PATH mode. This new mode specifies the path in

the XML tree where a column's value appears.

The new

directive can be used to define read-only XML views over relational

data with SQL syntax. The view can be queried with SQL statements and embedded XQuery, as

shown in the following example. You can also refer to these SQL views in stored procedures.

The following SQL view definition creates an XML view over a relational column, pk, and book

authors retrieved from an XML column:

The V view contains a single row with a single columnxmlVal of XML type

It can be queried

like a regular

data type instance. For example, the following query returns the author

whose first name is "David":

SQL view definitions are similar to XML views that are created by using annotated schemas.

However, there are important differences. The SQL view definition is read-only and must be

manipulated with embedded XQuery. The XML views are created by using annotated schema.

```sql.
CREATE
VIEW
V (xmlVal)
AS
SELECT pk, xCol.query(
'/book/author'
)
FROM
T
FOR
XML
AUTO
,
TYPE
;
SELECT xmlVal.query(
'//author[first-name = "David"]'
)
FROM
V;
```
