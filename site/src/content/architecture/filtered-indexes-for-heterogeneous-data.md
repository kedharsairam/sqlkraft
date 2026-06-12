---
title: "Filtered indexes for heterogeneous data"
topic: "index-architecture"
description: "is valid for the following query."
tags: ["index-architecture","architecture"]
pubDate: 2026-05-29
---

The filtered index

is valid for the following query.

Display the

Estimated Execution Plan

to determine if the query optimizer used the filtered index.

For more information about how to create filtered indexes and how to define the filtered index

predicate expression, see

Create filtered indexes.

When a table has heterogeneous data rows, you can create a filtered index for one or more

categories of data.

For example, the products listed in the

table are each assigned to a

, which are in turn associated with the product categories Bikes,

Components, Clothing, or Accessories. These categories are heterogeneous because their

column values in the

table aren't closely correlated. For example, the

columns

,

,

,

,

, and

have unique

characteristics for each product category. Suppose that there are frequent queries for

accessories, which have subcategories between 27 and 36 inclusive. You can improve the

performance of queries for accessories by creating a filtered index on the accessories

subcategories as shown in the following example.

`FIBillOfMaterialsWithEndDate`

`Production.Product`

`ProductSubcategoryID`

`Production.Product`

`Color`

`ReorderPoint`

`ListPrice`

`Weight`

`Class`

`Style`

```sql
CREATE
NONCLUSTERED
INDEX
FIBillOfMaterialsWithEndDate
ON
Production.BillOfMaterials (ComponentID, StartDate)
WHERE
EndDate
IS
NOT
NULL
;
SELECT
ProductAssemblyID,
ComponentID,
StartDate
FROM
Production.BillOfMaterials
WHERE
EndDate
IS
NOT
NULL
AND
ComponentID = 5
AND
StartDate >
'20080101'
;
```

```sql
CREATE
NONCLUSTERED
INDEX
FIProductAccessories
ON
Production.Product (ProductSubcategoryID, ListPrice)
INCLUDE (
Name
)
WHERE
ProductSubcategoryID >= 27
AND
ProductSubcategoryID <= 36;
```
