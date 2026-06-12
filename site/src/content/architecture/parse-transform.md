---
title: "Parse & transform"
topic: "json-data"
description: |
  Applies to:

  SQL Server 2016 (13.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  Azure Synapse Analytics (serverless SQL pool only)

  SQL

  analytics endpoint in Microsoft Fabric
tags:
  - "json-data"
  - "parse-transform"
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

(serverless SQL pool only)

analytics endpoint in Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in

Microsoft Fabric

The

rowset function converts JSON text into a set of rows and columns. After you

transform a JSON collection into a rowset with

, you can run any SQL query on the

returned data or insert it into a SQL Server table. For more information about working with

JSON data in the SQL Server Database Engine, see

JSON data in SQL Server.

The

function takes a single JSON object or a collection of JSON objects and

transforms them into one or more rows. By default, the

function returns the following

data:

From a JSON object, the function returns all the key/value pairs that it finds at the first

level.

From a JSON array, the function returns all the elements of the array with their indexes.

You can add an optional

clause to provide a schema that explicitly defines the structure

of the output.

When you use the

function without providing an explicit schema for the results - that

is, without a

clause after

- the function returns a table with the following three

columns:

1. The

of the property in the input object (or the index of the element in the input

array).

2. The

of the property or the array element.

3. The

(for example, string, number, boolean, array, or object).

returns each property of the JSON object, or each element of the array, as a separate

row.

The following example uses

with the default schema - that is, without the optional

clause - and returns one row for each property of the JSON object.

```sql
OPENJSON
OPENJSON
OPENJSON
OPENJSON
WITH
OPENJSON
WITH
OPENJSON name value type
OPENJSON
OPENJSON
WITH
```
