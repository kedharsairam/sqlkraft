---
title: "Client connection summary"
topic: "azure-synapse"
description: "This article teaches you how to view client connections to SQL Server enabled by Azure Arc in Azure portal. To collect client connection data for SQL Server enabled by Azure"
tags: ["azure-synapse","client-connection-summary"]
pubDate: 2025-12-01
---

This article teaches you how to view client connections to SQL Server enabled by Azure Arc in

Azure portal.

To collect client connection data for SQL Server enabled by Azure Arc and view the summary in

Azure, you must meet the following conditions:

The version of Azure Extension for SQL Server (

) is v1.1.2986.256

or greater.

enabled by Azure Arc is running on the Windows operating system.

running on Windows Server 2012 R2 and older versions aren't supported.

The SQL Server version is SQL Server 2016 (13.x) with Service Pack 1 or greater.

The server has connectivity to. For more information, see

the

network requirements.

The license type on SQL Server enabled by Azure Arc is Software Assurance or pay-as-

you-go.

You have an Azure role with the action. You can use the following

built-in role, which includes this action:

Azure Hybrid Database Administrator - Read Only

Service Role. For more information, see

Azure built-in roles.

To view a summary of all client connections to the SQL Server instance, follow these steps:

1. Select an instance of SQL Server enabled by Azure Arc in the

Azure portal.

2. Under

, select

Connections.

3. (Optionally) Use the time range to view connections during a preferred window within the

last 30 days.

```cmd
WindowsAgent.SqlServer
*.<region>.arcdataservices.com
Microsoft.AzureArcData/sqlServerInstances/getTelemetry/
```
