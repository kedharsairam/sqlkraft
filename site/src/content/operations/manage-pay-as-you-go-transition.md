---
title: "Manage pay-as-you-go transition"
topic: "azure-synapse"
description: |
  This article explains how to transition the SQL Server instances to pay-as-you-go subscriptions.

  This option is available for instances of SQL Server that currently:

  Use a SQL Server license with So
tags:
  - "azure-synapse"
  - "manage-pay-as-you-go-transition"
pubDate: 2025-12-01
---

This article explains how to transition the SQL Server instances to pay-as-you-go subscriptions.

This option is available for instances of SQL Server that currently:

Use a SQL Server license with Software Assurance (SA)

Use a SQL Server subscription license

Licensed through a Services Provider License Agreement (SPLA)

If your SQL Server instances are covered by a license with Software assurance or a subscription

license, typically you want to transition to a pay-as-you-go Azure subscription immediately

after the expiration time. At that point you want to make sure that:

All Arc SQL deployments are switched to pay-as-you-go billing.

All Azure SQL deployments (PaaS and IaaS) are switched to pay-as-you-go billing.

The transition tasks are executed immediately after the license agreement expiration for

continuous compliance and accurate billing.

To manage the transition follow these steps.

Make sure you have an active Azure account with at least one subscription.

Make sure that all on-premises SQL Server instances covered by the license with Software

assurance or by SQL subscription are connected to Azure Arc.

If you license virtual cores or physical cores without using VMs, make sure that the Azure

extensions for SQL Server are configured with

set to. See

License SQL

Server instances by virtual cores

and

License SQL Server instances by physical cores

without VMs

for details.

If you use the unlimited virtualization licensing method, make sure the p-core license or

licenses are created with

set to

, activated and all SQL Servers instances

subscription

```cmd
licenseType
Paid billingPlan
Paid
```
