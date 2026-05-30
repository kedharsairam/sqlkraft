---
name: "Updatable views"
title: "Updatable views"
category: "statements"
description: "When a view is created, information about the view is stored in the following catalog views:"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

When a view is created, information about the view is stored in the following catalog views:

sys.views

,

sys.columns

, and

sys.sql_expression_dependencies

. The text of the

statement is stored in the

sys.sql_modules

catalog view.

A query that uses an index on a view defined with

or

expressions might have a

result that is different from a similar query that does not use the index on the view. This

difference can be caused by rounding errors during

,

, or

actions on

underlying tables.

The Database Engine saves the settings of

and

when a

view is created. These original settings are used to parse the view when the view is used.

Therefore, any client-session settings for

and

do not

affect the view definition when the view is accessed.

In Azure Synapse Analytics, views do not support schema binding. Therefore, if changes are

made to the underlying objects, you should drop and recreate the view to refresh the

underlying metadata. For more information, see

T-SQL views with dedicated SQL pool and

serverless SQL pool in Azure Synapse Analytics

.

In Azure Synapse Analytics, updatable views, DML triggers (of either type

or

),

and partitioned views are not supported. For more information, see

T-SQL views with

dedicated SQL pool and serverless SQL pool in Azure Synapse Analytics

.

In Azure Synapse Analytics, partitioned views are not supported. For more information, see

T-

SQL views with dedicated SQL pool and serverless SQL pool in Azure Synapse Analytics

.

In Fabric SQL database, views can be created, but they are not

mirrored into the Fabric

OneLake

. For more information, see

Limitations of Fabric SQL database mirroring

.

You can modify the data of an underlying base table through a view, as long as the following

conditions are true:

Any modifications, including

,

, and

statements, must reference

columns from only one base table.

The columns being modified in the view must directly reference the underlying data in

the table columns. The columns cannot be derived in any other way, such as through the

following:

An aggregate function:

,

,

,

,

,

,

,

,

, and

.

### INSTEAD OF triggers

### Partitioned views

```sql
CREATE VIEW
```

```sql
INSERT
```

```sql
DELETE
```

```sql
UPDATE
```

```sql
SET QUOTED_IDENTIFIER
```

```sql
SET ANSI_NULLS
```

```sql
SET QUOTED_IDENTIFIER
```

```sql
SET ANSI_NULLS
```

```sql
AFTER
```

```sql
INSTEAD OF
```

```sql
UPDATE
```

```sql
INSERT
```

```sql
DELETE
```

```sql
AVG
```

```sql
COUNT
```

```sql
SUM
```

```sql
MIN
```

```sql
MAX
```

```sql
GROUPING
```

```sql
STDEV
```

```sql
STDEVP
```

```sql
VAR
```

```sql
VARP
```
