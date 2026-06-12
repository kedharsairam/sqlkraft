---
name: "O. Use the UNION query hint"
title: "O. Use the UNION query hint"
category: "statements"
description: ""
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

The following example shows how the

clause is used with a

clause.

The following example uses the

query hint.

```sql
OPTION (GROUP)
```

```sql
GROUP BY
```

```sql
MERGE UNION
```

```sql
USE
AdventureWorks2025;
GO
SELECT pp.FirstName,
pp.LastName,
e.NationalIDNumber
FROM
HumanResources.Employee
AS e
WITH (
INDEX (AK_Employee_NationalIDNumber))
INNER
JOIN
Person.Person
AS pp
ON e.BusinessEntityID = pp.BusinessEntityID
WHERE
LastName =
'Johnson'
;
GO
-- Force a table scan by using INDEX = 0.
USE
AdventureWorks2025;
GO
SELECT pp.LastName,
pp.FirstName,
e.JobTitle
FROM
HumanResources.Employee
AS e
WITH (
INDEX
= 0)
INNER
JOIN
Person.Person
AS pp
ON e.BusinessEntityID = pp.BusinessEntityID
WHERE
LastName =
'Johnson'
;
GO
```

```sql
USE
AdventureWorks2025;
GO
SELECT
ProductID, OrderQty,
SUM (LineTotal)
AS
Total
FROM
Sales.SalesOrderDetail
WHERE
UnitPrice < $5.00
GROUP
BY
ProductID, OrderQty
ORDER
BY
ProductID, OrderQty
OPTION (
HASH
GROUP
,
FAST
10);
GO
```
