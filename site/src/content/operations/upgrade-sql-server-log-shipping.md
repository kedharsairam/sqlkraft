---
title: "Upgrade SQL Server log shipping"
topic: "high-availability"
description: |
  ﾃ
  
  Summarize this article for me
  
  Applies to:
  
  SQL Server
  
  To preserve your log shipping disaster recovery solution, upgrade, or apply servicing updates in
  
  the appropriate order. Servicing updates in
tags:
  - "high-availability"
  - "upgrade-sql-server-log-shipping"
pubDate: 2025-12-01
---

ﾃ

Summarize this article for me

Applies to:

SQL Server

To preserve your log shipping disaster recovery solution, upgrade, or apply servicing updates in

the appropriate order. Servicing updates include service packs or cumulative updates.

Before you begin, review the following important information.

Description

Supported version and

edition upgrades

Verify that you can upgrade to your desired version of SQL Server from

your existing Windows operating system and version of SQL Server. For

example, you can't upgrade directly from a SQL Server 2005 (9.x) instance

to SQL Server 2025 (17.x).

Choose a Database Engine

upgrade method

Select the appropriate upgrade method and steps based on your review of

supported version and edition upgrades. Also consider other components

installed in your environment to upgrade components in the correct order.

Plan and test Database

Engine upgrade plan

Review the release notes and known upgrade issues, the pre-upgrade

checklist, and develop and test the upgrade plan.

Hardware and software

requirements for installing

SQL Server

Review the software requirements for installing SQL Server. If other

software is required, install it on each node before you begin the upgrade

process to minimize any downtime.

Contained availability group

support

added in SQL

If you want to start using contained availability groups with log shipping,

you need to drop and recreate the log shipping topology. However, if

７

Note

An upgraded log shipping configuration uses the

server-level

configuration option to control whether

is used for the transaction

log backup files. You can specify the backup compression behavior of log backups for

each log shipping configuration. For more information, see

.

ﾉ

Expand table

```cmd
backup compression default
```