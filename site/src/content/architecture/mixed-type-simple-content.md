---
title: "Mixed type & simple content"
topic: "xml-data"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  SQL Server doesn't support restricting a mixed type to a simple content.
  
  In the following XM
tags:
  - "xml-data"
  - "mixed-type-simple-content"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

SQL Server doesn't support restricting a mixed type to a simple content.

In the following XML schema collection,

is a complex type that can be emptied.

That is, both its elements have

set to 0. The attempt to restrict this to a simple

content, as in the

declaration, isn't supported. Therefore, the following XML

schema collection creation fails:

SQL

Requirements and Limitations for XML Schema Collections on the Server

```sql
myComplexTypeA
minOccurs
myComplexTypeB
CREATE
XML
SCHEMA
COLLECTION SC
AS
'
<schema xmlns="http://www.w3.org/2001/XMLSchema" targetNamespace="http://ns"
xmlns:ns="http://ns"
xmlns:ns1="http://ns1">
<complexType name="myComplexTypeA" mixed="true">
<sequence>
<element name="a" type="string" minOccurs="0"/>
<element name="b" type="string" minOccurs="0" maxOccurs="23"/>
</sequence>
</complexType>
<complexType name="myComplexTypeB">
<simpleContent>
<restriction base="ns:myComplexTypeA">
<simpleType>
<restriction base="int">
<minExclusive value="25"/>
</restriction>
</simpleType>
</restriction>
</simpleContent>
</complexType>
</schema>
'
;
GO
```