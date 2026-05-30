---
title: "Default Schema"
topic: "json-data"
description: |
  Applies to:

  SQL Server 2016 (13.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  Azure Synapse Analytics

  SQL database in Microsoft Fabric

  Use

  with the default schema to retu
tags:
  - "json-data"
  - "default-schema"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

Azure Synapse Analytics

SQL database in Microsoft Fabric

Use

with the default schema to return a table with one row for each property of the

object or for each element in the array.

Here are some examples that use

with the default schema. For more info and more

examples, see

OPENJSON (Transact-SQL)

.

SQL

name

John

surname

Doe

age

45

SQL

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
