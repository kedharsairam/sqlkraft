---
name: "Predicates supported with a JSON index"
title: "Predicates supported with a JSON index"
category: "queries"
description: "For a list of features supported by the editions of SQL Server on Windows, see:"
tags: ["tsql", "queries"]
pubDate: 2026-05-29
---

For a list of features supported by the editions of SQL Server on Windows, see:

Editions and supported features of SQL Server 2025 Preview

Editions and supported features of SQL Server 2022

Editions and supported features of SQL Server 2019

Editions and supported features of SQL Server 2017

Editions and supported features of SQL Server 2016

Determines the level of data compression used by the index.

No compression used on data by the index

Row compression used on data by the index

Page compression used on data by the index

Every option can be specified only once per

statement. Specifying a

duplicate of any option raises an error.

If you specify a filegroup for a JSON index, the index is placed on that filegroup, regardless of

the partitioning scheme of the table.

For more information about creating indexes, see the Remarks section in

CREATE INDEX

.

Searching operations on JSON documents contained in a

column in a table can be

optimized if a JSON index exists on the

column. The JSON index is used in queries with

various JSON function-based expressions.

### json

### json

#### SalesOrderNumber

#### Info

### json

## JSON_PATH_EXISTS function

## JSON_VALUE function

The following examples use the

table in the

database with a

column called

. The

column is created as a

type. A JSON

index is also created on the

column with default settings. The following code sample

shows the

statement:

For the sample search expressions, use the following JSON documents as data:

Use the

JSON_PATH_EXISTS

function to test if a specified SQL/JSON path exists in a JSON

document.

This query demonstrates

on a

column that can be optimized using a

JSON index:

JSON index is supported with

predicate and the following operators:

Comparison operators (

)

predicate (Not currently supported)

Expand table

### json

Use the

JSON_VALUE

to extract the JSON text / scalar value in a specified SQL/JSON path in a

JSON document. The following queries show how a

expression on a

column

can be optimized using a JSON index.

Equality search for a JSON string in an object property:

Equality search for a JSON number in an object property after converting the value to an

data type:

Range search for a JSON number in an object property after converting the value to an

data type:

Range search for a JSON number in an object property after converting the value to a

data type:

The JSON index is supported with a

predicate, and the following operators:

Comparison operators (

)

predicate (not currently supported)

predicate (not currently supported)

### json

### sysadmin

### db_ddladmin

### db_owner

### json

### json

### json

## JSON_CONTAINS function

```sql
CREATE JSON INDEX
```

`Sales.SalesOrderHeader`

`AdventureWorks2022`

`Info`

`Info`

`Info`

```sql
CREATE JSON INDEX
```

```sql
437
{"Customer":{"Name":"Kelsey Raje","ID":16517,"Type":"IN"},"Order":
{"ID":43710,"Number":"SO43710","CreationDate":"2011-06-
02T00:00:00","TotalDue":3953.9884}}
643
{"Customer":{"Name":"Aaron Campbell","ID":16167,"Type":"IN"},"Order":
{"ID":64304,"Number":"SO64304","CreationDate":"2014-01-
16T00:00:00","TotalDue":36.0230, "IsProcessed": true}}
```

`JSON_PATH_EXISTS`

`JSON_PATH_EXISTS`

```sql
=
```

```sql
IS [NOT] NULL
```

```sql
CREATE
JSON
INDEX sales_info_idx
ON
Sales.SalesOrderHeader (Info);
```

```sql
SELECT
COUNT (*)
FROM
Sales.SalesOrderHeader
WHERE
JSON_PATH_EXISTS(Info,
'$.Order.IsProcessed'
) = 1;
```

`JSON_VALUE`

`JSON_VALUE`

```sql
=
```

`LIKE`

```sql
IS [NOT] NULL
```

```sql
SELECT
COUNT (*)
FROM
Sales.SalesOrderHeader
WHERE
JSON_VALUE(Info,
'$.Customer.Type'
) =
'IN'
;
SELECT
*
FROM
Sales.SalesOrderHeader
WHERE
JSON_VALUE(Info,
'$.Customer.ID'
RETURNING
INT
) = 16167;
SELECT
*
FROM
Sales.SalesOrderHeader
WHERE
JSON_VALUE(Info,
'$.Customer.ID'
RETURNING
INT
)
IN (16167, 16517);
SELECT
*
FROM
Sales.SalesOrderHeader
WHERE
JSON_VALUE(Info,
'$.Order.TotalDue RETURNING decimal(20, 4)) BETWEEN 1000 and 2000;
```
