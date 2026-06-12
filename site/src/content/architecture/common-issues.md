---
title: "Common issues"
topic: "json-data"
description: ""
tags: ["json-data","common-issues"]
pubDate: "2025-12-01"
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

(serverless SQL pool only)

database in Microsoft Fabric

Find answers here to some common questions about the built-in JSON support in the SQL

Database Engine.

I want to create a JSON text result from a simple SQL query on a single table. FOR

JSON PATH and FOR JSON AUTO produce the same output. Which of these two options should

I use?

Use FOR JSON PATH. Although there is no difference in the JSON output, AUTO mode

applies some additional logic that checks whether columns should be nested. Consider PATH

the default option.

I want to produce complex JSON with several arrays on the same level. FOR JSON

PATH can create nested objects using paths, and FOR JSON AUTO creates additional nesting

level for each table. Neither one of these two options lets me generate the output I want. How

can I create a custom JSON format that the existing options don't directly support?

You can create any data structure by adding FOR JSON queries as column expressions

that return JSON text. You can also create JSON manually by using the JSON_QUERY function.

The following example demonstrates these techniques.

```sql
SELECT col1, col2, col3,
(
SELECT col11, col12, col13
FROM t11
WHERE t11.FK = t1.PK
FOR
JSON
PATH
) as t11,
(
SELECT col21, col22, col23
FROM t21
WHERE t21.FK = t1.PK
FOR
JSON
PATH
) as t21,
(
SELECT col31, col32, col33
FROM t31
WHERE t31.FK = t1.PK
FOR
JSON
PATH
) as t31,
JSON_QUERY(
'{"'
+col4+
'":"'
+col5+
'"}'
) as t41
```
