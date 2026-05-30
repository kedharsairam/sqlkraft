---
title: "xml Data Type"
topic: "xml-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  If a

  query specifies a column of

  type in the

  clause, column values are

  mapped as elements
tags:
  - "xml-data"
  - "xml-data-type"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

If a

query specifies a column of

type in the

clause, column values are

mapped as elements in the returned XML, regardless of whether you specify the

directive. Any XML declaration in the

type column isn't serialized.

For example, the following query retrieves customer contact information such as the

,

, and

columns, and the telephone numbers from the

column of

type.

Because the query doesn't specify the

directive, the column values are returned as

attributes, except for the extra contact information values retrieved from the

type column.

These are returned as elements.

This is the partial result:

XML

```sql
FOR XML
SELECT
ELEMENTS
BusinessEntityID
FirstName
LastName
AdditionalContactInfo
ELEMENTS
USE
AdventureWorks2022;
GO
SELECT
BusinessEntityID,
FirstName,
LastName,
AdditionalContactInfo.query(
'
declare namespace act="http://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ContactTypes";
//act:telephoneNumber/act:number
'
)
AS
PhoneNumber
FROM
Person.Person
WHERE
AdditionalContactInfo.query(
'
declare namespace act="http://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ContactTypes";
//act:telephoneNumber/act:number
'
)
IS
NOT
NULL
FOR
XML
AUTO
,
TYPE
;
<Person.Person
BusinessEntityID
=
"291"
FirstName
=
"Gustavo"
LastName
=
"Achong"
>
<PhoneNumber>
<act:number xmlns:act
=
"https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ContactTypes"
>
425-555-1112
</act:number>
<act:number xmlns:act
=
"https://schemas.microsoft.com/sqlserver/2004/07/adventure-
```
