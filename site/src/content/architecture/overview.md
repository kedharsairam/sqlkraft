---
title: "Overview"
topic: "collation"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  A database in SQL Server is made up of a collection of tables that stores a specific set of
  
  
tags:
  - "collation"
  - "overview"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

A database in SQL Server is made up of a collection of tables that stores a specific set of

structured data. A table contains a collection of rows, also referred to as records or tuples, and

columns, also referred to as attributes. Each column in the table is designed to store a certain

type of information, for example, dates, names, dollar amounts, and numbers.

A computer can have one or more than one instance of SQL Server installed. Each instance of

SQL Server can contain one or many databases. Within a database, there are one or many

object ownership groups called schemas. Within each schema there are database objects such

as tables, views, and stored procedures. Some objects such as certificates and asymmetric keys

are contained within the database, but are not contained within a schema. For more

information about creating tables, see

Tables

.

SQL Server databases are stored in the file system in files. Files can be grouped into filegroups.

For more information about files and filegroups, see

Database Files and Filegroups

.

When people gain access to an instance of SQL Server they are identified as a login. When

people gain access to a database they are identified as a database user. A database user can be

based on a login. If contained databases are enabled, a database user can be created that is

not based on a login. For more information about users, see

CREATE USER (Transact-SQL)

.

A user that has access to a database can be given permission to access the objects in the

database. Though permissions can be granted to individual users, we recommend creating

database roles, adding the database users to the roles, and then grant access permission to the

roles. Granting permissions to roles instead of users makes it easier to keep permissions

consistent and understandable as the number of users grow and continually change. For more

information about roles permissions, see

CREATE ROLE (Transact-SQL)

and

Principals (Database

Engine)

.

Most people who work with databases use the SQL Server Management Studio tool. The

Management Studio tool has a graphical user interface for creating databases and the objects

in the databases. Management Studio also has a query editor for interacting with databases by

writing Transact-SQL statements. Management Studio can be installed from the SQL Server