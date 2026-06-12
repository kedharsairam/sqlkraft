---
title: "Configure"
topic: "high-availability"
description: |
  ﾃ

  Summarize this article for me

  Applies to:

  SQL Server

  This article describes how to configure log shipping in SQL Server by using SQL Server

  Management Studio or Transact-SQL.

  The primary datab
tags:
  - "high-availability"
  - "configure"
pubDate: 2025-12-01
---

ﾃ

Summarize this article for me

SQL Server

This article describes how to configure log shipping in SQL Server by using SQL Server

Management Studio or Transact-SQL.

The primary database must use the full or bulk-logged recovery model; switching the

database to simple recovery will cause log shipping to stop functioning.

Before you configure log shipping, you must create a share to make the transaction log

backups available to the secondary server. This is a share of the directory where the

transaction log backups will be generated. For example, if you back up your transaction

logs to the directory

, you could create the

share

of that directory.

The log shipping stored procedures require membership in the

fixed server role.

７

Note

2008 (10.0.x) Enterprise and later versions support backup compression. When

creating a log shipping configuration, you can control the backup compression behavior

of log backups. For more information, see.

）

Important

2025 (17.x) uses

as the default version for linked

servers, which has a default

value of. Changes to the linked

server configuration might be required when adding a SQL Server 2025 (17.x)

instance as a replica or monitor.

Log shipping monitoring can break if the monitor is a remote SQL Server 2025 (17.x)

instance when other SQL Server instances in the log shipping topology use a

previous version.

```cmd
C:\data\tlogs\
\\<primaryserver>\tlogs
Encrypt
Mandatory
```
