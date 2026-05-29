---
title: "Configure replication"
topic: "linux-operations"
description: |
  Applies to:
  
  SQL Server
  
  on Linux
  
  In this tutorial, configure SQL Server snapshot replication on Linux with two instances of SQL
  
  Server using Transact-SQL (T-SQL). The publisher and distributor are 
tags:
  - "linux-operations"
  - "configure-replication"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

In this tutorial, configure SQL Server snapshot replication on Linux with two instances of SQL

Server using Transact-SQL (T-SQL). The publisher and distributor are on the same instance, and

the subscriber is on a separate instance.

All replication configurations can be configured with

replication stored procedures

.

To complete this tutorial, you need:

Two instances of SQL Server with the latest version of SQL Server on Linux

A tool to issue T-SQL queries to set up replication, such as

sqlcmd

or

SQL Server

Management Studio (SSMS)

See

Use SQL Server Management Studio on Windows to manage SQL Server on Linux

.

1. Enable SQL Server replication agents on Linux. On both host machines, run the following

commands in the terminal.

Bash

Enable SQL Server replication agents on Linux

＂

Create a sample database

＂

Configure snapshot folder for SQL Server agents access

＂

Configure the distributor

＂

Configure the publisher

＂

Configure publication and articles

＂

Configure subscriber

＂

Run the replication jobs

＂

７

Note

SQL Server Replication is supported on Linux in SQL Server 2017 (14.x) (

) and

later versions.