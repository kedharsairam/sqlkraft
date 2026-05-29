---
name: 'views'
title: 'views'
category: 'statements'
description: 'The value being inserted into the partitioning column satisfies at least one of the'
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

The value being inserted into the partitioning column satisfies at least one of the

underlying constraints; otherwise, the insert action fails with a constraint violation.

statements cannot specify the

keyword as a value in the

clause, even

if the column has a

value defined in the corresponding member table.

Columns in the view that are an identity column in one or more of the member tables

cannot be modified by using an

or

statement.

If one of the member tables contains a

column, the data cannot be modified

by using an

or

statement.

If one of the member tables contains a trigger or an

or

constraint, the view cannot be

modified.

,

, and

actions against a partitioned view are not allowed if there is a

self-join with the same view or with any of the member tables in the statement.

Bulk importing data into a partitioned view is unsupported by

or the

and

statements. However, you can insert

multiple rows into a partitioned view by using the

INSERT

statement.

For distributed partitioned views (when one or more member tables are remote), the following

additional conditions apply:

A distributed transaction is started to guarantee atomicity across all nodes affected by the

update.

Set the

option to

for

,

, or

statements to work.

Any columns in remote tables of type

that are referenced in a partitioned

view are mapped as

. Therefore, the corresponding columns (in the same ordinal

position in the select list) in the local tables must also be of type

.

７

Note

To update a partitioned view, the user must have

,

, and


## permissions on the member tables.
### smalldatetime

### smalldatetime

### smalldatetime

### smalldatetime

### datetime

### datetime

### uniqueidentifier

### uniqueidentifier

### uniqueidentifier

```sql
UPDATE
```

```sql
DEFAULT
```

```sql
SET
```

```sql
DEFAULT
```

```sql
INSERT
```

```sql
UPDATE
```

```sql
INSERT
```

```sql
UPDATE
```

```sql
ON UPDATE CASCADE/SET NULL/SET
DEFAULT
```

```sql
ON DELETE CASCADE/SET NULL/SET DEFAULT
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
bcp
```

```sql
BULK INSERT
```

```sql
INSERT ... SELECT * FROM OPENROWSET(BULK...)
```

```sql
XACT_ABORT SET
```

```sql
ON
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
INSERT
```

```sql
UPDATE
```

```sql
DELETE
```
