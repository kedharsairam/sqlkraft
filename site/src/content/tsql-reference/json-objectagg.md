---
name: "JSON_OBJECTAGG"
title: "JSON_OBJECTAGG"
category: "statements"
description: "2025 (17.x)"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## Return value

2025 (17.x)

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

2025

or

Always-up-to-date

update policy

\*\*),

SQL database in Microsoft Fabric, and Fabric Data Warehouse.

in preview for SQL Server 2025 (17.x).

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

Here's the result set.

JSON

７

Note

To create a JSON array from an aggregate instead, use

JSON_ARRAYAGG.

json_key_value

json_null_clause

A. Return JSON object with one key

The following example constructs a JSON object with three properties from a result set.

Here's the result set.

JSON

The following example returns a result with two columns. The first column contains the

value. The second column contains a JSON

object where the key is the column name and value is the.

The following example returns a JSON object as

json

type.

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

aggregates with. The first two columns return the

and

column value. The third column

## returns the value of

aggregate on

B. Construct JSON object from result set

C. Return result with two columns

D. Return a JSON object as JSON type

Expand table

E. Return aggregated result with four columns

the

column. The fourth column

## returns the value of

aggregate on the

and

columns.

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

Expand table
