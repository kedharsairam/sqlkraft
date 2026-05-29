---
title: "SUSE Linux Enterprise Server (SLES)"
topic: "linux-operations"
description: |
  Applies to:
  
  SQL Server
  
  on Linux
  
  This sample bash script installs SQL Server 2022 (16.x) on SUSE Linux Enterprise Server (SLES)
  
  without interactive input. It provides examples of installing the Dat
tags:
  - "linux-operations"
  - "suse-linux-enterprise-server-sles"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

This sample bash script installs SQL Server 2022 (16.x) on SUSE Linux Enterprise Server (SLES)

without interactive input. It provides examples of installing the Database Engine, the SQL

Server command-line tools, SQL Server Agent, and performs post-install steps. You can

optionally install full-text search and create an administrative user.

If you don't need an unattended installation script, the fastest way to install SQL Server is to

follow the

quickstart for SLES

. For other setup information, see

Installation guidance for SQL

Server on Linux

.

You need at least 2 GB of memory to run SQL Server on Linux.

The file system must be

or

. Other file systems, such as

, aren't supported.

For other system requirements, see

System requirements for SQL Server on Linux

.

This example installs SQL Server 2019 (15.x) on SLES v15 SP6. If you want to install a different

version of SQL Server or SLES, change the Microsoft repository paths accordingly.

Save the sample script to a file and then customize it. Replace the variable values in the script.

You can also set any of the scripting variables as environment variables, as long as you remove

them from the script file.

７

Note

Starting in SQL Server 2025 (17.x), SUSE Linux Enterprise Server (SLES) isn't supported.

）

Important

SQL Server requires

, which the default SLES repositories don't provide.

You can install this package from the SLES SDK.

）

Important

```cmd
libsss_nss_idmap0
```