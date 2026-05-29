---
title: "Data tier applications"
topic: "ssms"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  A data-tier application (DAC) is a logical database entity that defines all of the SQL Server
tags:
  - "ssms"
  - "data-tier-applications"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

A data-tier application (DAC) is a logical database entity that defines all of the SQL Server

objects - such as tables, views, and instance objects, including logins - associated with a user's

database. A data-tier application is a self-contained unit of the entire database model and is

portable in both

and

packages.

Tooling support

for data-tier applications

enables developers and database administrators to apply

and

files to new or

existing databases or generate new files from existing databases.

The

file format is a related artifact that by default encapsulates the database schema

and the data stored in the database. Objects in the

database model are limited to the

surface area of Azure SQL Database. The primary use case for a

is to move a database

from one server to another - or to

migrate a database from a local server to the cloud

- and

archiving an existing database in an open format.

- the user can export a database to a

file. For more information, see

SqlPackage export

and

Export a BACPAC file

.

- the user can import a

file into a new database. For more information,

see

SqlPackage import

and

Import a BACPAC file to create a new database

.

Learn more about database portability from the

SqlPackage portability documentation

.

The

data-tier application package is the build artifact from

SQL database projects

You

can use it as part of a comprehensive database lifecycle management and DevOps strategy.

Data isn't included in a

by default, but you can choose to include data from user

tables when you extract a

from a live SQL Server or Azure SQL Database. As an

integral part of the SQL database project workflow and database development lifecycle,

files are used in several operations. The primary operations are:

- extract a database into a

. For more information, see

SqlPackage extract

and

Extract a DACPAC from a database

.

```cmd
.dacpac
.bacpac
.dacpac
.bacpac
.bacpac
```
