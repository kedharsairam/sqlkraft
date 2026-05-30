---
title: "Availability basics"
topic: "linux-operations"
description: |
  SQL Server availability basics for Linux

  Applies to:

  SQL Server

  on Linux

  Starting with SQL Server 2017 (14.x), SQL Server is supported on both Linux and Windows. Like

  Windows-based SQL Server dep
tags:
  - "linux-operations"
  - "availability-basics"
pubDate: 2025-12-01
---

SQL Server availability basics for Linux

Applies to:

SQL Server

on Linux

Starting with SQL Server 2017 (14.x), SQL Server is supported on both Linux and Windows. Like

Windows-based SQL Server deployments, SQL Server databases and instances need to be

highly available under Linux.

This article covers the technical aspects of planning and deploying highly available Linux-based

SQL Server instances and databases, and highlights key differences from Windows-based

installations. Because either SQL Server or Linux might be new to you, this article discusses

concepts that might already be familiar to you.

Besides backup and restore, the same three availability features are available on Linux as for

Windows-based deployments:

Availability groups for SQL Server on Linux

Failover Cluster Instances - SQL Server on Linux

Get started with log shipping on Linux

On Windows, FCIs always require an underlying Windows Server failover cluster (WSFC).

Depending on the deployment scenario, an AG usually requires an underlying WSFC, with the

exception being the new None variant in SQL Server 2017 (14.x). A WSFC doesn't exist in Linux.

Clustering implementation in Linux is discussed in

Pacemaker for availability groups and

failover cluster instances on Linux

.

While some Linux installations include an interface, most don't. You use the command line for

nearly everything at the operating system layer. The common term for this command line in

the Linux world is a

shell

, the most common being

.

In Linux, you need elevated privileges to run many commands, similar to needing administrator

privileges in Windows Server. You can run commands with elevated privileges in two ways:

1. Run the command as the proper user. To change to a different user, use the

command. If you run

without a username, you enter a shell as

if you know the

SQL Server availability options for Linux

```cmd
bash
su
su
root
```
