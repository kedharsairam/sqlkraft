---
title: "Example: Specifying the ELEMENT Directive"
topic: "xml-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  This retrieves employee information and generates element-centric XML as shown in the

  follow
tags:
  - "xml-data"
  - "example-specifying-the-element-directive"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

This retrieves employee information and generates element-centric XML as shown in the

following:

XML

The query remains the same, except you add the

directive in the column names.

Therefore, instead of attributes, the

and

element children are added to the

element. Because the

column doesn't specify the

directive,

is added as the attribute of the

element.

SQL

This is the partial result.

XML

```sql
ELEMENT
<FName>
<LName>
<Name>
Employee!1!EmpID
ELEMENT
EmpID
<Employee>
<Employee
EmpID
=
...
>
<Name>
<FName>
...
</FName>
<LName>
...
</LName>
</Name>
</Employee>
SELECT
1
as
Tag,
NULL
as
Parent
,
E.BusinessEntityID
as
[Employee!1!EmpID],
NULL
as
[
Name
!2!FName!
ELEMENT
],
NULL
as
[
Name
!2!LName!
ELEMENT
]
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
UNION
ALL
SELECT
2
as
Tag,
1
as
Parent
,
E.BusinessEntityID,
FirstName,
LastName
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
ORDER
BY
[Employee!1!EmpID],[
Name
!2!FName!
ELEMENT
]
FOR
XML
EXPLICIT;
```
