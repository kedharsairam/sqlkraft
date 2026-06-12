---
title: "Example: Retrieving Employee Information"
topic: "xml-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  This example retrieves an employee ID and employee name for each employee. In the

  database,
tags:
  - "xml-data"
  - "example-retrieving-employee-information"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

This example retrieves an employee ID and employee name for each employee. In the

database, the employeeID can be obtained from the BusinessEntityID

column in the Employee table. Employee names can be obtained from the Person table. The

BusinessEntityID column can be used to join the tables.

Assume that you want FOR XML EXPLICIT transformation to generate XML as shown in the

following sample:

XML

Because there are two levels in the hierarchy, you would write two

queries and apply

UNION ALL. This is the first query that retrieves values for the

element and its

attributes. The query assigns

as

value for the

element and NULL as

,

because it's the top-level element.

This is the second query. It retrieves values for the

element. It assigns

as

value

for the

element and

as

tag value identifying

as the parent.

```sql
AdventureWorks2025
SELECT
<Employee>
1
Tag
<Employee>
Parent
<Name>
2
Tag
<Name>
1
Parent
<Employee>
<Employee
EmpID
=
"1"
>
<Name
FName
=
"Ken"
LName
=
"Sánchez"
/>
</Employee>.
SELECT
1 as
Tag,
NULL as
Parent
,
E.BusinessEntityID
AS
[Employee!1!EmpID],
NULL as
[
Name
!2!FName],
NULL as
[
Name
!2!LName]
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
E.BusinessEntityID = P.BusinessEntityID;
SELECT
2 as
Tag,
1 as
Parent
,
E.BusinessEntityID,
FirstName,
LastName
FROM
HumanResources.Employee
AS
E
```
