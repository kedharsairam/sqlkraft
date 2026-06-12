---
title: "Default Schema"
topic: "json-data"
description: ""
tags: ["json-data","default-schema"]
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

Use

with the default schema to return a table with one row for each property of the

object or for each element in the array.

Here are some examples that use

with the default schema. For more info and more

examples, see

OPENJSON (Transact-SQL).

name

John

surname

Doe

age

45

ﾉ

Expand table

```sql
OPENJSON
OPENJSON
SELECT
*
FROM
OPENJSON(
'{"name":"John","surname":"Doe","age":45}'
)
SELECT
[
key
],
value
FROM
OPENJSON(
'["en-GB", "en-UK","de-AT","es-AR","sr-Cyrl"]'
)
```
