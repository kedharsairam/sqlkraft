---
title: "Use log shipping"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  Log shipping is a SQL Server high availability (HA) configuration where a database from a

  primary server is replicated onto one or more secondary servers. Log shipp
tags:
  - "linux-operations"
  - "use-log-shipping"
pubDate: 2025-12-01
---

SQL Server

on Linux

Log shipping is a SQL Server high availability (HA) configuration where a database from a

primary server is replicated onto one or more secondary servers. Log shipping allows backup

files from the source database to restore onto the secondary server. The primary server creates

transaction log backups periodically, and the secondary servers restore them, updating the

secondary copy of the database.

As described in the previous diagram, a log shipping session involves the following steps:

Backing up the transaction log file on the primary SQL Server instance

Copying the transaction log backup file across the network to one or more secondary

instances

Restoring the transaction log backup file on the secondary SQL Server instances

Install SQL Server Agent on Linux

７

Note
