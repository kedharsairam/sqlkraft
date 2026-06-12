---
name: "Temporary tables"
title: "Temporary tables"
category: "statements"
description: ""
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

The Database Engine doesn't enforce an order in which DEFAULT, IDENTITY, ROWGUIDCOL, or

column constraints are specified in a column definition.

When a table is created, the QUOTED IDENTIFIER option is always stored as ON in the

metadata for the table, even if the option is set to OFF when the table is created.

In SQL database in Microsoft Fabric, some table features can be created but aren't

mirrored

into the Fabric OneLake. For more information, see

Limitations for Fabric SQL database

mirroring.

You can create local and global temporary tables. Local temporary tables are visible only in the

current session, and global temporary tables are visible to all sessions. Temporary tables can't

be partitioned.

Prefix local temporary table names with single number sign (

), and prefix global

temporary table names with a double number sign (

).

Transact-SQL statements reference the temporary table by using the value specified for

table_name

in the

statement, for example:

If more than one temporary table is created inside a single stored procedure or batch, they

must have different names.

If you include a

schema_name

when you create or access a temporary table, it's ignored. All

temporary tables are created in the

schema.

If a local temporary table is created in a stored procedure or a SQL module that can be

executed at the same time by several sessions, the Database Engine must be able to distinguish

the tables created by the different sessions. The Database Engine does this by internally

appending a unique suffix to each local temporary table name. The full name of a temporary

table as stored in the

table in

is made up of the table name specified in

the

statement and the system-generated unique suffix. To allow for the suffix,

table_name

specified for a local temporary name can't exceed 116 characters.

### ON

### OFF

Temporary tables are automatically dropped when they go out of scope, unless explicitly

dropped earlier by using

:

A local temporary table created in a stored procedure is dropped automatically when the

stored procedure is finished. The table can be referenced by any nested stored

procedures executed by the stored procedure that created the table. The table can't be

referenced by the process that called the stored procedure that created the table.

All other local temporary tables are dropped automatically at the end of the current

session.

If the

database-scoped configuration is set to

(default), then global temporary tables are automatically dropped when the session that

created the table ends and all other tasks have stopped referencing them. The association

between a task and a table is maintained only for the life of a single Transact-SQL

statement. This means that a global temporary table is dropped at the completion of the

last Transact-SQL statement that was actively referencing the table when the creating

session ended.

If the

database-scoped configuration is set to

,

then global temporary tables are only dropped using

, or when the Database

Engine instance restarts. For more information, see

GLOBAL_TEMPORARY_TABLE_AUTO_DROP.

A local temporary table created within a stored procedure or trigger can have the same name

as a temporary table that was created before the stored procedure or trigger is called.

However, if a query references a temporary table and two temporary tables with the same

name exist at that time, it isn't defined which table the query is resolved against. Nested stored

procedures can also create temporary tables with the same name as a temporary table that was

created by the calling stored procedure. However, for modifications to resolve to the table that

was created in the nested procedure, the table must have the same structure, with the same

column names, as the table created in the calling procedure. This is shown in the following

example.

Here's the result set.

Output

When you create local or global temporary tables, the

## syntax supports constraint

definitions except for

constraints. If a

constraint is specified in a

temporary table, the statement returns a warning message that states the constraint was

skipped. The table is still created without the

constraint. Temporary tables can't be

referenced in

constraints.

If a temporary table is created with a named constraint and the temporary table is created

within the scope of a user-defined transaction, only one user at a time can execute the

## Database scoped global temporary tables in Azure SQL

## Database

## Permissions for temporary objects

```sql
#table_name
```

```sql
##table_name
```

```sql
CREATE TABLE
```

`dbo`

`sys.objects`

`tempdb`

```sql
CREATE TABLE
```

```sql
CREATE
TABLE
#MyTempTable (
col1
INT
PRIMARY
KEY
);
INSERT
INTO
#MyTempTable
VALUES (1);
```

```sql
DROP TABLE
```

`GLOBAL_TEMPORARY_TABLE_AUTO_DROP`

`GLOBAL_TEMPORARY_TABLE_AUTO_DROP`

```sql
DROP TABLE
```

```sql
CREATE
PROCEDURE dbo.Test2
AS
CREATE
TABLE
#t (
x
INT
PRIMARY
KEY
);
INSERT
INTO
#t
VALUES (2);
SELECT x
AS
Test2Col
FROM
#t;
GO
```

```sql
CREATE TABLE
```

```sql
FOREIGN KEY
```

```sql
FOREIGN KEY
```

```sql
FOREIGN KEY
```

```sql
FOREIGN KEY
```

```sql
CREATE
PROCEDURE dbo.Test1
AS
CREATE
TABLE
#t (
x
INT
PRIMARY
KEY
);
INSERT
INTO
#t
VALUES (1);
SELECT x
AS
Test1Col
FROM
#t;
EXECUTE
Test2;
GO
CREATE
TABLE
#t (
x
INT
PRIMARY
KEY
);
INSERT
INTO
#t
VALUES (99);
GO
EXECUTE
Test1;
GO (1 row(s) affected)
Test1Col
-----------
1 (1 row(s) affected)
Test2Col
-----------
2
```
