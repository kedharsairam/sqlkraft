---
title: "Point-in-time restore (preview)"
topic: "azure-synapse"
description: "This article demonstrates how to restore a database to a point-in-time as a new database on the same instance of SQL Server enabled by Azure Arc. The"
tags: ["azure-synapse","point-in-time-restore-preview"]
pubDate: 2025-12-01
---

This article demonstrates how to restore a database to a point-in-time as a new database on

the same instance of SQL Server enabled by Azure Arc.

The new database is restored from backup to a point-in-time in the past that is within the

retention period.

Before you can restore a database to a point-in-time with the instructions in this article, you

have to enable automatic backups. For instructions, see

Manage automated backups - SQL

Server enabled by Azure Arc.

Automated backups are disabled by default.

To restore to a point-in-time from Azure portal:

1. Browse to the Arc-enabled SQL Server

2. Select

3. Among the list of databases on the right pane, select

for the database you

want to restore.

Azure portal guides you through the instructions to create a database with the

selected database as the source database.

７

Note

As a preview feature, the technology presented in this article is subject to.

The latest updates are available in the.

Azure portal
