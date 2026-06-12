---
name: "Complex PIVOT example"
title: "Complex PIVOT example"
category: "queries"
description: ""
tags: ["tsql","queries"]
pubDate: "2026-05-29"
---

The following code displays the same result, pivoted so that the

values

become the column headings. A column is provided for three (

) days, even though the

results are.

Here's the result set.

A common scenario where

can be useful is when you want to generate cross-tabulation

reports to give a summary of the data. For example, suppose you want to query the

table in the

sample database to determine the

number of purchase orders placed by certain employees. The following query provides this

report, ordered by vendor.

#### Output

Here's a partial result set.

The results returned by this subselect statement are pivoted on the

column.

The unique values returned by the

column become fields in the final result set. As

such, there's a column for each

number specified in the pivot clause, which are

employees

,

,

,

, and

in this example. The

column serves

as the value column, against which the columns returned in the final output, which are called

the grouping columns, are grouped. In this case, the grouping columns are aggregated by the

function. A warning message appears that indicates that any null values appearing in the

column weren't considered when computing the

for each employee.

）

Important

`DaysToManufacture`

```sql
[3]
```

`NULL`

`PIVOT`

`PurchaseOrderHeader`

`AdventureWorks2025`

```sql
-- Pivot table with one row and five columns
SELECT
'AverageCost'
AS
CostSortedByProductionDays,
[0], [1], [2], [3], [4]
FROM (
SELECT
DaysToManufacture,
StandardCost
FROM
Production.Product
)
AS
SourceTable
PIVOT (
AVG (StandardCost)
FOR
DaysToManufacture
IN ([0], [1], [2], [3], [4])
)
AS
PivotTable;
CostSortedByProductionDays 0 1 2 3 4
--------------------------- ----------- ----------- ----------- ----------- -------
----
AverageCost 5.0885 223.88 359.1082 NULL
949.4105
```

```sql
USE
AdventureWorks2022;
GO
SELECT
VendorID,
[250]
AS
Emp1,
[251]
AS
Emp2,
[256]
AS
Emp3,
[257]
AS
Emp4,
```

`EmployeeID`

`EmployeeID`

`EmployeeID`

```sql
250
```

```sql
251
```

```sql
256
```

```sql
257
```

```sql
260
```

`PurchaseOrderID`

`COUNT`

`PurchaseOrderID`

`COUNT`

```sql
[260]
AS
Emp5
FROM (
SELECT
PurchaseOrderID,
EmployeeID, VendorID
FROM
Purchasing.PurchaseOrderHeader
) p
PIVOT (
COUNT (PurchaseOrderID)
FOR
EmployeeID
IN ([250], [251], [256], [257], [260])
)
AS pvt
ORDER
BY pvt.VendorID;
VendorID Emp1 Emp2 Emp3 Emp4 Emp5
----------- ----------- ----------- ----------- ----------- -----------
1492 2 5 4 4 4
1494 2 5 4 5 4
1496 2 4 4 5 5
1498 2 5 4 4 4
1500 3 4 4 5 4
SELECT
PurchaseOrderID,
EmployeeID,
VendorID
FROM
PurchaseOrderHeader;
```
