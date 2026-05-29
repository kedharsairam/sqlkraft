---
title: "Register a database as a DAC"
topic: "ssms"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  The registration process creates a data-tier application (DAC) definition that defines the ob
tags:
  - "ssms"
  - "register-a-database-as-a-dac"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The registration process creates a data-tier application (DAC) definition that defines the objects

in the database. Register a database as a data-tier application (DAC) to build a data-tier

application (DAC) definition that describes the objects in an existing database and write that

DAC definition in the

system database (

in Azure SQL Database).

To register a database as a DAC, use:

The Register Data-tier Application Wizard in SQL Server Management Studio

SQL Server Data Tools

The SqlPackage command-line utility

Registering a DAC in an instance of Database Engine requires at least ALTER ANY sign in and

database scope VIEW DEFINITION permissions, SELECT permissions on

, and membership in the

fixed server role.

Members of the

fixed server role or the built-in SQL Server system administrator

account named

can also register a DAC. Registering a DAC that doesn't contain logins in

SQL Database requires membership in the

or

roles. Registering a DAC

that contains logins in SQL Database requires membership in the

or

roles.

1. In

, expand the node for the instance containing the database to be

registered as a DAC.

2. Expand the

node.

3. Right-click the database to be registered, point to

, and then select

4. Complete the wizard dialogs:

a.

Introduction Page

b. [Set Properties Page](#set-properties-page

c. [Validation and Summary Page](#validation-and-summary-page

d.

Register DAC Page

SQL Server Management Studio

```cmd
msdb
master
sys.sql_expression_dependencies
```
