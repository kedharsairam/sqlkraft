---
title: "Columns without a Name"
topic: "xml-data"
description: "Any column without a name will be inlined."
tags: ["xml-data","columns-without-a-name"]
pubDate: "2025-12-01"
---

Any column without a name will be inlined. For example, computed columns or nested scalar

queries that don't specify column alias will generate columns without any name. If the column

is of

type, the content of that data type instance is inserted. Otherwise, the column content

is inserted as a text node.

Produce this XML. By default, for each row in the rowset, a

element is generated in the

resulting XML. This is the same as RAW mode.

The following query returns a three-column rowset. The third column without a name has XML

data. The PATH mode inserts an instance of the xml type.

This is the partial result:

XML

```sql
<row>
<row>4</row>
SELECT
2 + 2
FOR
XML
PATH
;
USE
AdventureWorks2022;
GO
SELECT
ProductModelID,
Name
,
Instructions.query(
'declare namespace
MI="http://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelManuInstructions";
/MI:root/MI:Location
'
)
FROM
Production.ProductModel
WHERE
ProductModelID=7
FOR
XML
PATH
;
GO
<row>
<ProductModelID>
7
</ProductModelID>
<Name>
HL Touring Frame
</Name>
<MI:Location.LocationID
=
"10".
></MI:Location>
```
