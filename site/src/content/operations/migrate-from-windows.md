---
title: "Migrate from Windows"
topic: "linux-operations"
description: "on Linux SQL Server's backup and restore feature is the recommended way to migrate a database from SQL Server on Windows to SQL Server on Linux. In this tutorial, you walk t"
tags: ["linux-operations","migrate-from-windows"]
pubDate: 2025-12-01
---

on Linux

's backup and restore feature is the recommended way to migrate a database from

on Windows to SQL Server on Linux. In this tutorial, you walk through the steps

required to move a database to Linux with backup and restore techniques.

You can also create a SQL Server Always On Availability Group to migrate a SQL Server database

from Windows to Linux. See

sql-server-linux-availability-group-cross-platform.

The following prerequisites are required to complete this tutorial:

On a Windows machine:

installed.

Management Studio

installed.

Target database to migrate.

On a Linux machine:

(

Red Hat Enterprise Linux

,

SUSE Linux Enterprise Server

, or

Ubuntu

) with

command-line tools.

Create a backup file on Windows with SSMS

＂

Install a Bash shell on Windows

＂

Move the backup file to Linux from the Bash shell

＂

Restore the backup file on Linux with Transact-SQL

＂

Run a query to verify the migration

＂

７

Note

Starting in SQL Server 2025 (17.x), SUSE Linux Enterprise Server (SLES) isn't supported.
