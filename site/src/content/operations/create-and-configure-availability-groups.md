---
title: "Create and configure availability groups"
topic: "linux-operations"
description: "on Linux This tutorial shows how to create and configure an availability group (AG) for SQL Server on Linux. Unlike SQL Server 2016 (13.x) and earlier versions on Windows, y"
tags: ["linux-operations","create-and-configure-availability-groups"]
pubDate: "2025-12-01"
---

on Linux

This tutorial shows how to create and configure an availability group (AG) for SQL Server on

Linux. Unlike SQL Server 2016 (13.x) and earlier versions on Windows, you can enable an AG

with or without creating the underlying Pacemaker cluster first. Integration with the cluster, if

needed, happens later.

The tutorial includes the following tasks:

Deploy the Pacemaker high availability cluster as described in

Deploy a Pacemaker cluster for

on Linux.

Unlike on Windows, you can't use PowerShell or SQL Server Configuration Manager to enable

the availability groups (AG) feature. On Linux, you can enable the availability groups feature in

two ways: use the

utility, or edit the

file manually.

Enable availability groups.

＂

Create availability group endpoints and certificates.

＂

Use SQL Server Management Studio (SSMS) or Transact-SQL to create an availability

group.

＂

Create the SQL Server login and permissions for Pacemaker.

＂

Create availability group resources in a Pacemaker cluster (External type only).

＂

）

Important

You must enable the AG feature for configuration-only replicas, even on SQL Server

Express.

```cmd
mssql.conf
```
