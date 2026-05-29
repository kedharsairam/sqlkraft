---
name: 'Reporting errors'
title: 'Reporting errors'
category: 'statements'
description: 'Azure SQL Managed Instance'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

10/14/2025

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

This article describes guidelines for using the

data type methods.

The

data type methods can't be used in the

statement as shown in the following

example. The

data type methods are treated as subqueries, and subqueries aren't allowed

in the

statement. As a result, the following example returns an error:

SQL

A solution is to first assign the result of the

method to a variable of

type and then

specify the variable in the query.

SQL

The

data type methods are treated internally as subqueries. Because

requires a

scalar and doesn't allow aggregates and subqueries, you can't specify the

data type

methods in the

clause. A solution is to call a user-defined function that uses XML

methods inside of it.

### xml

### node()

### value()

### nodes()

### value()

### XACT_ABORT

```sql
PRINT
```

```sql
PRINT
```

```sql
GROUP BY
```

```sql
GROUP BY
```

```sql
DECLARE
@x
XML
SET
@x =
'<root>Hello</root>'
PRINT @x.value(
'/root[1]'
,
'varchar(20)'
)
-- will not work because this is treated
as a subquery (select top 1 col from table)
DECLARE
@x
XML
DECLARE
@c
VARCHAR
(
max
)
SET
@x =
'<root>Hello</root>'
SET
@c = @x.value(
'/root[1]'
,
'VARCHAR(11)'
)
PRINT @c
```
