---
title: "Add namespaces to queries"
topic: "xml-data"
description: "WITH XMLNAMESPACES (Transact-SQL) provides namespace URI support in the following way: It makes the n"
tags: ["xml-data","add-namespaces-to-queries"]
pubDate: "2025-12-01"
---

WITH XMLNAMESPACES (Transact-SQL)

provides namespace URI support in the following way:

It makes the namespace prefix to URI mapping available when

Constructing XML Using

FOR XML

queries.

It makes the namespace to URI mapping available to the static namespace context of the

xml Data Type Methods.

WITH XMLNAMESPACES lets you include XML namespaces in FOR XML queries. For example,

consider the following FOR XML query:

This is the result:

XML

To add namespaces to the XML constructed by the FOR XML query, first specify the namespace

prefix to URI mappings by using the WITH NAMESPACES clause. Then, use the namespace

prefixes in specifying the names in the query as shown in the following modified query. The

WITH XMLNAMESPACES clause specifies the namespace prefix (

) to URI (

) mapping.

The

prefix is then used in specifying the element and attribute names to be constructed by

the FOR XML query.

```sql
ns1 uri ns1
SELECT
ProductID,
Name
, Color
FROM
Production.Product
WHERE
ProductID
IN (316, 317)
FOR
XML
RAW
;
<row
ProductID
=
"316"
Name
=
"Blade"
/>
<row
ProductID
=
"317"
Name
=
"LL Crankarm"
Color
=
"Black"
/>
```
