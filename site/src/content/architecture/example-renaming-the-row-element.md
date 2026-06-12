---
title: "Example: Renaming the <row> Element"
topic: "xml-data"
description: "For each row in the result set, the RAW mode generates an element ."
tags: ["xml-data","example-renaming-the-row-element"]
pubDate: "2025-12-01"
---

For each row in the result set, the RAW mode generates an element. You can optionally

specify another name for this element by specifying an optional argument to the RAW mode,

as shown in this query. The query returns a

element for each row in the rowset.

This is the result. Because the

directive is added in the query, the result is element-

centric.

XML

Use RAW Mode with FOR XML

```sql
<row>
<ProductModel>
ELEMENTS
SELECT
ProductModelID,
Name
FROM
Production.ProductModel
WHERE
ProductModelID = 122
FOR
XML
RAW (
'ProductModel'
), ELEMENTS;
GO
<ProductModel>
<ProductModelID>
122
</ProductModelID>
<Name>
All-Purpose Bike Stand
</Name>
</ProductModel>
```
