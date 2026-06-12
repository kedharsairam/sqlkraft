---
title: "Bulk copy with bcp"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  This article shows how to use the

  bcp utility

  to bulk copy data between an instance of SQL Server

  on Linux and a data file in a user-specified format.

  You can us
tags:
  - "linux-operations"
  - "bulk-copy-with-bcp"
pubDate: 2025-12-01
---

SQL Server

on Linux

This article shows how to use the

bcp utility

to bulk copy data between an instance of SQL Server

on Linux and a data file in a user-specified format.

You can use

to import large numbers of rows into SQL Server tables or to export data from

tables into data files. Except when used with the queryout option,

requires no

knowledge of Transact-SQL. The

command-line utility works with Microsoft SQL Server

running on-premises or in the cloud, on Linux, Windows or Docker and Azure SQL Database and

Azure Synapse Analytics.

This article shows you how to:

Import data into a table using the

command

Export data from a table using the

command

is part of the SQL Server command-line tools, which aren't installed automatically with SQL

Server on Linux. If you haven't already installed the SQL Server command-line tools on your Linux

machine, you must install them. For more information on how to install the tools, select your

Linux distribution from the following list:

Red Hat Enterprise Linux (RHEL)

Ubuntu

SUSE Linux Enterprise Server (SLES)

In this tutorial, you create a sample database and table on the local SQL Server instance

(

) and then use

to load into the sample table from a text file on disk.

Start by creating a sample database with a simple table that is used in the rest of this tutorial.

```cmd
bcp in bcp out localhost
```
