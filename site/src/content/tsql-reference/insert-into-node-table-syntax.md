---
name: "INSERT Into node table syntax"
title: "INSERT Into node table syntax"
category: "queries"
description: "2017 (14.x) and later versions"
tags: ["tsql","queries"]
pubDate: "2026-05-29"
---

2017 (14.x) and later versions

Azure

SQL Managed Instance

Adds one or more rows to a

or

table in SQL Server.

The syntax for inserting into a Node table is the same as for a regular table.

## syntaxsql

`node`

`edge`

```sql
[
WITH
<common_table_expression>
[ ,.n ] ]
INSERT
{
[
TOP ( expression ) [
PERCENT
] ]
[
INTO
]
{
<object>
| rowset_function_limited
[
WITH (
<Table_Hint_Limited>
[.n ] ) ]
}
{
[ (column_list) ] | [(
<edge_table_column_list>
)]
[
<OUTPUT Clause>
]
{
VALUES ( {
DEFAULT
|
NULL
| expression } [ ,.n ] ) [ ,.n ]
| derived_table
| execute_statement
|
<dml_table_source>
|
DEFAULT
VALUES
}
}
}
[;]
<object>
::=
{
[ server_name. database_name. schema_name.
| database_name.[ schema_name ].
| schema_name.
]
node_table_name | edge_table_name
}
<dml_table_source>
::=
SELECT
<select_list>
FROM (
<dml_statement_with_output_clause>
)
[
AS
] table_alias [ ( column_alias [ ,.n ] ) ]
[
WHERE
<on_or_where_search_condition>
]
[
OPTION (
<query_hint>
[ ,.n ] ) ]
```
