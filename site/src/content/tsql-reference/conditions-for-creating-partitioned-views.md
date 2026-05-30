---
name: "Conditions for creating partitioned views"
title: "Conditions for creating partitioned views"
category: "statements"
description: "When you design a partitioning scheme, it must be clear what data belongs to each partition."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

When you design a partitioning scheme, it must be clear what data belongs to each partition.

For example, the data for the

table is distributed in three member tables in three

server locations:

on

,

on

, and

on

.

A partitioned view on

is defined in the following way:

Generally, a view is said to be a partitioned view if it is of the following form:

## syntaxsql

1. The select

７

Note

The preferred method for partitioning data local to one server is through partitioned

tables. For more information, see

.

In the column list of the view definition, select all columns in the member tables.

Ensure that the columns in the same ordinal position of each

are of the

same type, including collations. It is not sufficient for the columns to be implicitly

convertible types, as is generally the case for

.

Also, at least one column (for example

) must appear in all the select lists in

the same ordinal position. Define

in a way that the member tables

have CHECK constraints

defined on

, respectively.

Constraint

defined on table

must be of the following form:

## syntaxsql

The constraints must be in such a way that any specified value of

can satisfy,

at most, one of the constraints

so that the constraints form a set of

disjointed or nonoverlapping intervals. The column

on which the disjointed

constraints are defined is called the partitioning column. The partitioning column

can have different names in the underlying tables. The constraints must be in an

enabled and trusted state for them to meet the previously mentioned conditions of

the partitioning column. If the constraints are disabled, re-enable constraint

checking by using the

option of

,

and using the

option to validate them.

The following examples show valid sets of constraints:

## syntaxsql

The same column cannot be used multiple times in the select list.

2. Partitioning column

The partitioning column is a part of the PRIMARY KEY of the table.

### user options

`Customers`

`Customers_33`

`Server1`

`Customers_66`

`Server2`

`Customers_99`

`Server3`

`Server1`

`list`

```sql
--Partitioned view as defined on Server1
CREATE
VIEW
Customers
AS
--Select from local member table.
SELECT
*
FROM
CompanyData.dbo.Customers_33
UNION
ALL
--Select from member table on Server2.
SELECT
*
FROM
Server2.CompanyData.dbo.Customers_66
UNION
ALL
--Select from member table on Server3.
SELECT
*
FROM
Server3.CompanyData.dbo.Customers_99;
SELECT
<select_list1>
FROM
T
1
UNION
ALL
SELECT
<select_list2>
FROM
T
2
UNION
ALL
...
SELECT
<select_listn>
FROM
T n;
```

```sql
select list
```

`UNION`

```sql
<col>
```

```sql
<col>
```

```sql
T1, ...,
Tn
```

```sql
C1, ..., Cn
```

```sql
<col>
```

`C1`

`T1`

```sql
<col>
```

```sql
C1, ..., Cn
```

```sql
<col>
```

```sql
CHECK CONSTRAINT *constraint_name*
```

```sql
ALTER TABLE
```

```sql
WITH CHECK
```

```sql
C
1
::=
< simple_interval >
[
OR
< simple_interval >
OR
...]
< simple_interval >
:: =
< col >
{
< | >
| \
<= | >
= | =
< value >
}
|
< col >
BETWEEN
< value1 >
AND
< value2 >
|
< col >
IN ( value_list )
|
< col >
{ > | >= }
< value1 >
AND
< col >
{
< | <= } < value2 >
{ [col
< 10], [col between 11 and 20] , [col >
20] }
{ [col between 11 and 20], [col between 21 and 30], [col between 31 and
100] }
```
