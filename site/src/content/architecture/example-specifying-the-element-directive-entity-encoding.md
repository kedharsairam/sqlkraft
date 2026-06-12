---
title: "Example: Specifying the ELEMENT Directive & Entity Encoding"
topic: "xml-data"
description: "This example illustrates the difference between the and directives. The directive entitize"
tags: ["xml-data","example-specifying-the-element-directive-entity-encoding"]
pubDate: 2025-12-01
---

This example illustrates the difference between the

and

directives. The

directive entitizes the data, but the

directive doesn't. The

element is

assigned XML,

, in the query.

Consider this query:

This is the result. The summary description is entitized in the result.

XML

Now, if you specify the

directive in the column name,

,

instead of the

directive, you'll receive the summary description without entitization.

```sql
<Summary>
<Summary>This is summary description</Summary>
Summary!2!SummaryDescription!XML
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
[Summary!2!SummaryDescription!
ELEMENT
]
FROM
Production.ProductModel
WHERE
ProductModelID=19
UNION
ALL
SELECT
2 as
Tag,
1 as
Parent
,
ProductModelID,
NULL
,
'<Summary>This is summary description</Summary>'
FROM
Production.ProductModel
WHERE
ProductModelID = 19
FOR
XML
EXPLICIT;
<ProductModel
ProdModelID
=
"19"
Name
=
"Mountain-100"
>
<Summary>
<SummaryDescription><Summary>
This is summary description
</Summary>
</SummaryDescription>
</Summary>
</ProductModel>
```
