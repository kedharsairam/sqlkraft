---
title: "Required Permissions for SQL Server Data Tools"
topic: "data-tools"
description: |
  Required permissions for SQL Server Data
  
  09/09/2025
  
  Before you can perform an action on a database in Visual Studio, you must sign in with an
  
  account that has certain permissions on that database. 
tags:
  - "data-tools"
  - "required-permissions-for-sql-server-data-tools"
pubDate: 2025-12-01
---

Required permissions for SQL Server Data

09/09/2025

Before you can perform an action on a database in Visual Studio, you must sign in with an

account that has certain permissions on that database. The specific permissions that you need

vary based on what action you want to perform. The following sections describe each action

that you might want to perform and the permissions that you need to perform it.

You must have the following permissions to create or deploy a database.

Required permissions

Import database objects

and settings

You must be able to connect to the source database.

If the source database is based on SQL Server 2005, you must also own or

have the

permission on each object.

If the source database is based on SQL Server 2008 or later, you must also

own or have the

permission on each object. Your login must

have the

permission (for database encryption keys).

Import server objects and

settings

You must be able to connect to the primary database on the specified server.

If the server is running SQL Server 2005, you must have the

permission on the server.

If the source database is based on SQL Server 2008 or later, you must have

the

permission on the server. Your login must have the

permission (for database encryption keys).

Create or update a

database project

You don't need any database permissions to create or modify a database

project.

Deploy a new database

or deploy with the

option set

You must either have the

permission or be a member of the

role on the target server.

When you create a database, Visual Studio connects to the

database

and copies its contents. The initial login (for example,

yourLogin

) that you use

to connect to the target database must have

and

permissions. This login must have a user mapping on the

database. If

ﾉ

Expand table

```cmd
VIEW DEFINITION
VIEW DEFINITION
VIEW SERVER STATE
VIEW ANY
DEFINITION
VIEW ANY DEFINITION
```