---
name: "P. Use a UNION"
title: "P. Use a UNION"
category: "statements"
description: "In the following example, the result set includes the contents of the"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

In the following example, the result set includes the contents of the

and

columns of both the

and

tables.

`ProductModelID`

`Name`

`ProductModel`

`Gloves`

```sql
USE
AdventureWorks2025;
GO
SELECT
BusinessEntityID,
JobTitle,
HireDate,
VacationHours,
SickLeaveHours
FROM
HumanResources.Employee
AS e1
UNION
SELECT
BusinessEntityID,
JobTitle,
HireDate,
VacationHours,
SickLeaveHours
FROM
HumanResources.Employee
AS e2
OPTION (
MERGE
UNION
);
GO
```

```sql
USE
AdventureWorks2025;
GO
IF OBJECT_ID('dbo.Gloves', 'U') IS NOT NULL
DROP
TABLE dbo.Gloves;
GO
-- Create Gloves table.
SELECT
ProductModelID,
Name
INTO dbo.Gloves
FROM
Production.ProductModel
WHERE
ProductModelID
IN (3, 4);
GO
-- Here is the simple union.
USE
AdventureWorks2025;
GO
SELECT
ProductModelID,
Name
FROM
Production.ProductModel
WHERE
ProductModelID
NOT
IN (3, 4)
UNION
```
