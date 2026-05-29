---
title: "Generate an Inline XSD Schema"
topic: "xml-data"
description: |
  Article
  
  •
  
  10/17/2024
  
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  In a FOR XML clause, you can request that your query return an inline schema together with
  
  the query results. If you want an XDR s
tags:
  - "xml-data"
  - "generate-an-inline-xsd-schema"
pubDate: 2025-12-01
---

Article

•

10/17/2024

Applies to:

SQL Server

Azure SQL Database

In a FOR XML clause, you can request that your query return an inline schema together with

the query results. If you want an XDR schema, you use the XMLDATA keyword in the FOR XML

clause. If you want an XSD schema, you use the XMLSCHEMA keyword.

This article describes the XMLSCHEMA keyword and explains the structure of the resulting

inline XSD schema. Following are the limitations when you're requesting inline schemas:

You can specify XMLSCHEMA only in RAW and AUTO mode, not in EXPLICIT mode.

If a nested FOR XML query specifies the TYPE directive, the query result is of

type,

and this result is treated as an instance of untyped XML data. For more information, see

XML Data (SQL Server)

.

When you specify XMLSCHEMA in a FOR XML query, you receive both a schema and XML data,

the query result. Each top-level element of the data refers to the previous schema by using a

default namespace declaration that, in turn, refers to the target namespace of the inline

schema.

For example:

XML

```sql
<xsd:schema
targetNamespace
=
"urn:schemas-microsoft-com:sql:SqlRowSet1"
xmlns:schema
=
"urn:schemas-microsoft-com:sql:SqlRowSet1"
xmlns:xsd
=
"http://www.w3.org/2001/XMLSchema"
xmlns:sqltypes
=
"https://schemas.microsoft.com/sqlserver/2004/sqltypes"
elementFormDefault
=
"qualified"
>
<xsd:import
namespace
=
"https://schemas.microsoft.com/sqlserver/2004/sqltypes"
schemaLocation
=
"https://schemas.microsoft.com/sqlserver/2004/sqltypes/sqltypes.xsd
"
/>
<xsd:element
name
=
"Production.ProductModel"
>
<xsd:complexType>
<xsd:attribute
name
=
"ProductModelID"
type
=
"sqltypes:int"
use
=
"required"
/>
<xsd:attribute
name
=
"Name"
use
=
"required"
>
<xsd:simpleType
sqltypes:sqlTypeAlias
=
"[AdventureWorks2022].[dbo].[Name]"
>
<xsd:restriction
base
=
"sqltypes:nvarchar"
sqltypes:localeId
=
"1033"
sqltypes:sqlCompareOptions
=
"IgnoreCase IgnoreKanaType IgnoreWidth"
sqltypes:sqlSortId
=
"52"
>
<xsd:maxLength
value
=
"50"
/>
</xsd:restriction>
</xsd:simpleType>
</xsd:attribute>
</xsd:complexType>
</xsd:element>
```