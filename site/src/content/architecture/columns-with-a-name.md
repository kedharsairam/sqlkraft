---
title: "Columns with a Name"
topic: "xml-data"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  The following are the specific conditions in which rowset columns with a name are mapped,

  case-sensiti
tags:
  - "xml-data"
  - "columns-with-a-name"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

The following are the specific conditions in which rowset columns with a name are mapped,

case-sensitive, to the resulting XML:

The column name starts with an at sign (

).

The column name doesn't start with an at sign (

).

The column name doesn't start with an at sign (

) and contains a slash mark (

).

Several columns share the same prefix.

One column has a different name.

If the column name starts with an at sign (

) and doesn't contain a slash mark (

), an attribute

of the

element that has the corresponding column value is created. For example, the

following query returns a two-column (

) rowset. In the resulting XML, a

attribute is added to the corresponding

element and a value of

is assigned

to it.

SQL

This is the result:

XML

Attributes must come before any other node types, such as element nodes and text nodes, in

the same level. The following query will return an error:

```sql
@
@
@
/
@
/
row
@PmId, Name
PmId
row
ProductModelID
SELECT
ProductModelID
as
"@PmId"
,
Name
FROM
Production.ProductModel
WHERE
ProductModelID = 7
FOR
XML
PATH
;
<row
PmId
=
"7"
>
<Name>
HL Touring Frame
</Name>
</row>
```
