---
title: "Migrate to Docker"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  This tutorial demonstrates how to move and restore a SQL Server backup file into a SQL Server

  2025 (17.x) Linux container image running on Docker.

  A container runt
tags:
  - "linux-operations"
  - "migrate-to-docker"
pubDate: 2025-12-01
---

SQL Server

on Linux

This tutorial demonstrates how to move and restore a SQL Server backup file into a SQL Server

2025 (17.x) Linux container image running on Docker.

A container runtime installed, such as

Docker

or

Podman

Install the latest

sqlcmd

System requirements for SQL Server on Linux

This section provides deployment options for your environment.

doesn't currently support the

parameter when creating containers. If you use

the

instructions in this tutorial, you create a container with the Developer edition of SQL

Server. Use the command line interface (CLI) instructions to create a container using the license

of your choice. For more information, see

Deploy and connect to SQL Server Linux containers.

1. Open a bash terminal on Linux.

2. Pull the SQL Server 2025 (17.x) Linux container image from the Microsoft Container

Registry.

Pull and run the latest SQL Server Linux container image.

＂

Copy the Wide World Importers database file into the container.

＂

Restore the database in the container.

＂

Run Transact-SQL statements to view and modify the database.

＂

Backup the modified database.

＂

CLI

```cmd
sqlcmd
MSSQL_PID sqlcmd
```
