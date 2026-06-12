---
title: "Register"
topic: "clr-integration"
description: "In order to use a user-defined type (UDT) in SQL Server, you must register it."
tags: ["clr-integration","register"]
pubDate: "2025-12-01"
---

In order to use a user-defined type (UDT) in SQL Server, you must register it. Registering a UDT

involves registering the assembly and creating the type in the database in which you wish to

use it. UDTs are scoped to a single database, and can't be used in multiple databases unless the

identical assembly and UDT are registered with each database. Once the UDT assembly is

registered and the type created, you can use the UDT in Transact-SQL and in client code. For

more information, see

CLR user-defined types.

The easiest way to deploy your UDT is by using Visual Studio. For more complex deployment

scenarios and the greatest flexibility, however, use Transact-SQL as discussed later in this

article.

Follow these steps to create and deploy a UDT using Visual Studio:

1. Create a new

project in the

or

language nodes.

2. Add a reference to the SQL Server database that will contain the UDT.

3. Add a

class.

4. Write code to implement the UDT.

5. From the

menu, select. This registers the assembly and creates the type in

the SQL Server database.

The Transact-SQL

syntax is used to register the assembly in the database in

which you wish to use the UDT. It's stored internally in database system tables, not externally in

the file system. If the UDT is dependent on external assemblies, they too must be loaded into

the database. The

statement is used to create the UDT in the database in which

it's to be used. For more information, see

CREATE ASSEMBLY

and

CREATE TYPE.

```sql
CREATE ASSEMBLY
CREATE TYPE
```
