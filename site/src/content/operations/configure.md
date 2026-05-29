---
title: "Configure"
topic: "linux-operations"
description: |
  07/03/2025
  
  Applies to:
  
  SQL Server
  
  - Linux
  
  SQL Server 2019 (15.x) introduces SQL Server Replication for instances of SQL Server on Linux.
  
  For detailed information about replication, see
  
  SQL Serve
tags:
  - "linux-operations"
  - "configure"
pubDate: 2025-12-01
---

07/03/2025

Applies to:

SQL Server

- Linux

SQL Server 2019 (15.x) introduces SQL Server Replication for instances of SQL Server on Linux.

For detailed information about replication, see

SQL Server Replication

.

Configure replication on Linux with either SQL Server Management Studio (SSMS) or Transact-

SQL stored procedures.

To use SSMS, follow the instructions in this article.

Use SSMS on a Windows operating system to connect to instances of SQL Server. For

background and instructions, see

Use SQL Server Management Studio on Windows to

manage SQL Server on Linux

.

For an example with stored procedures, follow the

Configure Replication with T-SQL

tutorial.

Before configuring publishers, distributors, and subscribers, you need to complete a couple

configuration steps for the SQL Server instance.

1. Enable SQL Server Agent to use replication agents. On all Linux servers, run the following

commands in the terminal.

Bash

2. Configure the SQL Server instance for replication. To configure the SQL Server instance for

replication, run

on all instances participating in

replication.

SQL

```cmd
sys.sp_MSrepl_createdatatypemappings
sudo /opt/mssql/bin/mssql-conf
set
sqlagent.enabled
true
sudo systemctl restart mssql-server
USE
msdb;
GO
```