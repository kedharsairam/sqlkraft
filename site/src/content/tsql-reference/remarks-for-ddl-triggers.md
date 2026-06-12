---
name: "Remarks for DDL triggers"
title: "Remarks for DDL triggers"
category: "statements"
description: ""
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

Switch partitions.

Add or drop

or

constraints.

Triggers work in transactions (implied or otherwise) and while they're open, they lock

resources. The lock remains in place until the transaction is confirmed (with

) or rejected

(with a

). The longer a trigger runs, the higher the probability that another process is

then blocked. So, write triggers to lessen their duration whenever possible. One way to achieve

shorter duration is to release a trigger when a DML statement changes zero rows.

To release the trigger for a command that doesn't change any rows, employ the system

variable

ROWCOUNT_BIG.

The following T-SQL code snippet shows how to release the trigger for a command that

doesn't change any rows. This code should be present at the beginning of each DML trigger:

DDL triggers, like standard triggers, launch stored procedures in response to an event. But,

unlike standard triggers, they don't run in response to

,

, or

statements

on a table or view. Instead, they primarily run in response to data definition language (DDL)

statements. The statement types include

,

,

,

,

,

, and. Certain system stored procedures that carry out DDL-like operations can also fire

DDL triggers.

７

Note

Because SQL Server doesn't support user-defined triggers on system tables, we

recommend that you don't create user-defined triggers on system tables.

）

Important

Test your DDL triggers to determine their responses to system stored procedure

execution. For example, the

statement and the

and

### sysadmin

### sysadmin

### Triggers

### Server Objects

### Database Triggers

### Programmability

```sql
PRIMARY KEY
```

`UNIQUE`

`COMMIT`

`ROLLBACK`

`UPDATE`

`INSERT`

`DELETE`

`CREATE`

`ALTER`

`DROP`

`GRANT`

`DENY`

`REVOKE`

```sql
UPDATE
STATISTICS
```

```sql
IF (ROWCOUNT_BIG() = 0)
RETURN;
```

```sql
CREATE TYPE
```

`sp_addtype`

`sp_rename`
