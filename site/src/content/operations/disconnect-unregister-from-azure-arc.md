---
title: "Disconnect & unregister from Azure Arc"
topic: "azure-arc"
description: |
  Applies to:

  SQL Server

  This article describes how to disconnect SQL Server instances from Azure Arc by using the Azure

  portal or a command shell. It applies to SQL Server instances enabled by Azure
tags:
  - "azure-arc"
  - "disconnect-unregister-from-azure-arc"
pubDate: 2025-12-01
---

Applies to:

SQL Server

This article describes how to disconnect SQL Server instances from Azure Arc by using the Azure

portal or a command shell. It applies to SQL Server instances enabled by Azure Arc. To stop

managing a SQL Server instance with Azure Arc, remove the SQL Server extension. After you

complete these steps, SQL Server - Azure Arc resources and associated components are fully

removed from your system and Azure.

Your Azure account must have a

Contributor role

for the instance subscription and resource

group.

Before you uninstall Azure Extension for SQL Server, opt out of automatic installation of the

extension by adding the following tag and value to the Azure Arc-enabled SQL Server resource:

Alternatively, you can limit which extensions can be installed on your server. You can configure

lists of the extensions that you want to allow and block on the server. To learn more, see

Allow

lists and block lists

.

７

Note

You don't need access to the hosting machine to disconnect from Azure Arc.

ﾉ

Expand table

```cmd
ArcSQLServerExtensionDeployment
Disabled
```
