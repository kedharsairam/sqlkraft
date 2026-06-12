---
name: "table"
title: "Table"
category: "data-types"
description: ""
tags: ["tsql","data-types"]
pubDate: 2026-05-29
---

You can use

with an

or

statement positioned on a cursor that uses

## syntax.

The

clause isn't supported in the following statements:

DML statements that reference local partitioned views, distributed partitioned views, or

remote tables.

statements that contain an

statement.

Full-text predicates aren't allowed in the

clause when the database compatibility

level is set to 100.

The

clause can't be used to insert into a view, or rowset function.

A user-defined function can't be created if it contains an

clause that has a

table as its target.

To prevent nondeterministic behavior, the

clause can't contain the following references:

Subqueries or user-defined functions that perform user or system data access, or are

assumed to perform such access. User-defined functions are assumed to perform data

access if they aren't schema-bound.

A column from a view or inline table-valued function when that column is defined by one

of the following methods:

A subquery.

A user-defined function that performs user or system data access, or is assumed to

perform such access.

A computed column that contains a user-defined function that performs user or

system data access in its definition.

When SQL Server detects such a column in the

clause, error 4186 is raised.

When you're capturing the results of an

clause in a nested

,

,

, or

statement and inserting those results into a target table, keep the following information

in mind:

`OUTPUT`

`UPDATE`

`DELETE`

```sql
WHERE CURRENT OF
```

`OUTPUT`

`INSERT`

`EXECUTE`

`OUTPUT`

```sql
OUTPUT INTO
```

```sql
OUTPUT INTO
```

`OUTPUT`

`OUTPUT`

`OUTPUT`

`INSERT`

`UPDATE`

`DELETE`

`MERGE`
