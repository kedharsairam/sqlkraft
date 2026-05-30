---
name: "Remarks for DML triggers"
title: "Remarks for DML triggers"
category: "statements"
description: "For a CLR trigger, specifies the method of an assembly to bind with the trigger. The method"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

For a CLR trigger, specifies the method of an assembly to bind with the trigger. The method

must take no arguments and return void.

class_name

must be a valid SQL Server identifier and

must exist as a class in the assembly with assembly visibility. If the class has a namespace-

qualified name that uses

to separate namespace parts, the class name must be delimited by

using [ ] or " " delimiters. The class can't be a nested class.

DML triggers are frequently used for enforcing business rules and data integrity. SQL Server

provides declarative referential integrity (DRI) through the

and

statements. However, DRI doesn't provide cross-database referential integrity. Referential

integrity refers to the rules about the relationships between the primary and foreign keys of

tables. To enforce referential integrity, use the

and

constraints in

and

. If constraints exist on the trigger table, they're checked after

the

trigger runs and before the

trigger runs. If the constraints are violated,

the

trigger actions are rolled back and the

trigger isn't fired.

You can specify the first and last

triggers to be run on a table by using

. You can specify only one first and one last

trigger for each

,

, and

operation on a table. If there are other

triggers on the same table,

they're randomly run.

If an

statement changes a first or last trigger, the first or last attribute set on the

modified trigger is dropped, and you must reset the order value by using

.

An

trigger is run only after the triggering SQL statement runs successfully. This

successful execution includes all referential cascade actions and constraint checks associated

with the object updated or deleted. An

doesn't recursively fire an

trigger on

the same table.

If an

trigger defined on a table runs a statement against the table that would

ordinarily fire the

trigger again, the trigger isn't called recursively. Instead, the

statement processes as if the table had no

trigger and starts the chain of constraint

７

Note

By default, the ability of SQL Server to run CLR code is off. You can create, modify, and

drop database objects that reference managed code modules, but these references don't

run in an instance of SQL Server unless the

option is enabled with

.

## Test for UPDATE or INSERT actions to specific columns

## Trigger limitations

operations and

trigger executions. For example, if a trigger is defined as an

trigger for a table. And, if the trigger runs an

statement on the same table, the

statement launched by the

trigger doesn't call the trigger again. The

launched by the trigger starts the process of running constraint actions and firing any

triggers defined for the table.

When an

trigger defined on a view runs a statement against the view that would

ordinarily fire the

trigger again, it's not called recursively. Instead, the statement is

resolved as modifications against the base tables underlying the view. In this case, the view

definition must meet all the restrictions for an updatable view. For a definition of updatable

views, see

Modify Data Through a View

.

For example, if a trigger is defined as an

trigger for a view. And, the trigger

runs an

statement referencing the same view, the

statement launched by the

trigger doesn't call the trigger again. The

launched by the trigger is

processed against the view as if the view didn't have an

trigger. The columns

changed by the

must be resolved to a single base table. Each modification to an

underlying base table starts the chain of applying constraints and firing

triggers defined

for the table.

You can design a Transact-SQL trigger to do certain actions based on

or

modifications to specific columns. Use

UPDATE

or

COLUMNS_UPDATED

in the body of the

trigger for this purpose.

tests for

or

attempts on one column.

tests for

or

actions that run on multiple columns. This function

## returns a bit pattern that indicates which columns were inserted or updated.

must be the first statement in the batch and can apply to only one table.

A trigger is created only in the current database; however, a trigger can reference objects

outside the current database.

If the trigger schema name is specified to qualify the trigger, qualify the table name in the

same way.

The same trigger action can be defined for more than one user action (for example,

and

) in the same

statement.

/

triggers can't be defined on a table that has a foreign

key with a cascade on

/

action defined.

Any SET statement can be specified inside a trigger. The SET option selected remains in effect

during the execution of the trigger and then reverts to its former setting.

When a trigger fires, results are returned to the calling application, just like with stored

procedures. To prevent results being returned to an application because of a trigger firing,

don't include either

statements that return results or statements that carry out variable

assignment in a trigger. A trigger that includes either

statements that return results to

the user or statements that do variable assignment, requires special handling. You'd have to

write the returned results into every application in which modifications to the trigger table are

allowed. If variable assignment must occur in a trigger, use a

statement at the

start of the trigger to prevent the return of any result sets.

Although a

statement is in effect a

statement, it doesn't activate a

trigger because the operation doesn't log individual row deletions. However, only those users

with permissions to run a

statement need be concerned about inadvertently

circumventing a

trigger this way.

The

statement, whether logged or unlogged, doesn't activate a trigger.

The following Transact-SQL statements aren't allowed in a DML trigger:

Additionally, the following Transact-SQL statements aren't allowed inside the body of a DML

trigger when it's used against the table or view that's the target of the triggering action.

(including

and

)

when used to do the following actions:

Add, modify, or drop columns.

## Optimize DML triggers

```sql
.
```

```sql
ALTER TABLE
```

```sql
CREATE TABLE
```

```sql
PRIMARY KEY
```

```sql
FOREIGN KEY
```

```sql
ALTER TABLE
```

```sql
CREATE TABLE
```

```sql
INSTEAD OF
```

```sql
AFTER
```

```sql
INSTEAD OF
```

```sql
AFTER
```

```sql
AFTER
```

```sql
sp_settriggerorder
```

```sql
AFTER
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
AFTER
```

```sql
ALTER TRIGGER
```

```sql
sp_settriggerorder
```

```sql
AFTER
```

```sql
AFTER
```

```sql
INSTEAD OF
```

```sql
INSTEAD OF
```

```sql
INSTEAD OF
```

```sql
INSTEAD OF
```

```sql
AFTER
```

```sql
INSTEAD OF
INSERT
```

```sql
INSERT
```

```sql
INSERT
```

```sql
INSTEAD OF
```

```sql
INSERT
```

```sql
AFTER INSERT
```

```sql
INSTEAD OF
```

```sql
INSTEAD OF
```

```sql
INSTEAD OF UPDATE
```

```sql
UPDATE
```

```sql
UPDATE
```

```sql
INSTEAD OF
```

```sql
UPDATE
```

```sql
INSTEAD OF
```

```sql
UPDATE
```

```sql
AFTER
```

```sql
UPDATE
```

```sql
INSERT
```

```sql
UPDATE()
```

```sql
UPDATE
```

```sql
INSERT
```

```sql
COLUMNS_UPDATED
```

```sql
UPDATE
```

```sql
INSERT
```

```sql
CREATE TRIGGER
```

```sql
INSERT
```

```sql
UPDATE
```

```sql
CREATE TRIGGER
```

```sql
INSTEAD OF DELETE
```

```sql
INSTEAD OF UPDATE
```

```sql
DELETE
```

```sql
UPDATE
```

```sql
SELECT
```

```sql
SELECT
```

```sql
SET NOCOUNT
```

```sql
TRUNCATE TABLE
```

```sql
DELETE
```

```sql
TRUNCATE TABLE
```

```sql
DELETE
```

```sql
WRITETEXT
```

```sql
ALTER DATABASE
CREATE DATABASE
DROP DATABASE
RESTORE DATABASE
RESTORE LOG
RECONFIGURE
```

```sql
CREATE INDEX
```

```sql
CREATE SPATIAL INDEX
```

```sql
CREATE XML INDEX
```

```sql
ALTER INDEX
DROP INDEX
DROP TABLE
DBCC DBREINDEX
ALTER PARTITION FUNCTION
ALTER TABLE
```
