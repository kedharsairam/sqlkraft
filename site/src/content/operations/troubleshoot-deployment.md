---
title: "Troubleshoot deployment"
topic: "azure-synapse"
description: |
  Applies to:

  SQL Server

  Before you start, note the logs locations.

  The extension log file is at:

  The log file name depends on the version Azure Extension for SQL Server, for the latest version

  of
tags:
  - "azure-synapse"
  - "troubleshoot-deployment"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Before you start, note the logs locations.

The extension log file is at:

The log file name depends on the version Azure Extension for SQL Server, for the latest version

of Azure Extension for SQL Server, the log file is:

For extension version

and earlier, the log file is:

The deployer logs are deployed at:

Replace

with your extension version. For example:

The failure to create the Arc-enabled SQL Server resource could be caused by several issues.

```cmd
C:\ProgramData\GuestConfig\extension_logs\Microsoft.AzureData.WindowsAgent.SqlServer\
unifiedagent.log
1.1.24724.69
ExtensionLog_0.log
C:\ProgramData\GuestConfig\extension_logs\Microsoft.AzureData.WindowsAgent.SqlServer\
<extension version>\deployer.log
```
