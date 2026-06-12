---
title: "Change the schema"
topic: "tables"
description: |
  Applies to:

  SQL Server 2016 (13.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  SQL database in Microsoft Fabric

  Use the

  statement to add, alter, or remove a column.

  permis
tags:
  - "tables"
  - "change-the-schema"
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

Use the

statement to add, alter, or remove a column.

permission on current and history tables is required to change schema of temporal

table.

During an

operation, the system holds a schema lock on both tables.

Specified schema change is propagated to history table appropriately (depending on type of

change).

Adding

,

,

or XML columns with defaults, is an

update data operation on all editions of SQL Server.

If row size after column addition exceeds the row size limit, new columns can't be added

online.

Once you extend a table with a new

column, consider dropping the default constraint

on the history table, as the system automatically populates all columns in that table.

The online option (

) has no effect on

with

temporal tables.

column isn't performed as online, regardless of which value was

specified for

option.

You can use

to change the

property for period columns.

You can't use direct

for the following schema changes. For these types of changes, set.

Adding a computed column

Adding an

column

Adding a

column or changing existing column to be

when the history

table is set to

or

, which is the default

for the history table.

Adding a

```sql
ALTER TABLE
CONTROL
ALTER TABLE
NOT NULL
WITH (ONLINE = ON
ALTER TABLE ALTER COLUMN
ALTER
ONLINE
ALTER COLUMN
IsHidden
ALTER
SYSTEM_VERSIONING = OFF
IDENTITY
SPARSE
SPARSE
DATA_COMPRESSION = PAGE
DATA_COMPRESSION = ROW
COLUMN_SET
```
