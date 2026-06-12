---
name: "Q. Use SELECT INTO with UNION"
title: "Q. Use SELECT INTO with UNION"
category: "statements"
description: ""
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

In the following example, the

clause in the second

statement specifies that the

table named

holds the final result set of the union of the designated columns

of the

and

tables. The

table is created in the first

statement.

`INTO`

`SELECT`

`ProductResults`

`ProductModel`

`Gloves`

`Gloves`

`SELECT`

```sql
SELECT
ProductModelID,
Name
FROM dbo.Gloves
ORDER
BY
Name
;
GO
```

```sql
USE
AdventureWorks2025;
GO
IF OBJECT_ID('dbo.ProductResults', 'U') IS NOT NULL
DROP
TABLE dbo.ProductResults;
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
USE
AdventureWorks2025;
GO
SELECT
ProductModelID,
Name
INTO dbo.ProductResults
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
FROM dbo.Gloves;
GO
SELECT
ProductModelID,
Name
FROM dbo.ProductResults;
```
