---
name: "Basic PIVOT example"
title: "Basic PIVOT example"
category: "queries"
description: ""
tags: ["tsql","queries"]
pubDate: "2026-05-29"
---

In Microsoft Fabric and Azure Synapse Analytics pools, queries with

operator fail if

there's a

on the nonpivot column output by. As a workaround, remove

the nonpivot column from the. Query results are the same, as this

clause is a duplicate.

Column names are of type

or. Because

projects column

names as values, the data type for an

column will also be

, which is

not a supported data type in Fabric Data Warehouse. If you want to save the results of

to a table in a warehouse in Fabric, cast it to a

supported data type in Fabric Data

Warehouse. For example:

The following code example produces a two-column table that has four rows.

Here's the result set.

No products are defined with a value of

for.

#### Output

`PIVOT`

```sql
GROUP BY
```

`PIVOT`

```sql
GROUP BY
```

```sql
GROUP BY
```

`UNPIVOT`

`UNPIVOT`

`UNPIVOT`

```sql
3
```

`DaysToManufacture`

```sql
CREATE
TABLE myTable
AS
SELECT value
,
CAST (columnNames as
VARCHAR (128) ) columnNames
FROM myTableToUnpivot
UNPIVOT (
value
FOR columnNames
IN ( col1, col2 )) unpvt;
```

```sql
USE
AdventureWorks2022;
GO
SELECT
DaysToManufacture,
AVG (StandardCost)
AS
AverageCost
FROM
Production.Product
GROUP
BY
DaysToManufacture;
DaysToManufacture AverageCost
------------------ ------------
0 5.0885
1 223.88
2 359.1082
4 949.4105
```
