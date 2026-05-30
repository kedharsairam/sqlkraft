---
title: "Explicit Schema"
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
  - "explicit-schema"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

Azure Synapse Analytics (serverless SQL pool only)

SQL

analytics endpoint in Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in

Microsoft Fabric

Use

with an explicit schema to return a table that's formatted as you specify in the

clause.

Here are some examples that use

with an explicit schema. For more information, see

OPENJSON (Transact-SQL)

.

The following query returns the results shown in the following table. Notice how the

clause causes values to be returned as JSON objects instead of scalar values in

and

.

SQL

```sql
OPENJSON
WITH
OPENJSON
AS JSON
col5
array_element
DECLARE
@
json
NVARCHAR
(
MAX
) =
N
'{"someObject":
{"someArray":
[
{"k1": 11, "k2": null, "k3": "text"},
{"k1": 21, "k2": "text2", "k4": { "data": "text4" }},
{"k1": 31, "k2": 32},
{"k1": 41, "k2": null, "k4": { "data": false }}
]
}
}'
SELECT
*
FROM
OPENJSON(@
json
, N
'lax $.someObject.someArray'
)
WITH
( k1
int
,
k2
varchar
(100),
col3
varchar
(6) N
'$.k3'
,
col4
varchar
(10) N
'lax $.k4.data'
,
col5
nvarchar
(
MAX
) N
'lax $.k4'
AS
JSON
,
array_element
nvarchar
(
MAX
) N
'$'
AS
JSON
)
```
