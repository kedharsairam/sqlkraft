---
title: "Automatic backups (preview)"
topic: "azure-synapse"
description: |
  SQL Server enabled by Azure Arc

  06/30/2025

  Applies to:

  SQL Server

  The Azure extension for SQL Server can perform backups automatically to local storage or

  network shares. Backups are written to t
tags:
  - "azure-synapse"
  - "automatic-backups-preview"
pubDate: 2025-12-01
---

SQL Server enabled by Azure Arc

06/30/2025

Applies to:

SQL Server

The Azure extension for SQL Server can perform backups automatically to local storage or

network shares. Backups are written to the

default backup location

for the SQL Server enabled

by Azure Arc instance.

This article explains how you can:

Enable automated backups

Configure backup schedule

You can enable automated backups through Azure portal or via

CLI.

To enable automated backups, set the retention days to a nonzero value.

Automated backups are only available for licenses with Software Assurance, SQL subscription,

or pay-as-you-go. For details, see

Feature availability depending on license type

.

You can configure two properties for automated backups:

- number of days to retain the backup files. Use a number between 1 and

35. If the backup retention day is set to 0, automated backup is disabled and no backups

are taken, even though backup policy is retained.

- the schedule at which the full, differential, and transaction log backups

should be performed. Depends on backup type:

Full backups: Daily or weekly

Differential backups: Every 12 hours or every 24 hours

Transaction log backups: Increments of 5 minutes.

７

Note

As a preview feature, the technology presented in this article is subject to

.

The latest updates are available in the

.

```cmd
az
```
