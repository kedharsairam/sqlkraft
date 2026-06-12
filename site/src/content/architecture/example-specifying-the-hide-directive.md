---
title: "Example: Specifying the HIDE Directive"
topic: "xml-data"
description: "This example illustrates the use of the directive."
tags: ["xml-data","example-specifying-the-hide-directive"]
pubDate: 2025-12-01
---

This example illustrates the use of the

directive. This directive is useful when you want the

query to return an attribute for ordering the rows in the universal table that is returned by the

query, but you don't want that attribute in the final resulting XML document.

This query constructs this XML:

XML

This query generates the XML you want. The query identifies two column groups having 1 and

2 as Tag values in the column names.

This query uses the

query() Method (xml Data Type)

of the

data type to query the

CatalogDescription column of

type in order to retrieve the summary description. The query

also uses the

value() Method (xml Data Type)

of the

data type to retrieve the

ProductModelID value from the CatalogDescription column. This value isn't required in the

resulting XML, but is required to sort the resulting rowset. Therefore, the column name,

, includes the

directive. If this column isn't included in

the SELECT statement, you'll have to sort the rowset by

and

that is

type and you can't use the

type column in

ORDER BY. Therefore, the extra

column is added and is then

specified in the ORDER BY clause.

```sql
[Summary!2!ProductModelID!HIDE]
[ProductModel!1!ProdModelID]
[Summary!2!SummaryDescription]
[Summary!2!ProductModelID!HIDE]
<ProductModel
ProdModelID
=
"19"
Name
=
"Mountain-100"
>
<Summary>
<SummaryDescription>
<Summary>
element from XML stored in CatalogDescription column
</SummaryDescription>
</Summary>
</ProductModel>
USE
AdventureWorks2022;
GO
SELECT
1 as
Tag,
0 as
Parent
,
ProductModelID as
[ProductModel!1!ProdModelID],
Name as
[ProductModel!1!
Name
],
NULL as
[Summary!2!ProductModelID!hide],
NULL as
[Summary!2!SummaryDescription]
FROM
Production.ProductModel
WHERE
CatalogDescription is not null
```
