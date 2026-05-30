---
title: "Known issues"
topic: "azure-synapse"
description: |
  ﾃ

  Summarize this article for me

  This article provides information about known issues associated with SQL Server enabled by

  Azure Arc.

  If a database isn't online and updatable, required permissions
tags:
  - "azure-synapse"
  - "known-issues-2"
pubDate: 2025-12-01
---

ﾃ

Summarize this article for me

This article provides information about known issues associated with SQL Server enabled by

Azure Arc.

If a database isn't online and updatable, required permissions aren't assigned to that database.

Features requiring permissions to that database are affected.

Verify that the databases are online and updateable. Review

Verify state of user

databases

.

Check the error logs. The error log might show Microsoft SQL Server error 945:

To resolve, follow the steps at

MSSQLSERVER_945

.

Currently

tags are not included in cost reports. For updates, review

Microsoft.AzureArcData tag support

You might occasionally see throttling notifications for Azure resource updates in Activity log, as

shown below. This behavior is expected due to service-imposed rate limits. Updates for SQL

Server instances, databases, and availability groups inventory run continuously on an hourly

basis and should eventually complete successfully.

```cmd
Microsoft.AzureArcData
Database cannot be opened due to inaccessible files or insufficient memory or disk space
```
