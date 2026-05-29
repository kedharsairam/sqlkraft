---
title: 'Guidelines for using forced parameterization'
topic: 'io-fundamentals'
description: 'Fixed-point numeric literals that are parts of predicates that involve comparison operators'
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

Fixed-point numeric literals that are parts of predicates that involve comparison operators

parameterize to numeric whose precision is 38 and whose scale is just large enough to

support its size. Fixed-point numeric literals that aren't parts of predicates that involve

comparison operators parameterize to numeric whose precision and scale are just large

enough to support its size.

Floating point numeric literals parameterize to float(53).

Non-Unicode string literals parameterize to varchar(8000) if the literal fits within 8,000

characters, and to varchar(max) if it is larger than 8,000 characters.

Unicode string literals parameterize to nvarchar(4000) if the literal fits within 4,000

Unicode characters, and to nvarchar(max) if the literal is larger than 4,000 characters.

Binary literals parameterize to varbinary(8000) if the literal fits within 8,000 bytes. If it is

larger than 8,000 bytes, it is converted to varbinary(max).

Money type literals parameterize to money.

Consider the following when you set the

option to FORCED:

Forced parameterization, in effect, changes the literal constants in a query to parameters

when compiling a query. Therefore, the Query Optimizer can choose suboptimal plans for

queries. In particular, the Query Optimizer is less likely to match the query to an indexed

view or an index on a computed column. It might also choose suboptimal plans for

queries posed on partitioned tables and distributed partitioned views. Forced

parameterization shouldn't be used for environments that rely heavily on indexed views

and indexes on computed columns. Generally, the

option

should only be used by experienced database professionals after determining that doing

this doesn't adversely affect performance.

Distributed queries that reference more than one database are eligible for forced

parameterization as long as the

option is set to

in the database

whose context the query is running.

Setting the

option to

flushes all query plans from the plan

cache of a database, except those that currently are compiling, recompiling, or running.

Plans for queries that are compiling or running during the setting change are

parameterized the next time the query is executed.

Setting the

option is an online operation that it requires no database-

level exclusive locks.

The current setting of the

option is preserved when reattaching or

restoring a database.

You can override the behavior of forced parameterization by specifying that simple

parameterization be attempted on a single query, and any others that are syntactically

```sql
PARAMETERIZATION
```

```sql
PARAMETERIZATION FORCED
```

```sql
PARAMETERIZATION
```

```sql
FORCED
```

```sql
PARAMETERIZATION
```

```sql
FORCED
```

```sql
PARAMETERIZATION
```

```sql
PARAMETERIZATION
```
