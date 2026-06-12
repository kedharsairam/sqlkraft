---
title: "Manage SQL services"
topic: "linux-operations"
description: "07/03/2025 - Linux This article describes how to start, stop, or restart the SQL Server Database Engine and SQL Server Agent on Linux by using the command line, or Transact"
tags: ["linux-operations","manage-sql-services"]
pubDate: 2025-12-01
---

- Linux

This article describes how to start, stop, or restart the SQL Server Database Engine and SQL

Server Agent on Linux by using the command line, or Transact-SQL.

For SQL Server on Windows, see

Start, stop, pause, resume, and restart SQL Server services.

For SQL Server on Linux containers, see

Configure and customize SQL Server Linux containers.

components are executable programs that run as services (also known as

daemons

on Linux). Linux services can run without displaying any activity on the computer screen and

without user interaction on the command line.

The Database Engine service is the default instance, with a limit of one per computer. Named

instances aren't supported on Linux. To run multiple instances of SQL Server on a single

computer using containers, see

Deploy and connect to SQL Server Linux containers.

The SQL Server Agent service executes scheduled administrative tasks, which are called jobs

and alerts. For more information, see

Agent. SQL Server Agent isn't available in

every edition of SQL Server. For a list of features supported by the editions of SQL Server, see

Editions and supported features of SQL Server 2022.

On Linux, you can't pause the Database Engine service like you can on Windows. The SQL

Server Agent service also can't be paused or resumed.

When running on a cluster, use the appropriate cluster management tool to manage the

Database Engine for your Linux distribution. See

Deploy a Pacemaker cluster for SQL Server on

Linux

for an example using Pacemaker.

Database Engine service

Agent service
