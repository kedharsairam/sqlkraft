---
title: "Extract a dacpac"
topic: "ssms"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The extraction process creates a DAC package file (

  ) that contains definitions of the

  data
tags:
  - "ssms"
  - "extract-a-dacpac"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The extraction process creates a DAC package file (

) that contains definitions of the

database objects and their related instance-level elements. For example, a

file contains

the database tables, stored procedures, views, and users, along with the logins that map to the

database users. The

file can be used to deploy the database to another instance of

SQL Server or Azure SQL Database or to register the database as a data-tier application (DAC)

in the current instance.

Options for extracting a

include:

1. the

wizard in SQL Server Management Studio (SSMS)

2. SQL Server Data Tools

3. SqlPackage command-line utility

4. MSSQL extension for Visual Studio Code

Extracting a

requires at least

and database scope

permissions, and

permissions on

. Members of the

fixed server role who are also members of the database_owner fixed database

role are eligible to extract a

. Members of the

fixed server role or the built-in

SQL Server system administrator account named

can also extract a

.

1. In

, expand the node for the instance containing the database from

which the

is to be extracted.

2. Expand the

node.

3. Right-click the node for the database from which the

is to be extracted,

point to

, and then select

4. Complete the wizard dialogs:

a.

Introduction Page

SQL Server Management Studio

```cmd
.dacpac
.dacpac
.dacpac
.dacpac
.dacpac
```
