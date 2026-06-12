---
name: "Pseudocode and semantics"
title: "Pseudocode and semantics"
category: "operators"
description: "CTE query definitions are considered anchor members unless they reference the CTE"
tags: ["tsql","operators"]
pubDate: "2026-05-29"
---

CTE query definitions are considered anchor members unless they reference the CTE

itself. All anchor-member query definitions must be positioned before the first recursive

member definition, and a

operator must be used to join the last anchor

member with the first recursive member.

2. Recursive invocation of the routine.

The recursive invocation includes one or more CTE query definitions joined by

operators that reference the CTE itself. These query definitions are referred to as recursive

members.

3. Termination check.

The termination check is implicit; recursion stops when no rows are returned from the

previous invocation.

For more information, see:

Query hints

WITH common_table_expression

Recursive CTEs

The recursive CTE structure must contain at least one anchor member and one recursive

member. The following pseudocode shows the components of a simple recursive CTE that

contains a single anchor member and single recursive member.

## syntaxsql

７

Note

An incorrectly composed recursive CTE might cause an infinite loop. For example, if the

recursive member query definition returns the same values for both the parent and child

columns, an infinite loop is created. When testing the results of a recursive query, you can

limit the number of recursion levels allowed for a specific statement by using the

hint and a value between 0 and 32,767 in the

clause of the

,

,

, or

statement.

```sql
UNION ALL
```

```sql
UNION ALL
```

`MAXRECURSION`

`OPTION`

`INSERT`

`UPDATE`

`DELETE`

`SELECT`

```sql
WITH cte_name ( column_name [ ,.n ] )
AS (
CTE
_query_definition
-- Anchor member is defined.
```
