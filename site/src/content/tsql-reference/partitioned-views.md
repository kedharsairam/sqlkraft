---
name: "Partitioned views"
title: "Partitioned views"
category: "statements"
description: "A computation."
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

A computation. The column cannot be computed from an expression that uses other

columns. Columns that are formed by using the set operators UNION, UNION ALL,

CROSSJOIN, EXCEPT, and INTERSECT amount to a computation and are also not

updatable.

The columns being modified are not affected by

,

, or

clauses.

TOP is not used anywhere in the

select_statement

of the view together with the

clause.

The previous restrictions apply to any subqueries in the FROM clause of the view, just as they

apply to the view itself. Generally, the Database Engine must be able to unambiguously trace

modifications from the view definition to one base table. For more information, see

Modify

Data Through a View.

If the previous restrictions prevent you from modifying data directly through a view, consider

the following options:

triggers can be created on a view to make a view updatable. The

trigger is executed instead of the data modification statement on which the trigger is

defined. This trigger lets the user specify the set of actions that must happen to process

the data modification statement. Therefore, if an

trigger exists for a view on a

specific data modification statement (

,

, or

), the corresponding view

is updatable through that statement. For more information about

triggers,

see

DML Triggers.

If the view is a partitioned view, the view is updatable, subject to certain restrictions.

When it is needed, the Database Engine distinguishes local partitioned views as the views

in which all participating tables and the view are on the same instance of SQL Server, and

distributed partitioned views as the views in which at least one of the tables in the view

resides on a different or remote server.

A partitioned view is a view defined by a

of member tables structured in the same

way, but stored separately as multiple tables in either the same instance of SQL Server or in a

group of autonomous instances of SQL Server servers, called federated database servers.

## Partitioned Tables and Indexes

```sql
GROUP BY
```

`HAVING`

`DISTINCT`

```sql
WITH
CHECK OPTION
```

```sql
INSTEAD OF
```

```sql
INSTEAD OF
```

```sql
INSTEAD OF
```

`INSERT`

`UPDATE`

`DELETE`

```sql
INSTEAD OF
```

```sql
UNION ALL
```
