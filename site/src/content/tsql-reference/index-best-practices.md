---
name: 'Index best practices'
title: 'Index best practices'
category: 'hints'
description: 'triggers are defined on'
tags: ["tsql", "hints"]
pubDate: 2026-05-29
---

If any

OF

or

OF

triggers are defined on

target_table

, the

update or delete operations aren't run. Instead, the triggers fire and the

and

tables then populate accordingly.

If any

OF

triggers are defined on

target_table

, the insert operation isn't

performed. Instead, the table populates accordingly.

Requires

permission on the source table and

,

, or


## permissions on
the target table. For more information, see the Permissions section in the

SELECT (Transact-

SQL)

,

INSERT (Transact-SQL)

,

UPDATE (Transact-SQL)

, and

DELETE (Transact-SQL)

articles.

By using the

statement, you can replace the individual DML statements with a single

statement. This can improve query performance because the operations are performed within a

single statement, therefore, minimizing the number of times the data in the source and target

tables are processed. However, performance gains depend on having correct indexes, joins,

and other considerations in place.

To improve the performance of the

statement, we recommend the following index

guidelines:

Create indexes to facilitate the join between the source and target of the

:

Create an index on the join columns in the source table that has keys covering the join

logic to the target table. If possible, it should be unique.

Also, create an index on the join columns in the target table. If possible, it should be a

unique clustered index.

These two indexes ensure that the data in the tables is sorted, and uniqueness aids

performance of the comparison. Query performance is improved because the query

７

Note

Unlike separate

,

, and

statements, the number of rows reflected by

inside of a trigger might be higher. The

inside any

trigger

(regardless of data modification statements the trigger captures) will reflect the total

number of rows affected by the

. For example, if a

statement inserts one row,

updates one row, and deletes one row,

will be three for any

trigger,

even if the trigger is only declared for

statements.

```sql
INSTEAD
```

```sql
UPDATE
```

```sql
INSTEAD
```

```sql
DELETE
```

```sql
INSTEAD
```

```sql
INSERT
```

```sql
SELECT
```

```sql
INSERT
```

```sql
UPDATE
```

```sql
DELETE
```

```sql
MERGE
```

```sql
MERGE
```

```sql
MERGE
```

```sql
INSERT
```

```sql
UPDATE
```

```sql
DELETE
```

```sql
@@ROWCOUNT
```

```sql
@@ROWCOUNT
```

```sql
AFTER
```

```sql
MERGE
```

```sql
MERGE
```

```sql
@@ROWCOUNT
```

```sql
AFTER
```

```sql
INSERT
```
