---
title: "Automate updates"
topic: "azure-synapse"
description: "You can configure automatic updates for SQL Server enabled by Azure Arc. Automatic updates: Establish a maintenance window for an Azure Arc-enabled SQL Server instance. Work"
tags: ["azure-synapse","automate-updates"]
pubDate: 2025-12-01
---

You can configure automatic updates for SQL Server enabled by Azure Arc. Automatic updates:

Establish a maintenance window for an Azure Arc-enabled SQL Server instance.

Work at the level of the host operating system and apply to all installed SQL Server

instances.

Occur only during the maintenance window.

This restriction ensures that system updates and any associated restarts happen at the

best possible time for the SQL Server instances and their hosted databases.

Currently work only on Windows hosts.

They configure Windows Update and Microsoft Update, which are the services that

ultimately update an Azure Arc-enabled SQL Server instance.

Apply Windows and SQL Server updates marked as

Important

or.

You must manually install other SQL Server updates, such as service packs and cumulative

updates that aren't marked as

Important

or.

You can configure automatic updates:

By using the Azure portal.

Programmatically or by policy.

The following table describes the options that you can configure for automatic updates.

Description

|

Enables or disables automatic updates.

|

|

|

|

|

|

|

The weekly schedule for downloading and

installing Windows, SQL Server, and

ﾉ

Expand table
