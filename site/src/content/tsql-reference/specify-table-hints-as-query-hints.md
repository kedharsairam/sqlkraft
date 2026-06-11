---
name: "Specify table hints as query hints"
title: "Specify table hints as query hints"
category: "data-types"
description: ""
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

Query hints can't be specified in an

statement, except when a

clause is used

inside the statement.

Query hints can be specified only in the top-level query, not in subqueries. When a table hint is

specified as a query hint, the hint can be specified in the top-level query or in a subquery.

However, the value specified for

exposed_object_name

in the

clause must match

exactly the exposed name in the query or subquery.

We recommend using the

,

, or

table hint as a query hint only in the

context of a

plan guide

. Plan guides are useful when you can't modify the original query, for

example, because it's a third-party application. The query hint specified in the plan guide is

added to the query before it compiles and is optimized. For ad hoc queries, use the

clause only when testing plan guide statements. For all other ad hoc queries, we recommend

specifying these hints only as table hints.

When specified as a query hint, the

,

, and

table hints are valid for

the following objects:

Tables

Views

Indexed views

Common table expressions (the hint must be specified in the

statement whose

result set populates the common table expression)

Dynamic Management Views (DMVs)

Named subqueries

You can specify

,

, and

table hints as query hints for a query that

doesn't have any existing table hints. You can also use them to replace existing

,

, or

hints in the query, respectively.

Table hints other than

,

, and

are disallowed as query hints unless

the query already has a

clause specifying the table hint. In this case, a matching hint must

also be specified as a query hint. Specify the matching hint as a query hint by using

in the

clause. This specification preserves the query's semantics. For example, if the

query contains the table hint

, the

clause in the

@hints

parameter of the plan

guide must also contain the

hint. See

Example K

.

`INSERT`

`SELECT`

```sql
TABLE HINT
```

`INDEX`

`FORCESCAN`

`FORCESEEK`

```sql
TABLE HINT
```

`INDEX`

`FORCESCAN`

`FORCESEEK`

`SELECT`

`INDEX`

`FORCESCAN`

`FORCESEEK`

`INDEX`

`FORCESCAN`

`FORCESEEK`

`INDEX`

`FORCESCAN`

`FORCESEEK`

`WITH`

```sql
TABLE HINT
```

`OPTION`

`NOLOCK`

`OPTION`

`NOLOCK`
