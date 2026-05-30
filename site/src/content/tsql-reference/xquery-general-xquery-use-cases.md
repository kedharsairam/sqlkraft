---
name: "xquery-general-xquery-use-cases"
title: "XQuery - General XQuery Use Cases"
category: "xquery"
description: "XQuery Language Reference: General XQuery Use Cases"
syntax: "namespace"
tags:
  - "xquery"
  - "general-xquery-use-cases"
pubDate: 2025-12-01
---

09/29/2025

Applies to:

SQL Server

This article provides general examples of XQuery use.

The following query returns the product model IDs and weights, if they exist, from the product

catalog description. The query constructs XML that has the following form:

XML

Here's the query:

Note the following considerations from the previous query:

The

keyword in the XQuery prolog defines a namespace prefix that is used in

the query body.

The query body constructs the required XML.

```sql
namespace
<Product
ProductModelID
=
"..."
>
<Weight>
...
</Weight>
</Product>
SELECT
CatalogDescription.query(
'
declare namespace p1="https://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelDescription";
<Product  ProductModelID="{ (/p1:ProductDescription/@ProductModelID)[1] }">
{
/p1:ProductDescription/p1:Specifications/Weight
}
</Product>
'
)
AS
Result
FROM
Production.ProductModel
WHERE
CatalogDescription
IS
NOT
NULL
;
```
