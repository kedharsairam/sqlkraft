---
title: "Troubleshoot common issues"
topic: "azure-synapse"
description: |
  ﾃ
  
    Summarize this article for me
  
    This article helps you troubleshoot common issues you might encounter when migrating SQL
  
    Server databases to Azure SQL Managed Instance by using SQL Server migration
tags: ["azure-synapse","troubleshoot-common-issues"]
pubDate: "2025-12-01"
---

ﾃ

Summarize this article for me

This article helps you troubleshoot common issues you might encounter when migrating SQL

Server databases to Azure SQL Managed Instance by using SQL Server migration in Azure Arc.

When you use SQL Server migration in Azure Arc, certain features require a minimum version

of the Arc agent. The Arc agent is an executable that runs alongside your SQL Server instance

to provide connectivity to Azure. Always keep your Arc agent version up to date to get the

latest fixes and updates.

With

automatic updates

enabled, the Arc agent stays up to date automatically. However, when

a new version of the Arc agent rolls out, it can take a few days for the update to reach all

servers. You can speed up the process by

manually executing an on-demand Arc agent update

through either the Azure portal or command line interfaces.

If you see the following error when accessing the

pane in the Azure portal,

you need to upgrade your Arc agent to a supported version:

If you encounter issues with the Arc agent, such as an unhealthy extension state or a

disconnected SQL Server instance, use the following extension troubleshooting guide:

Troubleshoot Azure extension for SQL Server.

７

Note

You can provide feedback about your migration experience.

```cmd
To enable migration and monitoring capabilities,
please update your Azure Arc agent extension "WindowsAgentSQLServer" to the latest version.
```
