---
title: "From SAP ASE"
topic: "migration"
description: |
  Article

  •

  09/16/2024

  Applies to:

  SQL Server

  In this guide, you learn how to migrate your SAP ASE databases to SQL Server by using SQL

  Server Migration Assistant for SAP ASE (SSMA for SAP ASE).

tags:
  - "migration"
  - "from-sap-ase"
pubDate: 2025-12-01
---

Article

•

09/16/2024

Applies to:

SQL Server

In this guide, you learn how to migrate your SAP ASE databases to SQL Server by using SQL

Server Migration Assistant for SAP ASE (SSMA for SAP ASE).

For other migration guides, see

Azure Database Migration Guides

.

Before you begin migrating your SAP ASE database to SQL Server:

Verify that your source environment is supported.

Get

SQL Server Migration Assistant for SAP Adaptive Server Enterprise (formerly SAP

Sybase ASE)

.

Get connectivity and sufficient permissions to access both the source and target.

After you meet the prerequisites, you're ready to discover the topology of your environment

and assess the feasibility of your migration.

By using SSMA for SAP ASE, you can review database objects and data, assess databases for

migration, migrate Sybase database objects to SQL Server, and then migrate data to SQL

Server. To learn more, see

SQL Server Migration Assistant for Sybase (SybaseToSQL)

.

To create an assessment:

1. Open

SSMA for SAP ASE

.

2. On the

menu, select

.

3. Enter a project name and a location to save your project. Then select

SQL Server

as the

migration target from the dropdown list, and select

.

4. In the

dialog box, enter values for SAP connection details.

5. Right-click the SAP database you want to migrate, and then select

to

generate an HTML report.
