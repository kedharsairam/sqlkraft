---
name: "Usage guidelines"
title: "Usage guidelines"
category: "statements"
description: "Specifies a column name in the common table expression. Duplicate names within a single CTE"
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

## Guidelines for nonrecursive common table expressions

### Guidelines for recursive common

### table expressions

Specifies a column name in the common table expression. Duplicate names within a single CTE

definition aren't allowed. The number of column names specified must match the number of

columns in the result set of the

CTE_query_definition. The list of column names is optional only

if distinct names for all resulting columns are supplied in the query definition.

Specifies a

statement whose result set populates the common table expression. The

statement for

CTE_query_definition

must meet the same requirements as for creating a

view, except a CTE can't define another CTE. For more information, see the Remarks section

and

CREATE VIEW.

If more than one

CTE_query_definition

is defined, the query definitions must be joined by one

of these set operators:

,

,

, or.

Query results from common table expressions aren't materialized. Each outer reference to the

named result set requires the defined query to be re-executed. For queries that require

multiple references to the named result set, consider using a

temporary object

instead.

You can't execute a stored procedure in a common table expression.

For usage guidelines about recursive and nonrecursive CTEs, see the following sections.

Guidelines for nonrecursive common table expressions

Guidelines for recursive common table expressions

A CTE must be followed by a single

,

,

,

, or

statement that

references some or all the CTE columns. A CTE can also be specified in a

statement as part of the defining

statement of the view.

７

Note

The following guidelines apply to nonrecursive common table expressions. For guidelines

that apply to recursive common table expressions, see.

## Guidelines for recursive common table expressions

### Guidelines for nonrecursive common

### table expressions

Multiple CTE query definitions can be defined in a nonrecursive CTE. The definitions must be

combined by one of these set operators:

,

,

, or.

A CTE can reference itself and previously defined CTEs in the same

clause. Forward

referencing isn't allowed.

Specifying more than one

clause in a CTE isn't allowed. For example, if a

CTE_query_definition

contains a subquery, that subquery can't contain a nested

clause

that defines another CTE.

For more information on nested CTEs in Microsoft Fabric, see

Nested Common Table

Expression (CTE) in Fabric data warehousing (Transact-SQL).

The following clauses can't be used in the

CTE_query_definition

:

(except when a

or

clause is specified)

clause with query hints

The

clause can't be used inside a CTE definition. It can only be used in the outermost

statement.

When a CTE is used in a statement that is part of a batch, the statement before it must be

followed by a semicolon.

A query referencing a CTE can be used to define a cursor.

Tables on remote servers can be referenced in the CTE.

When executing a CTE, any hints that reference a CTE can conflict with other hints that are

discovered when the CTE accesses its underlying tables, in the same manner as hints that

reference views in queries. When this occurs, the query returns an error.

1

1

７

Note

The following guidelines apply to defining a recursive common table expression. For

guidelines that apply to nonrecursive CTEs, see.

The

recursive CTE

definition must contain at least two CTE query definitions, an anchor

member and a recursive member. Multiple anchor members and recursive members can be

defined; however, all anchor member query definitions must be put before the first recursive

member definition. All CTE query definitions are anchor members unless they reference the

CTE itself.

Anchor members must be combined by one of these set operators:

,

,

, or.

is the only set operator allowed between the last anchor

member and first recursive member, and when combining multiple recursive members.

The number of columns in the anchor and recursive members must be the same.

The data type of a column in the recursive member must be the same as the data type of the

corresponding column in the anchor member.

The

clause of a recursive member must refer only one time to the CTE

expression_name.

The following items aren't allowed in the

CTE_query_definition

of a recursive member:

Scalar aggregation

,

,

(

is allowed)

Subqueries

A hint applied to a recursive reference to a CTE inside a

CTE_query_definition.

７

Note

A recursive CTE executes in the following order: first, the anchor member query runs and

produces the initial result set. Then, the recursive member runs repeatedly, with each

iteration using the previous iteration's output as its input. Recursion stops when the

recursive member returns no rows. Finally,

combines the results of the anchor

member and all recursive iterations into a single result set. This means that

doesn't deduplicate rows during each recursive step — it concatenates all intermediate

results after recursion completes.

1

`SELECT`

`SELECT`

```sql
UNION ALL
```

`UNION`

`EXCEPT`

`INTERSECT`

`SELECT`

`INSERT`

`UPDATE`

`MERGE`

`DELETE`

```sql
CREATE VIEW
```

`SELECT`

```sql
UNION ALL
```

`UNION`

`INTERSECT`

`EXCEPT`

`WITH`

`WITH`

`WITH`

```sql
ORDER BY
```

`TOP`

```sql
OFFSET/FETCH
```

```sql
INTO
OPTION
```

```sql
FOR BROWSE
```

`OPTION`

`SELECT`

```sql
UNION ALL
```

`UNION`

`INTERSECT`

`EXCEPT`

```sql
UNION ALL
```

`FROM`

```sql
SELECT DISTINCT
GROUP BY
PIVOT
HAVING
```

```sql
TOP
LEFT
```

`RIGHT`

```sql
OUTER JOIN
```

```sql
INNER JOIN
```

```sql
UNION ALL
```

```sql
UNION ALL
```
