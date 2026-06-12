---
name: "Conditions for modifying data in partitioned views"
title: "Conditions for modifying data in partitioned views"
category: "predicates"
description: ""
tags: ["tsql","predicates"]
pubDate: 2026-05-29
---

It cannot be a computed, identity, default, or

column.

If there is more than one constraint on the same column in a member table, the

Database Engine ignores all the constraints and does not consider them when

determining whether the view is a partitioned view. To meet the conditions of the

partitioned view, ensure that there is only one partitioning constraint on the

partitioning column.

There are no restrictions on the updatability of the partitioning column.

3. Member tables, or underlying tables

The tables can be either local tables or tables from other computers that are running

that are referenced either through a four-part name or an

OPENDATASOURCE- or OPENROWSET-based name. The OPENDATASOURCE and

OPENROWSET syntax can specify a table name, but not a pass-through query. For

more information, see

OPENDATASOURCE (Transact-SQL)

and

OPENROWSET

(Transact-SQL).

If one or more of the member tables are remote, the view is called distributed

partitioned view, and additional conditions apply. They are described later in this

section.

The same table cannot appear two times in the set of tables that are being

combined with the

statement.

The member tables cannot have indexes created on computed columns in the table.

The member tables have all PRIMARY KEY constraints on the same number of

columns.

All member tables in the view have the same ANSI padding setting. This can be set

by using either the

option in

or the SET statement.

The following restrictions apply to statements that modify data in partitioned views:

The

statement supplies values for all the columns in the view, even if the

underlying member tables have a

constraint for those columns or if they allow

for

values. For those member table columns that have

definitions, the

statements cannot explicitly use the keyword.

```sql
T1,., Tn
```

```sql
UNION ALL
```

`sp_configure`

`INSERT`

`DEFAULT`

`NULL`

`DEFAULT`

`DEFAULT`
