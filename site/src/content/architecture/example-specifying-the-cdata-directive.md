---
title: "Example: Specifying the CDATA Directive"
topic: "xml-data"
description: "If the directive is set to , the contained data isn't entity encoded, but is put in the CDAT"
tags: ["xml-data","example-specifying-the-cdata-directive"]
pubDate: "2025-12-01"
---

If the directive is set to

, the contained data isn't entity encoded, but is put in the CDATA

section. The

attributes must be nameless.

The following query wraps the product model summary description in a CDATA section.

This is the result:

XML

Use EXPLICIT Mode with FOR XML

```sql
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
'<Summary>This is summary description</Summary>'
as
[ProductModel!1!!CDATA]
-- no attribute name so ELEMENT assumed
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
<![CDATA[<Summary>This is summary description</Summary>]]>
</ProductModel>
```
