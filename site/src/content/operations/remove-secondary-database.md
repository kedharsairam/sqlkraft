---
title: "Remove secondary database"
topic: "high-availability"
description: |
  Article
  
  •
  
  09/04/2024
  
  Applies to:
  
  SQL Server
  
  This topic describes how to remove a secondary database from an Always On availability group
  
  by using SQL Server Management Studio, Transact-SQL, or P
tags:
  - "high-availability"
  - "remove-secondary-database"
pubDate: 2025-12-01
---

Article

•

09/04/2024

Applies to:

SQL Server

This topic describes how to remove a secondary database from an Always On availability group

by using SQL Server Management Studio, Transact-SQL, or PowerShell in SQL Server.

This task is supported only on secondary replicas. You must be connected to the server

instance that hosts the secondary replica from which the database is to be removed.

Requires ALTER permission on the database.

1. In Object Explorer, connect to the server instance that hosts the secondary replica from

which you want to remove one or more secondary databases, and expand the server tree.

2. Expand the

node and the

node.

3. Select the availability group, and expand the

node.

4. This step depends on whether you want to remove multiple databases groups or only

one database, as follows:

To remove multiple databases, use the

pane to view and

select all the databases that you want to remove. For more information, see

Use the

Object Explorer Details to Monitor Availability Groups (SQL Server Management

Studio)

.

To remove a single database, select it in either the

pane or the

pane.

5. Right-click the selected database or databases, and select

in the command menu.

Prerequisites and Restrictions