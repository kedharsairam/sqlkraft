---
title: "Configure with mssql-conf"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  is a configuration script that installs with SQL Server for Red Hat Enterprise Linux,

  SUSE Linux Enterprise Server, and Ubuntu. It modifies the

  mssql.conf file

  wh
tags:
  - "linux-operations"
  - "configure-with-mssql-conf"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

is a configuration script that installs with SQL Server for Red Hat Enterprise Linux,

SUSE Linux Enterprise Server, and Ubuntu. It modifies the

mssql.conf file

where configuration

values are stored.

is a configuration script that installs with SQL Server on Linux. You can use this utility

to set the following parameters:

Description

Agent

Enable SQL Server Agent

Authenticate with Microsoft

Entra ID

Settings for authenticating with Microsoft Entra ID (

formerly Azure Active

Directory

).

Authenticate with Windows

Settings for Windows Server Active Directory authentication.

Collation

Set a new collation for SQL Server on Linux.

Custom password policy

Password policies enforce complexity, expiration, and password changes.

Customer feedback

Choose whether or not SQL Server sends feedback to Microsoft.

Database Mail Profile

Set the default database mail profile for SQL Server on Linux.

Default data directory

Change the default directory for new SQL Server database data files (

).

Default log directory

Changes the default directory for new SQL Server database log files (

).

Default master database file

directory

Changes the default directory for the

database files on existing SQL

installation.

Default master database file

Changes the name of

database files.

７

Note

Starting in SQL Server 2025 (17.x), SUSE Linux Enterprise Server (SLES) isn't supported.

ﾉ

Expand table

```cmd
.mdf
.ldf
master
master
```
