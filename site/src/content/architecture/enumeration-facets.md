---
title: "Enumeration Facets"
topic: "xml-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  SQL Server rejects XML schemas with types that have pattern facets or enumerations that

  viol
tags:
  - "xml-data"
  - "enumeration-facets"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

SQL Server rejects XML schemas with types that have pattern facets or enumerations that

violate those facets.

The following schema would be rejected, because the featured enumeration value includes a

mixed-case value. It would also be rejected because this value violates the pattern value that

limits values to only lowercase letters.

SQL

Requirements and Limitations for XML Schema Collections on the Server

Last updated on 11/18/2025

```sql
CREATE
XML
SCHEMA
COLLECTION MySampleCollection
AS
'
<schema xmlns="http://www.w3.org/2001/XMLSchema" targetNamespace="http://ns"
xmlns:ns="http://ns">
<simpleType name="MyST">
<restriction base="string">
<pattern value="[a-z]*"/>
</restriction>
</simpleType>
<simpleType name="MyST2">
<restriction base="ns:MyST">
<enumeration value="mYstring"/>
</restriction>
</simpleType>
</schema>'
;
GO
```
