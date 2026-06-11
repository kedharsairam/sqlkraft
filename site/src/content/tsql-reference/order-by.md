---
name: "ORDER BY"
title: "ORDER BY"
category: "queries"
description: ""
tags: ["tsql", "queries"]
pubDate: 2026-05-29
---

The order of certain parameters used with the

clause is important. The following

example shows the incorrect and correct use of

in two

statements where you

rename a column in the output.

`UNION`

`UNION`

`SELECT`

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
/* INCORRECT */
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
ORDER
BY
Name
UNION
SELECT
ProductModelID,
Name
FROM dbo.Gloves;
GO
/* CORRECT */
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
SELECT
ProductModelID,
Name
FROM dbo.Gloves
```
