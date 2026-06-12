---
title: "Remove square brackets WITHOUT_ARRAY_WRAPPER option (SQL Server)"
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
  - "remove-square-brackets-without-array-wrapper-option-sql-server"
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

To remove the square brackets that surround the JSON output of the

clause by

default, specify the

option. Use this option with a single-row result to

generate a single JSON object as output instead of an array with a single element.

If you use this option with a multiple-row result, the resulting output is not valid JSON because

of the multiple elements and the missing square brackets.

The following example shows the output of the

clause with and without the

option.

with the

option

JSON

(default) without the

option

JSON

```sql
FOR JSON
WITHOUT_ARRAY_WRAPPER
FOR JSON
WITHOUT_ARRAY_WRAPPER
WITHOUT_ARRAY_WRAPPER
WITHOUT_ARRAY_WRAPPER
SELECT
2015 as year
, 12 as month
, 15 as day
FOR
JSON
PATH
, WITHOUT_ARRAY_WRAPPER
{
"year"
: 2015,
"month"
: 12,
"day"
: 15
}
[{
"year"
: 2015,
"month"
: 12,
```
