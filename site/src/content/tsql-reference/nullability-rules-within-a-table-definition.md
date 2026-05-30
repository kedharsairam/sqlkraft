---
name: "Nullability rules within a table definition"
title: "Nullability rules within a table definition"
category: "data-types"
description: "A column-level CHECK constraint can reference only the constrained column, and a table-"
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

A column-level CHECK constraint can reference only the constrained column, and a table-

level CHECK constraint can reference only columns in the same table.

CHECK CONSTRAINTS and rules serve the same function of validating the data during

INSERT and UPDATE statements.

When a rule and one or more CHECK constraints exist for a column or columns, all

restrictions are evaluated.

CHECK constraints can't be defined on

,

, or

columns.

An index created for a constraint can't be dropped by using

; the constraint

must be dropped by using

. An index created for and used by a constraint

can be rebuilt by using

. For more information, see

Optimize

index maintenance to improve query performance and reduce resource consumption

.

Constraint names must follow the rules for

identifiers

, except that the name can't start

with a number sign (#). If

constraint_name

isn't supplied, a system-generated name is

assigned to the constraint. The constraint name appears in any error message about

constraint violations.

When a constraint is violated in an

,

, or

statement, the statement is

ended. However, when

is set to OFF, the transaction, if the statement is

part of an explicit transaction, continues to be processed. When

is set to

ON, the whole transaction is rolled back. You can also use the

statement with the transaction definition by checking the

system function.

When

and

, row-, page-, and table-level locks

are allowed when you access the index. The Database Engine chooses the appropriate

lock and can escalate the lock from a row or page lock to a table lock. When

and

, only a table-level lock is allowed

when you access the index.

If a table has FOREIGN KEY or CHECK CONSTRAINTS and triggers, the constraint

conditions are evaluated before the trigger is executed.

For a report on a table and its columns, use

or

. To rename a table,

use

. For a report on the views and stored procedures that depend on a table, use

sys.dm_sql_referenced_entities

and

sys.dm_sql_referencing_entities

.

#### Column data

#### type

#### Rule

#### timestamp

### AllowsNull

The nullability of a column determines whether that column can allow a null value (

) as the

data in that column.

isn't zero or blank:

means no entry was made or an explicit

was supplied, and it typically implies that the value is either unknown or not applicable.

When you use

or

to create or alter a table, database and session

settings influence and possibly override the nullability of the data type that is used in a column

definition. We recommend that you always explicitly define a column as NULL or NOT NULL for

noncomputed columns or, if you use a user-defined data type, that you allow the column to

use the default nullability of the data type. Sparse columns must always allow NULL.

When column nullability isn't explicitly specified, column nullability follows the rules shown in

the following table.

Alias data type

The Database Engine uses the nullability that is specified when the data type was

created. To determine the default nullability of the data type, use

.

CLR user-

defined type

Nullability is determined according to the column definition.

System-

supplied data

type

If the system-supplied data type has only one option, it takes precedence.

data types must be NOT NULL. When any session settings are set ON by using

:

, NULL is assigned.

, NOT NULL is assigned.

When any database settings are configured by using

:

, NULL is assigned.

, NOT NULL is assigned.

To view the database setting for

, use the

catalog

view

When neither of the ANSI_NULL_DFLT options is set for the session and the database is set to

the default (ANSI_NULL_DEFAULT is OFF), the default of NOT NULL is assigned.

If the column is a computed column, its nullability is always automatically determined by the

Database Engine. To find out the nullability of this type of column, use the

function with the

property.



Expand table

７

Note

```sql
DROP INDEX
```

```sql
ALTER TABLE
```

```sql
ALTER INDEX ... REBUILD
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
SET XACT_ABORT
```

```sql
SET XACT_ABORT
```

```sql
ROLLBACK TRANSACTION
```

```sql
@@ERROR
```

```sql
ALLOW_ROW_LOCKS = ON
```

```sql
ALLOW_PAGE_LOCK = ON
```

```sql
ALLOW_ROW_LOCKS = OFF
```

```sql
ALLOW_PAGE_LOCK = OFF
```

```sql
sp_help
```

```sql
sp_helpconstraint
```

```sql
sp_rename
```

```sql
NULL
```

```sql
NULL
```

```sql
NULL
```

```sql
NULL
```

```sql
CREATE TABLE
```

```sql
ALTER TABLE
```

```sql
sp_help
```

```sql
SET
```

```sql
ANSI_NULL_DFLT_ON = ON
```

```sql
ANSI_NULL_DFLT_OFF = ON
```

```sql
ALTER DATABASE
```

```sql
ANSI_NULL_DEFAULT_ON = ON
```

```sql
ANSI_NULL_DEFAULT_OFF = ON
```

```sql
ANSI_NULL_DEFAULT
```

```sql
sys.databases
```

```sql
COLUMNPROPERTY
```
