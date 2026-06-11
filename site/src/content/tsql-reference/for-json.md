---
name: "FOR JSON"
title: "FOR JSON"
category: "queries"
description: ""
tags: ["tsql", "queries"]
pubDate: 2026-05-29
---

## JSON

## AUTO

## PATH

## INCLUDE_NULL_VALUES

In Fabric Data Warehouse, the query must end with

, so you can't use it inside

subqueries.

Specify

to return the results of a query formatted as JSON text. You also need to

specify one of the following JSON modes:

or

. For more information about the

clause, see

Format query results as JSON with FOR JSON

.

Format the JSON output automatically based on the structure of the

statement by

specifying

. For more info and examples, see

Format JSON output automatically

with AUTO mode

.

Get full control over the format of the JSON output by specifying

.

mode

lets you create wrapper objects and nest complex properties. For more info and examples, see

Format nested JSON output with PATH mode

.

## ROOT [ ('

## RootName

## ') ]

## WITHOUT_ARRAY_WRAPPER

Include

values in the JSON output by specifying the

option with the

clause. If you don't specify this option, the output doesn't include JSON properties

for

values in the query results. For more info and examples, see

Include Null Values in

JSON - INCLUDE_NULL_VALUES Option

.

Add a single, top-level element to the JSON output by specifying the

option with the

clause. If you don't specify the

option, the JSON output doesn't have a root element.

For more info and examples, see

Add a Root Node to JSON Output with the ROOT Option

.

Remove the square brackets that surround the JSON output by default by specifying the

option with the

clause. If you don't specify this option, the

JSON output is enclosed within square brackets. Use the

option to

generate a single JSON object as output. For more info, see

Remove Square Brackets from

JSON - WITHOUT_ARRAY_WRAPPER Option

.

For more info, see

Format query results as JSON with FOR JSON

.

SELECT (Transact-SQL)

Use FOR JSON output in the SQL Database Engine and in client apps

Last updated on 02/04/2026

Related content

```sql
FOR JSON
```

```sql
FOR JSON
```

`AUTO`

`PATH`

```sql
FOR
JSON
```

`SELECT`

```sql
FOR JSON AUTO
```

```sql
FOR JSON PATH
```

`PATH`

```sql
USE
AdventureWorks2025;
SELECT p.BusinessEntityID,
FirstName,
LastName,
PhoneNumber
AS
Phone
FROM
Person.Person
AS p
INNER
JOIN
Person.PersonPhone
AS pph
ON p.BusinessEntityID = pph.BusinessEntityID
WHERE
LastName
LIKE
'G%'
ORDER
BY
LastName, FirstName
FOR
XML
AUTO
,
TYPE
,
XMLSCHEMA
, ELEMENTS XSINIL;
```

`NULL`

`INCLUDE_NULL_VALUES`

```sql
FOR JSON
```

`NULL`

`ROOT`

```sql
FOR
JSON
```

`ROOT`

`WITHOUT_ARRAY_WRAPPER`

```sql
FOR JSON
```

`WITHOUT_ARRAY_WRAPPER`
