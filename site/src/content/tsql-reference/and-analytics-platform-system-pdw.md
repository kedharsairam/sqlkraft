---
name: "and Analytics Platform System (PDW)"
title: "And Analytics Platform System (PDW)"
category: "operators"
description: "When the database compatibility level is 110 or higher. See"
tags: ["tsql", "operators"]
pubDate: 2026-05-29
---

When the database compatibility level is 110 or higher. See

Breaking changes to Database

Engine features in SQL Server 2016.

The following guidelines apply to using a recursive common table expression:

All columns returned by the recursive CTE are nullable regardless of the nullability of the

columns returned by the participating

statements.

An incorrectly composed recursive CTE can cause an infinite loop. For example, if the

recursive member query definition returns the same values for both the parent and child

columns, an infinite loop is created. To prevent an infinite loop, you can limit the number

of recursion levels allowed for a particular statement by using the

hint and

a value between

and

in the

clause of the

,

,

, or

statement. This lets you control the execution of the statement until you resolve

the code problem that is creating the loop. The server-wide default is 100. When 0 is

specified, no limit is applied. Only one

value can be specified per statement.

For more information, see

Query hints.

A view that contains a recursive common table expression can't be used to update data.

Cursors can be defined on queries using CTEs. The CTE is the

select_statement

argument

that defines the result set of the cursor. Only fast forward-only and static (snapshot)

cursors are allowed for recursive CTEs. If another cursor type is specified in a recursive

CTE, the cursor type is converted to static.

Tables on remote servers can be referenced in the CTE. If the remote server is referenced

in the recursive member of the CTE, a spool is created for each remote table so the tables

can be repeatedly accessed locally. If it's a CTE query, Index Spool/Lazy Spools are

displayed in the query plan, and will have the additional

predicate. This is one

way to confirm proper recursion.

Analytic and aggregate functions in the recursive part of the CTE are applied to the set for

the current recursion level and not to the set for the CTE. Functions like

operate only on the subset of data passed to them by the current recursion level and not

the entire set of data passed to the recursive part of the CTE. For more information, see

example I. Use analytical functions in a recursive CTE that follows.

1

`SELECT`

`MAXRECURSION`

```sql
0
```

```sql
32767
```

`OPTION`

`INSERT`

`UPDATE`

`DELETE`

`SELECT`

`MAXRECURSION`

```sql
WITH STACK
```

`ROW_NUMBER`
