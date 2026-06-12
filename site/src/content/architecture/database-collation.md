---
title: "Database Collation"
topic: "collation"
description: "This article describes how to set or change the database collation by using Management Studio (SSMS) or Transact-SQL. If no databa"
tags: ["collation","database-collation"]
pubDate: "2025-12-01"
---

This article describes how to set or change the database

collation

by using

Management Studio (SSMS)

or Transact-SQL.

If no database collation is specified, the

server collation

is used.

You can find the supported collation names in

Windows Collation Name

and

Collation Name

; or you can use the

sys.fn_helpcollations

system function.

When you change the database collation, you change:

Any

,

,

,

,

, or

columns in system tables are changed

to the new collation.

All existing

,

,

,

,

, or

parameters and scalar return

values for stored procedures and user-defined functions are changed to the new

collation.

The

,

,

,

,

, or

system data types, and all user-defined

data types based on these system data types, are changed to the new default collation.

You can change the collation of any new objects that are created in a user database by using

the

clause of the

ALTER DATABASE

statement. This statement

the

collation of the columns in any existing user-defined tables. These can be changed by using

the

clause of

ALTER TABLE.

To create a new database, you need the

permission in the

database,

or the

, or

permission.

To change the collation of an existing database, you need the

permission on the

database.

```sql
COLLATE
COLLATE
CREATE DATABASE master
CREATE ANY DATABASE
ALTER ANY DATABASE
ALTER
```
