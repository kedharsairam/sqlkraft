---
title: "Install & configure"
topic: "monitor"
description: |
  Article

  •

  08/01/2023

  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  Azure Synapse Analytics

  Analytics Platform System (PDW)

  This article contains installation and config
tags:
  - "monitor"
  - "install-configure-2"
pubDate: 2025-12-01
---

Article

•

08/01/2023

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

This article contains installation and configuration instructions for the

database.

2016

with Service Pack 1 (and later versions), or Azure SQL Database. To use

the full version of the sample, use SQL Server Developer or Enterprise editions.

Management Studio

(SSMS).

Download the sample

database backup/BACPAC that corresponds to

your edition of SQL Server or Azure SQL Database.

The latest release of the sample is available from

wide-world-importers-release.

Source code to recreate the sample database is available from

wide-world-importers-source.

Data population is based on ETL from the OLTP database (

).

You can use SSMS to restore a backup to SQL Server, or import a BACPAC into a new Azure

SQL database.

Restore a backup to a SQL Server instance using SSMS:

1. Open SSMS and connect to the target SQL Server instance.

2. Right-click on the

node, and select.

3. Select

and select the ellipses button (

).

4. In the dialog

, select

, navigate to the database backup in

the filesystem of the server, and select the backup. Select.

SQL Server

```cmd
WideWorldImportersDW
WideWorldImportersDW
WideWorldImporters
```
