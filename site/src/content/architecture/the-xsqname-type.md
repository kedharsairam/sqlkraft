---
title: "The xs:QName Type"
topic: "xml-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  SQL Server doesn't support types derived from

  by the use of an XML schema

  restriction eleme
tags:
  - "xml-data"
  - "the-xsqname-type"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

doesn't support types derived from

by the use of an XML schema

restriction element. Also, SQL Server currently doesn't support union types with

as a

member type.

The following

statements can't load the XML schema, because

they specify the

type as a member type of the union:

Both statements fail with an error.

Requirements and Limitations for XML Schema Collections on the Server

```sql
CREATE XML SCHEMA COLLECTION xs:QName
CREATE
XML
SCHEMA
COLLECTION QNameLimitation1
AS
N
'
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
<xs:simpleType name="myUnion">
<xs:union memberTypes="xs:int xs:QName"/>
</xs:simpleType>
</xs:schema>'
;
GO
CREATE
XML
SCHEMA
COLLECTION QNameLimitation2
AS
N
'
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
<xs:simpleType name="myUnion">
<xs:union memberTypes="xs:integer">
<xs:simpleType>
<xs:list itemType="xs:QName"/>
</xs:simpleType>
</xs:union>
</xs:simpleType>
</xs:schema>'
;
GO
```
