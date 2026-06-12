---
name: "JSON_ARRAYAGG"
title: "JSON_ARRAYAGG"
category: "statements"
description: "2025 (17.x)"
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

## Return value

2025 (17.x)

Constructs a JSON array from an aggregation of SQL data or columns.

can also be used in a statement with clause.

Both json

aggregate functions and

are: generally available for Azure SQL Database, Azure SQL Managed Instance (with the
2025 or

Always-up-to-date

update policy

\*\*),

, and Fabric Data Warehouse.

in preview for SQL Server 2025 (17.x).

## syntaxsql

The value expression can be a column or expression in a query or constants/literals.

Optional.

json_null_clause can be used to control the behavior of

function when value_expression

is. The option converts the SQL

value into a JSON null value when generating the value of the element in the JSON array. The option omits

the element in the JSON array if the value is. If omitted, is default.

Optional. The order of elements in the resulting JSON array can be specified to order the input rows to the aggregate.

## Returns a valid JSON array string of

nvarchar(max) type. If the

option is included then the JSON array is returned as json

type.

The following example returns an empty JSON array.

７

Note

To create a JSON object from an aggregate instead, use

JSON_OBJECTAGG.

value_expression json_null_clause

order_by_clause

Example 1

Result

JSON

The following example constructs a JSON array with three elements from a result set.

Result

JSON

The following example constructs a JSON array with three elements ordered by the value of the column.

Result

JSON

The following example returns a result with two columns. The first column contains the value. The second column contains a JSON

array containing the names of the columns. The columns in the JSON array are ordered based on the value.

Result

object_id column_list

3

5

6

7

8

Example 2

Example 3

Example 4

Example 5

The following example returns a result with four columns from a SELECT statement containing SUM and JSON_ARRAYAGG aggregates with GROUP

BY GROUPING SETS. The first two columns return the and

column value. The third column

## returns the value of SUM

aggregate on the column. The fourth column

## returns the value of JSON_ARRAYAGG aggregate on the

column.

Result

id type

total_amount json_total_name_amount

1 a

2 a

2

1 b

7 b

7

2 d

16 d

16

25

1

9

2

16

The following example returns a JSON array as json

type.

Result

JSON

JSON Path Expressions in the SQL Database Engine

JSON data in SQL Server

JSON_OBJECTAGG (Transact-SQL)

Example 6

`JSON_ARRAYAGG`

`SELECT`

```sql
GROUP BY
GROUPING SETS
```

`JSON_OBJECTAGG`

`JSON_ARRAYAGG`

`JSON_ARRAYAGG`

`NULL`

```sql
NULL ON NULL
```

`NULL`

```sql
ABSENT ON NULL
```

`NULL`

```sql
ABSENT ON NULL
```

```sql
RETURNING json
```

```sql
JSON
_
ARRAYAGG (value_expression [ order_by_clause ] [ json_null_clause ] [
RETURNING json ] ) json_null_clause
::=
NULL
ON
NULL
|
ABSENT
ON
NULL order_by_clause
::=
ORDER
BY
<column_list>
```

```sql
SELECT
JSON_ARRAYAGG(
NULL
);
```

`object_id`

`column_id`

```sql
["rsid","rscolid","hbcolid","rcmodified","ti","cid","ordkey","maxinrowlen","status","offset","nullbit","bitpos","colguid","ordlock"]
```

```sql
["rowsetid","ownertype","idmajor","idminor","numpart","status","fgidfs","rcrows","cmprlevel","fillfact","maxnullbit","maxleaf","maxint","minleaf","m
```

```sql
["id","subid","partid","version","segid","cloneid","rowsetid","dbfragid","status"]
```

```sql
["auid","type","ownerid","status","fgid","pgfirst","pgroot","pgfirstiam","pcused","pcdata","pcreserved"]
```

```sql
["status","fileid","name","filename"]
[]
```

```sql
SELECT
JSON_ARRAYAGG(c1)
FROM (
VALUES (
'c'
), (
'b'
), (
'a'
))
AS t(c1);
[
"c"
,
"b"
,
"a"
]
```

```sql
SELECT
JSON_ARRAYAGG( c1
ORDER
BY c1)
FROM (
VALUES (
'c'
), (
'b'
), (
'a'
)
)
AS t(c1);
[
"a"
,
"b"
,
"c"
]
```

```sql
SELECT
TOP(5) c.object_id, JSON_ARRAYAGG(c.name
ORDER
BY c.column_id)
AS column_list
FROM sys.columns
AS c
GROUP
BY c.object_id;
```

`id`

`type`

`total_amount`

`amount`

`json_total_amount`

`amount`

```sql
[2]
NULL
```

```sql
[2]
```

```sql
[4,3]
NULL
```

```sql
[4,3]
```

```sql
[9,7]
NULL
```

```sql
[9,7]
NULL
NULL
```

```sql
[2,4,3,9,7]
```

`NULL`

```sql
[3,4,2]
```

`NULL`

```sql
[9,7]
```

```sql
WITH
T
AS (
SELECT
*
FROM (
VALUES (1,
'k1'
,
'a'
, 2), (1,
'k2'
,
'b'
, 3), (1,
'k3'
,
'b'
, 4), (2,
'j1'
,
'd'
, 7), (2,
'j2'
,
'd'
, 9))
AS b(
id
,
name
,
type
, amount))
SELECT id
,
type
,
SUM (amount)
AS total_amount,
JSON_ARRAYAGG(amount)
AS json_total_amount
FROM
T
GROUP
BY
GROUPING
SETS ((
id
), (
type
), (
id
,
type
), ());
```

```sql
SELECT
JSON_ARRAYAGG(1
RETURNING
JSON
);
[1]
```
