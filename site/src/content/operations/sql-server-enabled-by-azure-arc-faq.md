---
title: "SQL Server enabled by Azure Arc FAQ"
topic: "azure-arc"
description: |
  Yes, you can use the

  setting in the Azure Policy to indicate the SQL Server

  instances that you don't want to include in the onboarding process.

  For example, if you have any standby instances, you m
tags:
  - "azure-arc"
  - "sql-server-enabled-by-azure-arc-faq"
pubDate: 2025-12-01
---

Yes, you can use the

setting in the Azure Policy to indicate the SQL Server

instances that you don't want to include in the onboarding process.

For example, if you have any standby instances, you might not want to view them in the portal.

When you use Azure Policy to onboard, you can exclude such instances based using pattern

matching of the instance names.

1. Create a copy of the definition that we provide in Azure to create a custom definition.

2. Set the value for excluded instances in the custom definition.

3. Target the subscription and resource group.

No. Microsoft only captures metadata and information about your SQL Server to help

troubleshoot and inventory. The data sent doesn't include user data or about your utilization of

SQL Server.

```cmd
excludedInstances
```
