---
name: "Marked transactions"
title: "Marked transactions"
category: "statements"
description: "option causes the transaction name to be recorded in the transaction log. When"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

The

option causes the transaction name to be recorded in the transaction log. When

you restore a database to an earlier state, the marked transaction can be used to specify the

restore point instead of a date and time. For more information, see

Use Marked Transactions to

Recover Related Databases Consistently

and

RESTORE Statements

.

Additionally, transaction log marks are necessary if you need to recover a set of related

databases to a certain shared state of consistency. An application that is aware of the

consistency state of every database can place marks in the transaction logs of the related

databases using a cross-database or a distributed transaction. Recovering the set of related

databases to these marks results in a set of databases that have a known shared state of

consistency.

The mark is placed in the transaction log only if the database is updated by the marked

transaction. Transactions that don't modify data aren't recorded in the log.

can be used when starting an inner transaction. In

that case,

becomes the mark name for the transaction if the outer transaction isn't

marked. In the following conceptual example,

is the name of the mark.

SQL

When you mark an inner transaction, you receive the following warning message if you try to

mark a transaction that is already marked:

Output

### Applies to

### Applies to

```sql
WITH MARK
```

```sql
BEGIN TRANSACTION <new_name> WITH MARK
```

```sql
<new_name>
```

```sql
M2
```

```sql
BEGIN
TRAN T1;
UPDATE
table1 ...;
BEGIN
TRAN M2
WITH
MARK;
UPDATE
table2 ...;
SELECT
column1
FROM
table1;
COMMIT
TRAN M2;
UPDATE
table3 ...;
COMMIT
TRAN T1;
Server: Msg 3920, Level 16, State 1, Line 3
WITH MARK option only applies to the first BEGIN TRAN WITH MARK.
```
