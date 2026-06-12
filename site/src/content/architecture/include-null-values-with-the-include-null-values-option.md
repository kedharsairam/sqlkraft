---
title: "Include null values with the INCLUDE_NULL_VALUES option"
topic: "json-data"
description: "2016 (13.x) and later versions Azure SQL Managed Instance Azure Synapse Analytics (serverless SQL pool only) SQL analytics endpoint in Microsoft Fabric"
tags: ["json-data","include-null-values-with-the-include-null-values-option"]
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

(serverless SQL pool only)

analytics endpoint in Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in

Microsoft Fabric

To include null values in the JSON output of the

clause, specify the

option.

If you don't specify the

option, the JSON output doesn't include

properties for values that are null in the query results.

The following example shows the output of the

clause with and without the

option.

Here's another example of a

clause with the

option.

JSON

ﾉ

Expand table

```sql
FOR JSON
INCLUDE_NULL_VALUES
INCLUDE_NULL_VALUES
FOR JSON
INCLUDE_NULL_VALUES
INCLUDE_NULL_VALUES
INCLUDE_NULL_VALUES
{ "name": "John", "surname": "Doe" }
{ "name": "John", "surname": "Doe", "age": null, "phone":
null }
FOR JSON
INCLUDE_NULL_VALUES
SELECT name
, surname
FROM emp
FOR
JSON
AUTO
, INCLUDE_NULL_VALUES
[{
"name"
:
"John"
,
"surname"
:
null
```
