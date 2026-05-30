---
title: "Reference"
topic: "xml-data"
description: |
  Article

  •

  11/01/2023

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  Every database you create has a predefined

  XML schema collection in the

  relational

  schema. It reserv
tags:
  - "xml-data"
  - "reference"
pubDate: 2025-12-01
---

Article

•

11/01/2023

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Every database you create has a predefined

XML schema collection in the

relational

schema. It reserves these predefined schemas, and they can be accessed from any other user-

created XML schema collection. The prefixes used in these predefined schemas are meaningful

in XQuery. Only

is a reserved prefix.

XML

The

sqltypes

namespace contains components that can be referenced from any user-created

XML schema collection. You can download the

sqltypes

schema from this

Microsoft Web

site

. The built-in components include the following:

XSD types

XML attributes

,

, and

Components of the

sqltypes

namespace

The following query returns built-in components that can be referenced from a user-created

XML schema collection:

```sql
xml = http://www.w3.org/XML/1998/namespace xs = http://www.w3.org/2001/XMLSchema xsi = http://www.w3.org/2001/XMLSchema-instance fn = http://www.w3.org/2004/07/xpath-functions sqltypes = https://schemas.microsoft.com/sqlserver/2004/sqltypes xdt = http://www.w3.org/2004/07/xpath-datatypes (no prefix) = urn:schemas-microsoft-com:xml-sql (no prefix) = https://schemas.microsoft.com/sqlserver/2004/SOAP
SELECT
C.name, N.name, C.symbol_space_desc from sys.xml_schema_components C join sys.xml_schema_namespaces N on ((C.xml_namespace_id = N.xml_namespace_id)
AND (C.xml_collection_id =
N.xml_collection_id)) join sys.xml_schema_collections SC on
SC.xml_collection_id = C.xml_collection_id where ((C.xml_collection_id = 1)
AND (C.name is not null
)
AND (C.scoping_xml_component_id is null
)
```
