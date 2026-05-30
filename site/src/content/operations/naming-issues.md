---
title: "Naming issues"
topic: "ssms"
description: |
  Article

  •

  11/22/2024

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  When you analyze the T-SQL code in your database project, one or more
tags:
  - "ssms"
  - "naming-issues"
pubDate: 2025-12-01
---

Article

•

11/22/2024

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

When you analyze the T-SQL code in your database project, one or more warnings might be

categorized as naming issues. You should address naming issues to avoid the following

situations:

The name that you specified for an object might conflict with the name of a system

object.

The name that you specified always needs to be enclosed in escape characters (in SQL

Server, '[' and ']').

The name that you specified might confuse others who try to read and understand your

code.

The code might break if you run it with future releases of SQL Server.

In general, you might suppress a naming issue if other applications that you can't change

depend on the current name.

The provided rules identify the following naming issues:

SR0011: Avoid using special characters in object names

SR0012: Avoid using reserved words for type names

SR0016: Avoid using sp\_ as a prefix for stored procedures

If you name a database object by using any character in the following table, you make it more

difficult not only to reference that object but also to read code that contains the name of that

object:

Description

Whitespace character

Left square bracket

Right square bracket

ﾉ

Expand table

```cmd
[
]
```
