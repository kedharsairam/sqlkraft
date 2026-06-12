---
title: "Identifiers"
topic: "collation"
description: "SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft F"
tags: ["collation","identifiers"]
pubDate: 2025-12-01
---

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

The database object name is its identifier.

Servers, databases, and database objects, such as tables, views, columns, indexes, triggers,

procedures, constraints, and rules, can have identifiers. Most objects require identifiers, but

some objects, such as constraints, make them optional.

You create an object identifier when you define the object. Use the identifier to reference the

object. For example, the following statement creates a table with the identifier

, and two

columns with the identifiers

and

:

This table has an unnamed constraint. The primary key constraint has no user-specified

identifier, so the system assigns it a generated name like. You

can see this name in system metadata views like

sys.key_constraints.

Constraint names and other schema-scoped objects must be unique within a database schema.

For example, two primary key constraints can't share a name. However, column names only

need to be unique within each table, not within the schema.

The collation of an identifier depends on the level at which you define it.

The default collation of the instance is assigned to identifiers of instance-level objects,

such as logins and database names.

The default collation of the database is assigned to identifiers of objects in a database,

such as tables, views, and column names. For example, you can create two tables with

names that differ only in case in a database that has case-sensitive collation, but you can't

create them in a database that has case-insensitive collation.

```sql
TableX
KeyCol
Description
PK__TableX__D7CB9CCCEEF0806C
CREATE
TABLE
TableX (
KeyCol
INT
PRIMARY
KEY
,
Description
NVARCHAR (80)
);
```
