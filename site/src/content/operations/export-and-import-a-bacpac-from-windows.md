---
title: "Export and import a BACPAC from Windows"
topic: "linux-operations"
description: |
  07/03/2025
  
  Applies to:
  
  SQL Server
  
  - Linux
  
  This article shows how to use
  
  SQL Server Management Studio
  
  (SSMS) and
  
  SqlPackage
  
  to
  
  export and import a database on SQL Server on Linux. SSMS and Sql
tags:
  - "linux-operations"
  - "export-and-import-a-bacpac-from-windows"
pubDate: 2025-12-01
---

07/03/2025

Applies to:

SQL Server

- Linux

This article shows how to use

SQL Server Management Studio

(SSMS) and

SqlPackage

to

export and import a database on SQL Server on Linux. SSMS and SqlPackage.exe are Windows

applications, so use this technique when you have a Windows machine that can connect to a

remote SQL Server instance on Linux.

You should always install and use the most recent version of SSMS as described in

Use SQL

Server Management Studio on Windows to manage SQL Server on Linux

.

For information about migrating a database from one SQL Server instance to another, see

Migrate a SQL Server database from Windows to Linux using backup and restore

.

1. Start SSMS by typing

in the Windows search

box, and then select the desktop app.

2. Connect to your source database in Object Explorer. The source database can be in

Microsoft SQL Server running on-premises or in the cloud, on Linux, Windows, or Docker

and Azure SQL Database or Azure Synapse Analytics.

3. Right-click the source database in the Object Explorer, point to

, and select

4. In the export wizard, select

, and then on the

tab, configure the export to

save the BACPAC file to either a local disk location or to an Azure blob.

5. By default, all objects in the database are exported. Select the

and choose

the database objects that you wish to export.

6. Select

and then select

.

The

file is successfully created at the location you chose, and you're ready to import it

into a target database.

```cmd
.bacpac
```