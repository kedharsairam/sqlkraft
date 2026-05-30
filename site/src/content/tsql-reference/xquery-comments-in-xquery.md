---
name: "xquery-comments-in-xquery"
title: "XQuery - Comments in XQuery"
category: "xquery"
description: "XQuery Language Reference: Comments in XQuery"
syntax: "(:"
tags:
  - "xquery"
  - "comments-in-xquery"
pubDate: 2025-12-01
---

Applies to:

SQL Server

You can add comments to XQuery. Add comment strings by using the and

delimiters.

For example: SQL

The following example shows a query against an column of the type: SQL

```sql
(:
:)
Instructions
DECLARE
@x
AS
XML
;
SET
@x =
''
;
SELECT
@x.query(
'
(: simple query to construct an element :)
<ProductModel ProductModelID = "10" />
'
);
SELECT
Instructions.query(
'
(: declare prefix and namespace binding in the prolog. :)
declare namespace AWMI =
"http://schemas.microsoft.com/sqlserver/2004/07/adventure-
works/ProductModelManuInstructions";
(: Following expression retrieves the <Location> element children of the <root>
element. :)
/AWMI:root/AWMI:Location
'
)
AS
Result
FROM
Production.ProductModel
WHERE
ProductModelID = 7;
```
