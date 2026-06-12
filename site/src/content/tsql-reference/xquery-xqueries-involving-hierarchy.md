---
name: "xquery-xqueries-involving-hierarchy"
title: "XQuery - XQueries Involving Hierarchy"
category: "xquery"
description: "XQuery Language Reference: XQueries Involving Hierarchy"
syntax: "ManuInstr"
tags: ["xquery","xqueries-involving-hierarchy"]
pubDate: "2025-12-01"
---

Most

type columns in the

database are semi-structured documents.

Therefore, documents stored in each row may look different. The query samples in this topic

illustrate how to extract information from these various documents.

For product model 7, the query constructs XML that includes the <

> element, with

and

attributes, and one or more <

> child

elements.

Each <

> element has its own set of attributes and one <

> child element. This

<

> child element is the first manufacturing step at the work center location.

```sql
ManuInstr
Location
Location step step
SELECT
Instructions.query(
'
declare namespace
AWMI="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelManuInstructions";
\<ManuInstr ProdModelID = "
{sql:column("Production.ProductModel.ProductModelID") }"
ProductModelName = "{ sql:column("Production.ProductModel.Name")
}" >
{
for $wc in //AWMI:root/AWMI:Location return
<Location>
{$wc/@* }
<step1> { string( ($wc//AWMI:step)[1] ) } </step1>
</Location>
}
</ManuInstr>
'
) as
Result
FROM
Production.ProductModel
WHERE
ProductModelID=7
```
