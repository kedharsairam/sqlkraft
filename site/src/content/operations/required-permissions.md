---
title: "Required permissions"
topic: "azure-synapse"
description: "This article lists the permissions the Azure Extension for SQL Server grants to the account when you use least privilege for SQL Server instances enabled by A"
tags: ["azure-synapse","required-permissions"]
pubDate: "2025-12-01"
---

This article lists the permissions the Azure Extension for SQL Server grants to the

account when you use

least privilege

for

instances

enabled by Azure Arc. With the least privilege configuration, the extension grants only necessary

permissions when you enable features in the Azure portal.

When you connect SQL Server to Azure Arc with

least privilege

enabled, the Azure Arc extension

grants its service account,

, only the permissions each feature

needs when you enable that feature. The extension automatically removes those permissions if

you disable the feature. If a feature is inactive, the extension doesn't grant any permissions for

that feature.

Manually setting the permissions for the agent account isn't supported.

The section

SQL privileges by feature

explains the permissions the extension grants when you

enable the following features:

７

Note

must have access to modify permissions on listed directories and

registry keys. This access is necessary so that

can grant required access

to the

account for least privilege mode.

Additionally,

must have an active SQL Server login with

permission on each SQL Server instance. The Deployer connects to SQL Server as

to configure all SQL-level permissions described in this article. If this login

is disabled, removed, or has

denied, the Deployer can't configure SQL

permissions in either standard or least-privilege mode. See

for verification

steps.

７

Note

Currently, least privileged configuration is not applied by default.

Existing servers with extension version

or greater will eventually have the least

privileged configuration applied. This extension was released in November, 2024. To prevent

the automatic application of least privilege, block extension upgrades after.

```cmd
NT
SERVICE\SqlServerExtension
NT SERVICE\SqlServerExtension
NT AUTHORITY\SYSTEM
NT AUTHORITY\SYSTEM
NT SERVICE\SqlServerExtension
```
