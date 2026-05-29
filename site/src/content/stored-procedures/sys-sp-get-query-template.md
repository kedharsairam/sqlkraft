---
name: 'sys.sp_get_query_template'
title: 'sp_get_query_template'
category: 'general'
description: 'Returns the parameterized form of a query. The results returned mimic the parameterized form of a query that results from using forced parameterization. Transact-SQL syntax conventions The query for which the parameterized version is to be generated. , and must be enclosed in single quotation marks and be preceded by the , provided as indicated, to receive the Arguments for extended stored procedu'
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: 'sp_get_query_template'
---

## Description

Returns the parameterized form of a query. The results returned mimic the parameterized form of a query that results from using forced parameterization. Transact-SQL syntax conventions The query for which the parameterized version is to be generated. , and must be enclosed in single quotation marks and be preceded by the , provided as indicated, to receive the Arguments for extended stored procedures must be entered in the specific order as

## Syntax

```sql
sp_get_query_template
```

## Examples

### Example 1

```sql
sp_get_query_template
```

### Example 2

```sql
NULL
```

### Example 3

```sql
sp_get_query_template
```

### Example 4

```sql
USE
AdventureWorks2022;
GO
DECLARE
@my_templatetext
AS
NVARCHAR
(
MAX
);
DECLARE
@my_parameters
AS
NVARCHAR
(
MAX
);
EXECUTE
sp_get_query_template N
'SELECT pi.ProductID, SUM(pi.Quantity) AS Total
FROM Production.ProductModel pm
INNER JOIN Production.ProductInventory pi
ON pm.ProductModelID = pi.ProductID
WHERE pi.ProductID = 2
GROUP BY pi.ProductID, pi.Quantity
HAVING SUM(pi.Quantity) > 400'
,
@my_templatetext
OUTPUT
,
@my_parameters
OUTPUT
;
SELECT
@my_templatetext;
SELECT
@my_parameters;
```
