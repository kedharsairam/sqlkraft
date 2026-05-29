---
title: "Install & configure"
topic: "monitor"
description: |
  Article
  
  •
  
  04/26/2024
  
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Wide World Importers OLTP database installation and configuration instructions.
  
  SQL Server 2016
  
  (or higher) or
  
  Azure SQL Databas
tags:
  - "monitor"
  - "install-configure"
pubDate: 2025-12-01
---

Article

•

04/26/2024

Applies to:

SQL Server

Azure SQL Database

Wide World Importers OLTP database installation and configuration instructions.

SQL Server 2016

(or higher) or

Azure SQL Database

. For the Full version of the

sample, use SQL Server Evaluation/Developer/Enterprise Edition.

SQL Server Management Studio

. For the best results use the June 2016 release or later.

The latest release of the sample:

wide-world-importers-release

Download the sample WideWorldImporters database backup/bacpac that corresponds to your

edition of SQL Server or Azure SQL Database.

Source code to recreate the sample database is available from the following location. Note that

recreating the sample will result in slight differences in the data, since there is a random factor

in the data generation:

wide-world-importers

To restore a backup to a SQL Server instance, you can use Management Studio.

1. Open SQL Server Management Studio and connect to the target SQL Server instance.

2. Right-click on the

node, and select

.

3. Select

and click on the button

4. In the dialog

, click

, navigate to the database backup in the

filesystem of the server, and select the backup. Click

.

5. If needed, change the target location for the data and log files, in the

pane. Note

that it is best practice to place data and log files on different drives.

SQL Server