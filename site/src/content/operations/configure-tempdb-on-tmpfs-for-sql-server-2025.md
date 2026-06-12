---
title: "Configure tempdb on tmpfs for SQL Server 2025"
topic: "linux-operations"
description: "2025 (17.x) - Linux This article guides you to enable and run database files on the filesystem in SQL Server 2025 (17.x). SQL Server on Linux and containers traditionally"
tags: ["linux-operations","configure-tempdb-on-tmpfs-for-sql-server-2025"]
pubDate: "2025-12-01"
---

2025 (17.x) - Linux

This article guides you to enable and run

database files on the

filesystem in SQL

Server 2025 (17.x).

on Linux and containers traditionally support

and

filesystems for

deploying SQL Server database files and logs. However, for temporary databases like

,

which don't require data to be saved from one uptime period to another, using a

filesystem that utilizes memory (RAM) can enhance overall performance for

-based

workloads.

For more information about the

filesystem, see

tmpfs - The Linux Kernel

documentation.

Description

is ideal for storing non-persistent data that doesn't need to be saved across

restarts. Currently only the

database files are supported on

filesystem

for both container and non-container based deployments.

filesystem can be used for user databases in SQL container deployments, but

only for development purposes. However, this configuration isn't supported. You

can provide feedback for this scenario on

GitHub.

To enable

support for SQL Server on Linux on physical or virtual machines, you need to

mount the

filesystem correctly, which requires sudo access. Once the mount points are

set up, you can place the

files on these mounts and start SQL Server with

files

mounted on the

filesystem.

1. Create the

directory.

Use the

command to create a directory for the

database. Ensure that it's

owned by the

user and group to allow SQL Server access:

ﾉ

Expand table

```cmd
tempdb tempdb tempdb tempdb tempdb
```
