---
title: "Example: Querying XMLType Columns"
topic: "xml-data"
description: "The following query includes columns of type. The query retrieves product model ID, name, a"
tags: ["xml-data","example-querying-xmltype-columns"]
pubDate: "2025-12-01"
---

The following query includes columns of

type. The query retrieves product model ID,

name, and manufacturing steps at the first location from the

column of the

type.

The following is the result. The table stores manufacturing instructions for only some product

models. The manufacturing steps are returned as subelements of the

element in the result.

XML

If the query specifies a column name for the XML returned by the XQuery, as specified in the

following

statement, the manufacturing steps are wrapped in the element that has the

specified name.

```sql
Instructions
<ProductModelData>
SELECT
USE
AdventureWorks2022;
GO
SELECT
ProductModelID,
Name
,
Instructions.query(
'
declare namespace MI="http://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelManuInstructions";
/MI:root/MI:Location[1]/MI:step'
)
FROM
Production.ProductModel
FOR
XML
RAW (
'ProductModelData'
)
GO
<ProductModelData
ProductModelID
=
"5"
Name
=
"HL Mountain Frame"
/>
<ProductModelData
ProductModelID
=
"6"
Name
=
"HL Road Frame"
/>
<ProductModelData
ProductModelID
=
"7"
Name
=
"HL Touring Frame"
>
<MI:step>.
</MI:step>
<MI:step>.
</MI:step>
</ProductModelData>
USE
AdventureWorks2022;
GO
SELECT
ProductModelID,
Name
,
```
