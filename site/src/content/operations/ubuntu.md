---
title: "Ubuntu"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  This sample bash script installs SQL Server on Ubuntu without interactive input. It provides

  examples of installing the Database Engine, the SQL Server command-line
tags:
  - "linux-operations"
  - "ubuntu"
pubDate: 2025-12-01
---

SQL Server

on Linux

This sample bash script installs SQL Server on Ubuntu without interactive input. It provides

examples of installing the Database Engine, the SQL Server command-line tools, SQL Server

Agent, and performs post-install steps. You can optionally install full-text search and create an

administrative user.

You need at least 2 GB of memory to run SQL Server on Linux.

The file system must be

or. Other file systems, such as

, are unsupported.

For other system requirements, see

System requirements for SQL Server on Linux.

This example installs SQL Server 2019 (15.x) on Ubuntu Server 20.04. If you want to install a

different version of SQL Server or Ubuntu Server, change the Microsoft repository paths

accordingly.

Save the sample script to a file and then to customize it. You must replace the variable values in

the script. You can also set any of the scripting variables as environment variables, as long as

you remove them from the script file.

The script might fail if SQL Server is slow to start. That's because the script exits with a non-

zero status. Removing the

switch on the first line might resolve this issue.



Tip

If you don't need an unattended installation script, the fastest way to install SQL Server is

to follow the

quickstart for Ubuntu. For other setup information, see.

）

Important

The

environment variable is deprecated. Use

instead.

```cmd
-e
SA_PASSWORD
MSSQL_SA_PASSWORD
```
