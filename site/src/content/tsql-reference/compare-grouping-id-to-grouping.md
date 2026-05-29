---
name: "Compare GROUPING_ID() to GROUPING()"
title: "Compare GROUPING_ID() to GROUPING()"
category: "statements"
description: "Azure SQL Managed Instance"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Article

•

09/06/2024

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Is a function that computes the level of grouping.

can be used only

in the

list,

, or

clauses when

is specified.

Transact-SQL syntax conventions

## syntaxsql

A

column_expression

in a

SELECT - GROUP BY

clause.

The

must exactly match the expression in the

list.

For example, if you're grouping by

, use

; or if you're grouping by

, use

.

inputs the equivalent of the

return for each column in its column list in each output row, as a string

#### Columns

#### aggregated

#### GROUPING_ID (a, b, c) input = GROUPING(a) +

#### GROUPING(b) + GROUPING(c)

#### GROUPING_ID()

#### output

```sql
GROUPING_ID
```

```sql
GROUPING_ID
```

```sql
SELECT <select>
```

```sql
HAVING
```

```sql
ORDER BY
```

```sql
GROUP BY
```

```sql
GROUPING_ID <column_expression>
```

```sql
GROUP BY
```

```sql
DATEPART (yyyy, <column name>)
```

```sql
GROUPING_ID
(DATEPART (yyyy, <column name>))
```

```sql
<column name>
```

```sql
GROUPING_ID
(<column name>)
```

```sql
GROUPING_ID (<column_expression> [ , ...n ])
```

```sql
GROUPING
(<column_expression>)
```

```sql
GROUPING
_
ID
(
<column_expression>
[ , ...n ] )
```
