---
name: "xquery-xqueries-involving-order"
title: "XQuery - XQueries Involving Order"
category: "xquery"
description: "XQuery Language Reference: XQueries Involving Order"
syntax: |
  SELECT
            Instructions.query(
            '
            declare namespace
            AWMI="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
            works/ProductModelManuInstructions";
            <ManuStep ProdModelID = "
            {sql:column("Production.ProductModel.ProductModelID")}"
            ProductModelName = "{ sql:column("Production.ProductModel.Name")
            }" >
            <Location>
            { (//AWMI:root/AWMI:Location)[2]/@* }
            <Steps>
            { for $s in (//AWMI:root/AWMI:Location)[2]//AWMI:step
            return
            <Step>
            { string($s) }
            </Step>
            }
            </Steps>
            </Location>
            </ManuStep>
            '
            )
            as
            Result
            FROM
            Production.ProductModel
            WHERE
            ProductModelID=7
tags: ["xquery","xqueries-involving-order"]
pubDate: 2025-12-01
---

Relational databases do not have a concept of sequence. For example, you cannot make a

request such as "Get the first customer from the database." However, you can query an XML

document and retrieve the first <Customer> element. Then, you will always retrieve the same

customer.

This topic illustrates queries based on the sequence in which nodes appear in the document.

For a specific product model, the following query retrieves manufacturing steps at the second

work center location in a sequence of work center locations in the manufacturing process.

```sql
SELECT
Instructions.query(
'
declare namespace
AWMI="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelManuInstructions";
<ManuStep ProdModelID = "
{sql:column("Production.ProductModel.ProductModelID")}"
ProductModelName = "{ sql:column("Production.ProductModel.Name")
}" >
<Location>
{ (//AWMI:root/AWMI:Location)[2]/@* }
<Steps>
{ for $s in (//AWMI:root/AWMI:Location)[2]//AWMI:step return
<Step>
{ string($s) }
</Step>
}
</Steps>
</Location>
</ManuStep>
'
) as
Result
FROM
Production.ProductModel
WHERE
ProductModelID=7
```
