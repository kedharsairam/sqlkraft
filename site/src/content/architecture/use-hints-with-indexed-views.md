---
title: "Use hints with indexed views"
topic: "index-architecture"
description: "The estimated cost for using the index has the lowest cost of any access mechanisms"
tags: ["index-architecture", "architecture"]
pubDate: 2026-05-29
---

clauses

Table references

The estimated cost for using the index has the lowest cost of any access mechanisms

considered by the Query Optimizer.

Every table referenced in the query (either directly, or by expanding a view to access its

underlying tables) that corresponds to a table reference in the indexed view must have

the same set of hints applied on it in the query.

Other than the requirements for the

options and table hints, these are the same rules that

the Query Optimizer uses to determine whether a table index covers a query. Nothing else has

to be specified in the query for an indexed view to be used.

A query doesn't have to explicitly reference an indexed view in the

clause for the Query

Optimizer to use the indexed view. If the query contains references to columns in the base

tables that are also present in the indexed view, and the Query Optimizer estimates that using

the indexed view provides the lowest cost access mechanism, the Query Optimizer chooses the

indexed view, similar to the way it chooses base table indexes when they aren't directly

referenced in a query. The Query Optimizer can choose the view when it contains columns that

aren't referenced by the query, as long as the view offers the lowest cost option for covering

one or more of the columns specified in the query.

The Query Optimizer treats an indexed view referenced in the

clause as a standard view.

The Query Optimizer expands the definition of the view into the query at the start of the

optimization process. Then, indexed view matching is performed. The indexed view can be

used in the final execution plan selected by the Query Optimizer, or instead, the plan might

materialize necessary data from the view by accessing the base tables referenced by the view.

The Query Optimizer chooses the lowest-cost alternative.

You can prevent view indexes from being used for a query by using the

query

hint, or you can use the

table hint to force the use of an index for an indexed view

specified in the

clause of a query. However, you should let the Query Optimizer

dynamically determine the best access methods to use for each query. Limit your use of

７

Note

The

and

hints are always considered different hints in

this context, regardless of the current transaction isolation level.

and

to specific cases where testing has shown that they improve performance

significantly.

The

option specifies that the Query Optimizer not use any view indexes for

the whole query.

When

is specified for a view, the Query Optimizer considers using any indexes

defined on the view.

specified with the optional

clause forces the

Query Optimizer to use the specified indexes.

can be specified only for an

indexed view and can't be specified for a view not indexed. Automatic use of an indexed

view by the query optimizer is supported only in specific editions of SQL Server. Azure

SQL Database and Azure SQL Managed Instance also support automatic use of indexed

views without specifying the

hint.

When neither

nor

is specified in a query that contains a view, the view

is expanded to access underlying tables. If the query that makes up the view contains any table

hints, these hints are propagated to the underlying tables. (This process is explained in more

detail in View Resolution.) As long as the set of hints that exists on the underlying tables of the

view are identical to each other, the query is eligible to be matched with an indexed view. Most

of the time, these hints will match each other, because they are being inherited directly from

the view. However, if the query references tables instead of views, and the hints applied directly

on these tables aren't identical, then such a query isn't eligible for matching with an indexed

view. If the

,

,

,

,

, or

hints apply to the tables

referenced in the query after view expansion, the query isn't eligible for indexed view matching.

If a table hint in the form of

references a view in a query and you

don't also specify the

hint, the index hint is ignored. To specify use of a particular

index, use

.

Generally, when the Query Optimizer matches an indexed view to a query, any hints specified

on the tables or views in the query are applied directly to the indexed view. If the Query

Optimizer chooses not to use an indexed view, any hints are propagated directly to the tables

referenced in the view. For more information, see View Resolution. This propagation doesn't

apply to join hints. They are applied only in their original position in the query. Join hints aren't

considered by the Query Optimizer when matching queries to indexed views. If a query plan

uses an indexed view that matches part of a query that contains a join hint, the join hint isn't

used in the plan.

Hints aren't allowed in the definitions of indexed views. In compatibility mode 80 and higher,

SQL Server ignores hints inside indexed view definitions when maintaining them, or when

executing queries that use indexed views. Although using hints in indexed view definitions

won't produce a syntax error in 80 compatibility mode, they are ignored.

```sql
GROUP BY
```

```sql
SET
```

```sql
FROM
```

```sql
FROM
```

```sql
EXPAND VIEWS
```

```sql
NOEXPAND
```

```sql
FROM
```

```sql
EXPAND
```

```sql
READCOMMITTED
```

```sql
READCOMMITTEDLOCK
```

```sql
NOEXPAND
```

```sql
EXPAND VIEWS
```

```sql
NOEXPAND
```

```sql
NOEXPAND
```

```sql
INDEX()
```

```sql
NOEXPAND
```

```sql
NOEXPAND
```

```sql
NOEXPAND
```

```sql
EXPAND VIEWS
```

```sql
INDEX
```

```sql
PAGLOCK
```

```sql
ROWLOCK
```

```sql
TABLOCKX
```

```sql
UPDLOCK
```

```sql
XLOCK
```

```sql
INDEX (index_val[ ,...n] )
```

```sql
NOEXPAND
```

```sql
NOEXPAND
```
