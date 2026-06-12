---
name: "Logical processing order of the SELECT statement"
title: "Logical processing order of the SELECT statement"
category: "queries"
description: "Syntax for Azure Synapse Analytics, Analytics Platform System (PDW), and Microsoft Fabric:"
tags: ["tsql","queries"]
pubDate: 2026-05-29
---

## Syntax for Azure Synapse Analytics, Analytics Platform System (PDW), and Microsoft Fabric:

## syntaxsql

The order of the clauses in the

statement is significant. Any one of the optional clauses

can be omitted, but when the optional clauses are used, they must appear in the appropriate

order.

statements are permitted in user-defined functions only if the select lists of these

statements contain expressions that assign values to variables that are local to the functions.

A four-part name constructed with the

function as the server-name part can be

used as a table source wherever a table name can appear in a

statement. A four-part

name can't be specified for Azure SQL Database.

Some syntax restrictions apply to

statements that involve remote tables.

### db_datareader

### db_owner

### sysadmin

`SELECT`

`SELECT`

`OPENDATASOURCE`

`SELECT`

`SELECT`

```sql
SELECT
[
ALL
|
DISTINCT
]
[
TOP ( expression ) [
PERCENT
] [
WITH
TIES
] ]
<select_list>
[
INTO new_table ]
[
FROM
{
<table_source>
} [ ,.n ] ]
[
WHERE
<search_condition>
]
[
<GROUP BY>
]
[
HAVING
<search_condition>
]
[ ; ]
[
WITH
<common_table_expression>
[ ,.n ] ]
SELECT
<select_criteria>
[ ; ]
<select_criteria>
::=
[
TOP ( top_expression ) ]
[
ALL
|
DISTINCT
]
{ * | column_name | expression } [ ,.n ]
[
FROM
{ table_source } [ ,.n ] ]
[
WHERE
<search_condition>
]
[
GROUP
BY
<group_by_clause>
]
[
HAVING
<search_condition>
]
[
ORDER
BY
<order_by_expression>
]
[
OPTION (
<query_option>
[ ,.n ] ) ]
```
