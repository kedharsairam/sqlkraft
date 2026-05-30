---
title: "Example: Requesting Schemas as Results with the XMLDATA & XMLSCHEMA Options"
topic: "xml-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The following query returns the XML-DATA schema that describes the document structure.

  SQL

tags:
  - "xml-data"
  - "example-requesting-schemas-as-results-with-the-xmldata-xmlschema-options"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The following query returns the XML-DATA schema that describes the document structure.

This is the result:

XML

By specifying the

option, you can request the XSD schema for the result.

７

Note

The

is declared as a namespace. To avoid namespace collisions when multiple

XML-Data schemas are requested in different FOR XML queries, the namespace identifier,

in this example, changes with every query execution. The namespace identifier is

made up of

where

is an integer.

```sql
XMLSCHEMA
USE
AdventureWorks2022;
GO
SELECT
ProductModelID,
Name
FROM
Production.ProductModel
WHERE
ProductModelID
IN (122, 119)
FOR
XML
RAW
, XMLDATA;
GO
<Schema name
=
"Schema1"
xmlns
=
"urn:schemas-microsoft-com:xml-data"
xmlns:dt
=
"urn:schemas-microsoft-com:datatypes"
>
<ElementType name
=
"row"
content
=
"empty"
model
=
"closed"
>
<AttributeType name
=
"ProductModelID"
dt:type
=
"i4"
/>
<AttributeType name
=
"Name"
dt:type
=
"string"
/>
<attribute type
=
"ProductModelID"
/>
<attribute type
=
"Name"
/>
</ElementType>
</Schema>
<row xmlns
=
"x-schema:#Schema1"
ProductModelID
=
"122"
Name
=
"All-Purpose Bike Stand"
/>
<row xmlns
=
"x-schema:#Schema1"
ProductModelID
=
"119"
Name
=
"Bike Wash"
/>
<Schema>
Schema1
```
