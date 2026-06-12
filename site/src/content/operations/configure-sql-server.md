---
title: "Configure SQL Server"
topic: "azure-synapse"
description: "Each Azure Arc-enabled server includes a set of properties that apply to all SQL Server instances installed on that server. You can configure these properties after Azure Ext"
tags: ["azure-synapse","configure-sql-server"]
pubDate: "2025-12-01"
---

Each Azure Arc-enabled server includes a set of properties that apply to all SQL Server

instances installed on that server. You can configure these properties after Azure Extension for

is installed on the machine. However, the properties take effect only if a SQL Server

instance or instances are installed. In the Azure portal, the

pane for SQL Server

enabled by Azure Arc reflects how the SQL Server configuration affects a particular instance.

You have a

Contributor role

in at least one of the Azure subscriptions that your

organization created.

Learn how to create a new billing subscription.

You have a

Contributor role

for the resource group in which the SQL Server instance will

be registered. For details, see

Managed Azure resource groups.

The

and

resource providers are

registered in each subscription that you use for SQL Server pay-as-you-go billing.

To register the resource providers, use one of the following methods:

1. Select.

2. Choose your subscription.

3. Under

, select.

4. Search for

and

, and then select.

You can use the Azure portal, Azure PowerShell, or the Azure CLI to change all or some

configuration settings on a specific Azure Arc-enabled server to the desired state.

Azure portal

```cmd
Microsoft.AzureArcData
Microsoft.HybridCompute
Microsoft.AzureArcData
Microsoft.HybridCompute
```
