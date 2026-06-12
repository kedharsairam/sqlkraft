---
title: "Troubleshoot best practices assessment"
topic: "azure-synapse"
description: "Before you proceed, verify all the necessary are met. The extension log file is at: The log file name depends on the version Azure Exten"
tags: ["azure-synapse","troubleshoot-best-practices-assessment"]
pubDate: 2025-12-01
---

Before you proceed, verify all the necessary

are met.

The extension log file is at:

The log file name depends on the version Azure Extension for SQL Server. For the latest version

of Azure Extension for SQL Server, the log file is:

For extension version

and earlier, the log file is:

The Azure monitor agent log is at:

You might encounter the following issues when you enable best practices assessment.

```cmd
C:\ProgramData\GuestConfig\extension_logs\Microsoft.AzureData.WindowsAgent.SqlServer\
unifiedagent.log
1.1.24724.69
ExtensionLog_0.log
C:\ProgramData\GuestConfig\extension_logs\Microsoft.Azure.Monitor.AzureMonitorWindowsAgen t\Extension.1.log
```
