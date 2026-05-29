---
title: "Display data & log space information for a database"
topic: "collation"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  Azure Synapse Analytics
  
  Analytics Platform System (PDW)
  
  SQL database in Microsoft
  
  Fabric
  
  This article describes how to disp
tags:
  - "collation"
  - "display-data-log-space-information-for-a-database"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

This article describes how to display the data and log space information for a database in SQL

Server by using SQL Server Management Studio or Transact-SQL.

Permission to run

is granted to the

role. Only members of the

fixed database role can specify the

parameter.

1. In Object Explorer, connect to an instance of SQL Server and then expand that instance.

2. Expand

.

3. Right-click a database, point to

, point to

, and then select

.

1. Connect to the Database Engine.

2. On the Standard toolbar, select

.

3. Paste the following example into the query window and then select

. This example

uses the

sp_spaceused

system stored procedure to report disk space information for the

entire database, including tables and indexes.

SQL