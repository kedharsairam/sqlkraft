---
name: "Multipart names"
title: "Multipart names"
category: "statements"
description: "Azure SQL Managed Instance"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

SQL)

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in Microsoft Fabric

The following table lists and describes conventions that are used in the syntax diagrams in the

Transact-SQL reference.

UPPERCASE or

Transact-SQL keywords.

italic

User-supplied parameters of Transact-SQL syntax.

Type database names, table names, column names, index names, stored procedures,

utilities, data type names, and text exactly as shown.

(vertical bar)

Separates syntax items enclosed in brackets or braces. You can use only one of the

items.

(brackets)

Optional syntax item.

(braces)

Required syntax items. Don't type the braces.

Indicates the preceding item can be repeated

n

number of times. The occurrences are

separated by commas.

Indicates the preceding item can be repeated

n

number of times. The occurrences are

separated by blanks.

Transact-SQL statement terminator. Although the semicolon isn't required for most

statements in this version of SQL Server, it will be required in a future version.

The name for a block of syntax. Use this convention to group and label sections of

lengthy syntax or a unit of syntax that you can use in more than one location within a

statement. Each location in which the block of syntax could be used, is indicated with

the label enclosed in chevrons: <label>.

A set is a collection of expressions, for example <grouping set>; and a list is a

collection of sets, for example <composite element list>.



Expand table

Unless specified otherwise, all Transact-SQL references to the name of a database object can be

a four-part name in the following form:

|

|

|

server_name

Specifies a linked server name or remote server name.

database_name

Specifies the name of a SQL Server database when the object resides in a local instance of

SQL Server. When the object is in a linked server,

database_name

specifies an OLE DB

catalog.

schema_name

Specifies the name of the schema that contains the object if the object is in a SQL Server

database. When the object is in a linked server,

schema_name

specifies an OLE DB schema

name.

object_name

Refers to the name of the object.

When referencing a specific object, you don't always have to specify the server, database, and

schema for the SQL Server Database Engine to identify the object. However, if the object can't

be found, an error is returned.

To avoid name resolution errors, we recommend specifying the schema name whenever you

specify a schema-scoped object.

To omit intermediate nodes, use periods to indicate these positions. The following table shows

the valid formats of object names.

Displayed in code

Displayed in code

#### Object reference format

### int

### varchar(255)

### bit

```sql
UPPERCASE
```

```sql
|
```

```sql
[ ]
```

```sql
{ }
```

```sql
[ , ...n ]
```

```sql
[ ...n ]
```

```sql
;
```

```sql
<label> ::=
```

```sql
<server_name>.[<database_name>].[<schema_name>].<object_name>
```

```sql
<database_name>.[<schema_name>].<object_name>
```

```sql
<schema_name>.<object_name>
```

```sql
<object_name>
```
