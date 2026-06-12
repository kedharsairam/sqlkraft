---
title: "Create a SQL Server Agent job"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  SQL Server jobs are used to regularly perform the same sequence of commands in your SQL

  Server database. This tutorial provides an example of how to create a SQL Se
tags:
  - "linux-operations"
  - "create-a-sql-server-agent-job"
pubDate: 2025-12-01
---

SQL Server

on Linux

jobs are used to regularly perform the same sequence of commands in your SQL

Server database. This tutorial provides an example of how to create a SQL Server Agent job on

Linux using both Transact-SQL and SQL Server Management Studio (SSMS).

For known issues with SQL Server Agent on Linux, see

on Linux: Known issues.

The following prerequisites are required to complete this tutorial:

Linux machine with the following prerequisites:

Quickstart: Install SQL Server and create a database on Red Hat Enterprise Linux

Quickstart: Install SQL Server and create a database on SUSE Linux Enterprise Server

Quickstart: Install SQL Server and create a database on Ubuntu

with command-line tools.

The following prerequisites are optional:

Windows machine with SSMS:

Install SQL Server Management Studio

for optional SSMS steps.

To use SQL Server Agent on Linux, you must first enable SQL Server Agent on a machine that

already has SQL Server installed.

Install SQL Server Agent on Linux

＂

Create a new job to perform daily database backups

＂

Schedule and run the job

＂

Perform the same steps in SSMS (optional)

＂

７

Note

Starting in SQL Server 2025 (17.x), SUSE Linux Enterprise Server (SLES) isn't supported.
