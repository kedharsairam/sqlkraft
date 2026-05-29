---
name: 'JSON_OBJECTAGG'
title: 'JSON_OBJECTAGG'
category: 'statements'
description: 'SQL Server 2025 (17.x)'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## Return value

Applies to:

SQL Server 2025 (17.x)

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The


## syntax constructs a JSON object from an aggregation of SQL data or columns.
can also be used in a

statement with

clause.

The key/value pairs can be specified as input values, column, variable references.

Both

json

aggregate functions

and

are:

generally available for Azure SQL Database, Azure SQL Managed Instance (with the

SQL Server 2025

or

Always-up-to-date

update policy

**),

SQL database in Microsoft Fabric, and Fabric Data Warehouse.

in preview for SQL Server 2025 (17.x).

Transact-SQL syntax conventions


## syntaxsql
The key / value pair of the JSON object.

Optional. Omits the entire property of an object if the value is

, or use JSON null as property value. If omitted,

is default.


## Returns a valid JSON object string of
nvarchar(max)

type. If the

option is included then the JSON object is returned as

json

type.

The following example returns a JSON object with one key and null value.

SQL

Here's the result set.

JSON

７

Note

To create a JSON array from an aggregate instead, use

JSON_ARRAYAGG

.

json_key_value

json_null_clause

A. Return JSON object with one key

The following example constructs a JSON object with three properties from a result set.

SQL

Here's the result set.

JSON

The following example returns a result with two columns. The first column contains the

value. The second column contains a JSON

object where the key is the column name and value is the

.

SQL

The following example returns a JSON object as

json

type.

SQL

Result

JSON

Here's the result set.

object_id

column_list

3

5

6

7

8

The following example returns a result with four columns from a

statement containing

and

aggregates with

. The first two columns return the

and

column value. The third column


## returns the value of
aggregate on

B. Construct JSON object from result set

C. Return result with two columns

D. Return a JSON object as JSON type

ﾉ

Expand table

E. Return aggregated result with four columns

the

column. The fourth column


## returns the value of
aggregate on the

and

columns.

SQL

Here's the result set.

id

type

total_amount

json_total_name_amount

1

a

2

a

2

1

b

7

b

7

2

d

16

d

16

25

1

9

2

16

JSON Path Expressions in the SQL Database Engine

JSON data in SQL Server

JSON_ARRAYAGG (Transact-SQL)

Last updated on 11/18/2025

ﾉ

Expand table

Related content

```sql
JSON_OBJECTAGG
```

```sql
JSON_OBJECTAGG
```

```sql
SELECT
```

```sql
GROUP BY GROUPING SETS
```

```sql
JSON_OBJECTAGG
```

```sql
JSON_ARRAYAGG
```

```sql
NULL
```

```sql
NULL ON NULL
```

```sql
RETURNING json
```

```sql
JSON
_
OBJECTAGG
( json_key_value [ json_null_clause ] [
RETURNING
json ] )
json_key_value
::=
<json_name>
:
<value_expression>
json_null_clause
::=
NULL
ON
NULL
|
ABSENT
ON
NULL
```

```sql
SELECT
JSON_OBJECTAGG(
'key'
:
NULL
);
```

```sql
object_id
```

```sql
column_id
```

```sql
{"bitpos":12,"cid":6,"colguid":13,"hbcolid":3,"maxinrowlen":8,"nullbit":11,"offset":10,"ordkey":7,"ordlock":14,"rcmodified":4,"rscolid":2,"rsid":1,"
```

```sql
{"cmprlevel":9,"fgidfs":7,"fillfact":10,"idmajor":3,"idminor":4,"lockres":17,"maxint":13,"maxleaf":12,"maxnullbit":11,"minint":15,"minleaf":14,"numpa
```

```sql
{"cloneid":6,"dbfragid":8,"id":1,"partid":3,"rowsetid":7,"segid":5,"status":9,"subid":2,"version":4}
```

```sql
{"auid":1,"fgid":5,"ownerid":3,"pcdata":10,"pcreserved":11,"pcused":9,"pgfirst":6,"pgfirstiam":8,"pgroot":7,"status":4,"type":2}
```

```sql
{"fileid":2,"filename":4,"name":3,"status":1}
```

```sql
SELECT
```

```sql
SUM
```

```sql
JSON_OBJECTAGG
```

```sql
GROUP BY
GROUPING SETS
```

```sql
id
```

```sql
type
```

```sql
total_amount
```

```sql
SUM
```

```sql
{
"key"
:
null
}
```

```sql
SELECT
JSON_OBJECTAGG(c1:c2)
FROM
(
VALUES
(
'key1'
,
'c'
), (
'key2'
,
'b'
), (
'key3'
,
'a'
)
)
AS
t(c1, c2);
{
"key1"
:
"c"
,
"key2"
:
"b"
,
"key3"
:
"a"
}
```

```sql
SELECT
TOP (5) c.object_id,
JSON_OBJECTAGG(c.name:c.column_id)
AS
columns
FROM
sys.columns
AS
c
GROUP
BY
c.object_id;
```

```sql
SELECT
JSON_OBJECTAGG(
'a'
:1
RETURNING
JSON
);
{
"a"
:1}
```

```sql
amount
```

```sql
json_total_name_amount
```

```sql
JSON_OBJECTAGG
```

```sql
name
```

```sql
amount
```

```sql
{"k1":2}
NULL
```

```sql
{"k1":2}
```

```sql
{"k3":4,"k2":3}
NULL
```

```sql
{"k3":4,"k2":3}
```

```sql
{"j2":9,"j1":7}
NULL
```

```sql
{"j2":9,"j1":7}
NULL
NULL
```

```sql
{"k1":2,"k3":4,"k2":3,"j2":9,"j1":7}
```

```sql
NULL
```

```sql
{"k2":3,"k3":4,"k1":2}
```

```sql
NULL
```

```sql
{"j2":9,"j1":7}
```

```sql
WITH
T
AS
(
SELECT
*
FROM
(
VALUES
(1,
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
, 9)
)
AS
b(
id
,
name
,
type
, amount))
SELECT
id
,
type
,
SUM
(amount)
AS
total_amount,
JSON_OBJECTAGG(
name
:amount)
AS
json_total_name_amount
FROM
T
GROUP
BY
GROUPING
SETS
((
id
), (
type
), (
id
,
type
), ());
```
