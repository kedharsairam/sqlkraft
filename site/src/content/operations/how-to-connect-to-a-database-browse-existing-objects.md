---
title: "How to: Connect to a Database & Browse Existing Objects"
topic: "ssb-diagnose"
description: |
  09/10/2025

  A common task for database administrators and developers is to connect to a live database,

  design, or browse its schema and query against its objects. The SQL Server Object Explorer in

  V
tags:
  - "ssb-diagnose"
  - "how-to-connect-to-a-database-browse-existing-objects"
pubDate: 2025-12-01
---

09/10/2025

A common task for database administrators and developers is to connect to a live database,

design, or browse its schema and query against its objects. The SQL Server Object Explorer in

Visual Studio now contains a dedicated

SQL Server

node, under which all connected SQL

Server instances and their databases are grouped in an SSMS-like hierarchy. The connected

SQL Server instances can be an on-premises one, such as SQL Server 2022 (16.x), or off-

premises in Azure SQL.

The following procedure assumes that you already have the AdventureWorks sample database

installed. Use

GitHub

to locate and install sample databases for different SQL Server versions.

If you prefer, you can also follow the steps and use an existing database on your server.

1. In Visual Studio, make sure that

SQL Server Object Explorer

is open. If it's not, select the

menu and select

SQL Server Object Explorer

.

2. Right-click the

SQL Server

node in

SQL Server Object Explorer

and select

.

3. In the

dialog box, enter the

of the server instance you

want to connect to, your credentials, and select

.

4. In

SQL Server Object Explorer

, expand the

node under your server instance.

You see all the databases residing in this server instance added under this

node.

5. Expand the

(or another database) node. You notice that all the database

entities are organized in a hierarchy similar to SQL Server Management Studio.
