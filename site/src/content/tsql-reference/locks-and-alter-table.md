---
name: "Locks and ALTER TABLE"
title: "Locks and ALTER TABLE"
category: "statements"
description: "You can change the length, precision, or scale of a column by specifying a new size for the"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## Extended Events (XEvents) for partition switch

## Add NOT NULL columns as an online operation

You can change the length, precision, or scale of a column by specifying a new size for the

column data type. Use the

clause. If data exists in the column, the new size can't be

smaller than the maximum size of the data. Also, you can't define the column in an index, unless

the column is a

,

, or

data type and the index isn't the result of a

constraint. See the example in the short section titled

Altering a Column Definition

.

Changes you specify in

take effect immediately. If the changes require modifications

to the rows in the table,

updates the rows.

acquires a schema modify

(Sch-M) lock on the table to ensure that no other connections reference even the metadata for

the table during the change, except online index operations that require a short Sch-M lock at

the end. In an

operation, the lock is acquired on both the source and

target tables. The modifications made to the table are logged and fully recoverable. Changes that

affect all the rows in large tables, such as dropping a column or, on some editions of SQL Server,

adding a

column with a default value, can take a long time to complete and generate

many log records. Run these

statements with the same care as any

,

,

or

statement that affects many rows.

The following XEvents are related to

and

online index

rebuilds

.

lock_request_priority_state

process_killed_by_abort_blockers

ddl_with_wait_at_low_priority

In SQL Server 2012 (11.x) Enterprise edition and later versions, adding a

column with a

default value is an online operation when the default value is a

runtime constant

. This default

behavior means that the operation finishes almost instantaneously despite the number of rows in

the table, because the existing rows in the table aren't updated during the operation. Instead, the

default value is stored only in the metadata of the table and the value is looked up, as needed, in

queries that access these rows. This behavior is automatic. No additional syntax is required to

implement the online operation beyond the

## syntax. A runtime constant is an

expression that produces the same value at runtime for each row in the table despite its

determinism. For example, the constant expression

, or the system function

### varchar(max)

### nvarchar(max)

### varbinary(max)

```sql
ALTER COLUMN
```

```sql
PRIMARY KEY
```

```sql
ALTER TABLE
```

```sql
ALTER TABLE
```

```sql
ALTER TABLE
```

```sql
ALTER TABLE...SWITCH
```

```sql
NOT NULL
```

```sql
ALTER TABLE
```

`INSERT`

`UPDATE`

`DELETE`

```sql
ALTER TABLE ... SWITCH PARTITION
```

```sql
NOT NULL
```

```sql
ADD COLUMN
```

```sql
"My temporary data"
```
