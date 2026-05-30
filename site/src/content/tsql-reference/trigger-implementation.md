---
name: "Trigger implementation"
title: "Trigger implementation"
category: "statements"
description: "At least one of the three"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

At least one of the three

clauses must be specified, but they can be specified in any

order. A variable can't be updated more than once in the same

clause.

Any insert, update, or delete action specified on the target table by the

statement are

limited by any constraints defined on it, including any cascading referential integrity

constraints. If

is

for any unique indexes on the target table,

ignores

this setting.

The

statement requires a semicolon (

) as a statement terminator. Error 10713 is raised

when a

statement is run without the terminator.

When used after

,

@@ROWCOUNT (Transact-SQL)

## returns the total number of rows

inserted, updated, and deleted to the client.

is a fully reserved keyword when the database compatibility level is set to

or higher.

The

statement is available under both

and

database compatibility levels;

however, the keyword isn't fully reserved when the database compatibility level is set to

.

For every insert, update, or delete action specified in the

statement, SQL Server fires any

corresponding

triggers defined on the target table, but doesn't guarantee on which

action to fire triggers first or last. Triggers defined for the same action honor the order you

specify. For more information about setting trigger firing order, see

Specify First and Last

Triggers

.

If the target table has an enabled

OF trigger defined on it for an insert, update, or

delete action done by a

statement, it must have an enabled

OF trigger for all of

the actions specified in the

statement.

Ｕ

Caution

Don't use the

statement when using

. The

and

queued updating trigger aren't compatible. Replace the

statement with an

and

statements.

### inserted

### deleted

`MATCHED`

`MATCHED`

`MERGE`

`IGNORE_DUP_KEY`

`ON`

`MERGE`

`MERGE`

```sql
;
```

`MERGE`

`MERGE`

`MERGE`

```sql
100
```

`MERGE`

```sql
90
```

```sql
100
```

```sql
90
```

`MERGE`

`AFTER`

`INSTEAD`

`MERGE`

`INSTEAD`

`MERGE`

```sql
INSERT tbl_A (
col
, col2)
SELECT col
, col2
FROM tbl_B
WHERE
NOT
EXISTS (
SELECT col
FROM tbl_A A2
WHERE
A2.col = tbl_B.col);
```

`MERGE`

`MERGE`

`MERGE`

`INSERT`

`UPDATE`
