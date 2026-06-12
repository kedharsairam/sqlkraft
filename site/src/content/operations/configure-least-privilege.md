---
title: "Configure least privilege"
topic: "azure-synapse"
description: |
  Applies to:

  SQL Server

  The information security principle of least privilege asserts that accounts and applications only

  have access to the data and operations they require. With SQL Server enabled
tags:
  - "azure-synapse"
  - "configure-least-privilege"
pubDate: 2025-12-01
---

SQL Server

The information security principle of least privilege asserts that accounts and applications only

have access to the data and operations they require. With SQL Server enabled by Azure Arc, you

can run the agent extension service with least privilege. This article explains how to run the agent

extension service with least privilege.

To optionally configure the service to run with least privilege, follow the steps in this article.

Currently, the service doesn't automatically run with least privilege.

Configure Windows service accounts and permissions for Azure Extension for SQL Server

describes the least privilege permissions for the agent extension service.

After you configure the agent extension service to run with least privilege, it uses the

service account.

The

account is a local Windows service account:

Created and managed by the Azure Extension for SQL Server when least privilege option is

enabled.

Granted the minimum required permissions and privileges to run the Azure Extension for

service on the Windows operating system. It only has access to folders and

directories used for reading and storing configuration or writing logs.

Granted permission to connect and query in SQL Server with a new login specifically for that

service account that has the minimum permissions required. Minimum permissions depend

on the enabled features.

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
1.1.2859.223
1.1.2859.223
```
