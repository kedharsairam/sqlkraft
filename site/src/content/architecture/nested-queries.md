---
title: "Nested queries"
topic: "xml-data"
description: ""
tags: ["xml-data","nested-queries"]
pubDate: "2025-12-01"
---

The

data type and the

TYPE directive in FOR XML queries

enable the XML returned by the

FOR XML queries to be processed on the server as well as on the client.

You can assign the FOR XML query result to an

type variable, or use XQuery to query the

result, and assign that result to an

type variable for more processing.

You can additionally process the XML returned in the variable,

, by using one of the

data

type methods. For example, you can retrieve the

attribute value by using the

value() method.

In the following example, the

query result is returned as an

type, because the

directive is specified in the

clause.

```sql
@x
ProductModelID
FOR XML
TYPE
FOR XML
DECLARE @x xml
SET @x=(SELECT ProductModelID, Name
FROM Production.ProductModel
WHERE ProductModelID=122 or ProductModelID=119
FOR XML RAW, TYPE)
SELECT @x
-- Result
--<row ProductModelID="122" Name="All-Purpose Bike Stand" />
--<row ProductModelID="119" Name="Bike Wash" />
DECLARE
@i int
;
SET
@i = (
SELECT
@x.value(
'/row[1]/@ProductModelID[1]'
,
'int'
));
SELECT
@i;
SELECT
ProductModelID,
Name
FROM
Production.ProductModel
WHERE
ProductModelID=119 or
ProductModelID=122
FOR
XML
RAW
,
TYPE
,ROOT(
'myRoot'
);
```
