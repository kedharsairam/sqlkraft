---
title: "Red Hat Enterprise Linux (RHEL)"
topic: "linux-operations"
description: |
  Applies to:
  
  SQL Server
  
  on Linux
  
  This sample bash script installs SQL Server on Red Hat Enterprise Linux (RHEL) without
  
  interactive input. It provides examples of installing the Database Engine, th
tags:
  - "linux-operations"
  - "red-hat-enterprise-linux-rhel"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

This sample bash script installs SQL Server on Red Hat Enterprise Linux (RHEL) without

interactive input. It provides examples of installing the Database Engine, the SQL Server

command-line tools, SQL Server Agent, and performs post-install steps. You can optionally

install full-text search and create an administrative user.

You need at least 2 GB of memory to run SQL Server on Linux.

The file system must be

or

. Other file systems, such as

, are unsupported.

For other system requirements, see

System requirements for SQL Server on Linux

.

This example installs SQL Server 2019 (15.x) on RHEL 8.x. If you want to install a different

version of SQL Server or RHEL, change the Microsoft repository paths accordingly.

Save the sample script to a file. To customize it, You must replace the variable values in the

script. You can also set any of the scripting variables as environment variables, as long as you

remove them from the script file.

Your password should follow the SQL Server default

password policy

. By default, the password

must be at least eight characters long and contain characters from three of the following four

sets: uppercase letters, lowercase letters, base-10 digits, and symbols. Passwords can be up to

128 characters long. Use passwords that are as long and complex as possible.



Tip

If you don't need an unattended installation script, the fastest way to install SQL Server is

to follow the

Quickstart: Install SQL Server and create a database on Red Hat Enterprise

. For other setup information, see

.

）

Important

The

environment variable is deprecated. Use

instead.

```cmd
SA_PASSWORD
MSSQL_SA_PASSWORD
```