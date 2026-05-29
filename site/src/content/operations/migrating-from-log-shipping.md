---
title: "Migrating from log shipping"
topic: "high-availability"
description: |
  Prerequisites to convert log shipping to

  ﾃ

  Summarize this article for me

  Applies to:

  SQL Server

  This article describes the prerequisites for converting a log shipping primary database and one

  or
tags:
  - "high-availability"
  - "migrating-from-log-shipping"
pubDate: 2025-12-01
---

Prerequisites to convert log shipping to

ﾃ

Summarize this article for me

Applies to:

SQL Server

This article describes the prerequisites for converting a log shipping primary database and one

or more secondary databases to an Always On primary and secondary database(s).

To allow backup jobs to run on the primary replica of the availability group, use the following

Always On Availability Groups backup settings:

Automated backup preference of availability group

Only on the primary replica

Back up priority of the primary replica.

> 0

View Availability Group Properties (SQL Server)

Configure Backup on Availability Replicas (SQL Server)

The log shipping primary database must reside on the instance of SQL Server that hosts

the initial/current primary replica of the availability group.

For a given log shipping secondary database to be converted to an Always On secondary

database, it must:

７

Note

You can configure any primary or secondary database (possibly readable) as a log

shipping primary database in an availability group.

ﾉ

Expand table
