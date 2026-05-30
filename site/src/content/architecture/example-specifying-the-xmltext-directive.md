---
title: "Example: Specifying the XMLTEXT Directive"
topic: "xml-data"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  This example illustrates how data in the overflow column is addressed by using the

  directive in a

  sta
tags:
  - "xml-data"
  - "example-specifying-the-xmltext-directive"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

This example illustrates how data in the overflow column is addressed by using the

directive in a

statement using EXPLICIT mode.

Consider the

table. This table has an

column that stores the unconsumed part

of the XML document.

This query retrieves columns from the

table. For the

column,

AttributeName

isn't specified, but

directive

is set to

as part of providing a universal table column

name.

In the resulting XML document:

Because

AttributeName

isn't specified for the

column and the

directive

is specified, the attributes in the

element are appended to the attribute list of

the enclosing

element.

Because the

attribute in the

element conflicts with the

attribute retrieved on the same element level, the attribute in the

element is

```sql
SELECT
Person
Overflow
Person
Overflow
XMLTEXT
Overflow xmltext
<overflow>
<Parent>
PersonID
<xmltext>
PersonID
<xmltext>
USE tempdb;
GO
CREATE
TABLE
Person(PersonID varchar (5), PersonName varchar (20),
Overflow nvarchar (200));
GO
INSERT
INTO
Person
VALUES (
'P1'
,
'Joe'
,N
'<SomeTag attr1="data">content</SomeTag>'
)
,(
'P2'
,
'Joe'
,N
'<SomeTag attr2="data"/>'
)
,(
'P3'
,
'Joe'
,N
'<SomeTag attr3="data" PersonID="P">content</SomeTag>'
);
SELECT
1 as
Tag,
NULL as parent
,
PersonID as
[
Parent
!1!PersonID],
PersonName as
[
Parent
!1!PersonName],
Overflow as
[
Parent
!1!!XMLTEXT]
-- No AttributeName; XMLTEXT directive
FROM
Person
FOR
XML
EXPLICIT;
```
