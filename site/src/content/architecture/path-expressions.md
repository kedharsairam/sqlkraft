---
title: "Path Expressions"
topic: "json-data"
description: "2016 (13.x) and later versions Azure SQL Managed Instance Azure Synapse Analytics (serverless SQL pool only) SQL database in Microsoft Fabric Use JSON"
tags: ["json-data","path-expressions"]
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

(serverless SQL pool only)

database in Microsoft Fabric

Use JSON path expressions to reference the properties of JSON objects.

You have to provide a path expression when you call the following functions.

When you call

OPENJSON

to create a relational view of JSON data.

When you call

JSON_VALUE

to extract a value from JSON text.

When you call

JSON_QUERY

to extract a JSON object or an array.

When you call

JSON_MODIFY

to update the value of a property in a JSON string.

A path expression has two components.

1. The optional

path mode

, with a value of

or.

2. The

path

itself.

At the beginning of the path expression, optionally declare the path mode by specifying the

keyword

or. The default is.

In

mode, the function returns empty values if the path expression contains an error.

For example, if you request the value

, and the JSON text doesn't contain a

key, the function returns null, but doesn't raise an error.

In

mode, the function raises an error if the path expression contains an error.

The following query explicitly specifies

mode in the path expression.

```sql
lax strict lax strict lax lax
$.name name strict lax
DECLARE
@
json
AS
NVARCHAR (
MAX
);
SET
@
json
= N
'{. }'
;
```
