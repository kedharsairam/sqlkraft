---
title: "Columns with a Name Specified as a Wildcard Character"
topic: "xml-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  If the column name specified is a wildcard character (*), the content of that column is inser
tags:
  - "xml-data"
  - "columns-with-a-name-specified-as-a-wildcard-character"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

If the column name specified is a wildcard character (\*), the content of that column is inserted

as if there's no column name specified. If this column is a non-

type column, the column

content is inserted as a text node, as shown in the following example:

This is the result:

XML

If the column is of

type, the corresponding XML tree is inserted. For example, the following

query specifies "\*" for the column name that contains the XML returned by the XQuery against

the Instructions column.

```sql
USE
AdventureWorks2022;
GO
SELECT
E.BusinessEntityID
"@EmpID"
,
FirstName
"*"
,
MiddleName
"*"
,
LastName
"*"
FROM
HumanResources.Employee
AS
E
INNER
JOIN
Person.Person
AS
P
ON
E.BusinessEntityID = P.BusinessEntityID
WHERE
E.BusinessEntityID=1
FOR
XML
PATH
;
<row
EmpID
=
"1"
>
KenJSánchez
</row>
SELECT
ProductModelID,
Name
,
Instructions.query(
'declare namespace
MI="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelManuInstructions"
/MI:root/MI:Location
'
) as
"*"
FROM
Production.ProductModel
WHERE
ProductModelID=7
FOR
XML
PATH
;
```
