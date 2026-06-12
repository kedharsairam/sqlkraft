---
title: "Defining UDT tables & columns"
topic: "clr-integration"
description: "Once the assembly containing the user-defined type (UDT) definition is registered in a SQL Server database, it can be used in a column definition. For"
tags: ["clr-integration","defining-udt-tables-columns"]
pubDate: "2025-12-01"
---

Once the assembly containing the user-defined type (UDT) definition is registered in a SQL

Server database, it can be used in a column definition. For more information, see

CREATE TYPE.

There's no special syntax for creating a UDT column in a table. You can use the name of the

UDT in a column definition as though it were one of the intrinsic SQL Server data types. The

following

Transact-SQL statement creates a table named

, with a column

named

, which is defined as an

identity column and the primary key for the table. The

second column is named

, with a data type of. The schema name used in this

example is. You must have the necessary permissions to specify a schema name. If you

omit the schema name, the default schema for the database user is used.

There are two options for indexing a UDT column:

In this case, if the UDT is binary-ordered, you can create an index

over the entire UDT column by using the

Transact-SQL statement.

You can create indexes on persisted computed columns over UDT

expressions. The UDT expression can be a field, method, or property of a UDT. The

expression must be deterministic and must not perform data access.

For more information, see

CREATE INDEX.

```sql
CREATE TABLE
Points
ID
PointValue
Point dbo
CREATE INDEX
CREATE
TABLE dbo.Points (
ID
INT
IDENTITY (1, 1) PRIMARY
KEY
,
PointValue Point
);
```
