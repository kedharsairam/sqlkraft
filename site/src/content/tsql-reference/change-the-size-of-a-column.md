---
name: "Change the size of a column"
title: "Change the size of a column"
category: "statements"
description: "or online index rebuild DDL operation currently being run without taking"
tags: ["tsql","statements"]
pubDate: 2026-05-29
---

Exit the

or online index rebuild DDL operation currently being run without taking

any action.

BLOCKERS

Kill all user transactions that currently block the

or online index rebuild DDL

operation so that the operation can continue.

Requires

permission.

: SQL Server 2016 (13.x) and later versions, and Azure SQL Database.

Conditionally drops the column or constraint only if it already exists.

: SQL Server 2022 (16.x) and later versions.

Specifies whether an

operation is resumable. Add table constraint

operation is resumable when. Add table constraint operation isn't resumable when.

Default is. The

option can be used as part of the

ALTER TABLE index_option

(Transact-SQL)

in the

ALTER TABLE table_constraint (Transact-SQL).

when used with

(requires

) indicates time (an integer

value specified in minutes) that a resumable online add constraint operation is executed before

being paused. If not specified, the operation continues until completion.

For more information on enabling and using resumable

operations,

see

Resumable add table constraints.

To add new rows of data, use

INSERT (Transact-SQL). To remove rows of data, use

DELETE

(Transact-SQL)

or

TRUNCATE TABLE (Transact-SQL). To change the values in existing rows, use

UPDATE (Transact-SQL).

If there are any execution plans in the procedure cache that reference the table,

marks them to be recompiled on their next execution.

`SWITCH`

`SWITCH`

```sql
ALTER ANY CONNECTION
```

```sql
ALTER TABLE ADD CONSTRAINT
```

`ON`

`OFF`

`OFF`

`RESUMABLE`

`MAX_DURATION`

```sql
RESUMABLE = ON
```

```sql
ONLINE = ON
```

```sql
ALTER TABLE ADD CONSTRAINT
```

```sql
ALTER TABLE
```
