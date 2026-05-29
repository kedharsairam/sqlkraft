---
title: "Manage Always On availability group"
topic: "azure-synapse"
description: |
  06/10/2025

  Applies to:

  SQL Server

  An Always On availability group is an enterprise level high availability and disaster recovery

  solution for SQL Server. This article describes how to manage a SQL
tags:
  - "azure-synapse"
  - "manage-always-on-availability-group"
pubDate: 2025-12-01
---

06/10/2025

Applies to:

SQL Server

An Always On availability group is an enterprise level high availability and disaster recovery

solution for SQL Server. This article describes how to manage a SQL Server enabled by Azure

Arc instance, in Azure portal. Specifically you can:

View list of availability groups and status

Failover

You have a

Contributor role

or a

Custom role

with

permissions in at least one of

the Azure subscriptions that your organization created.

Learn how to create a new subscription

.

Follow the steps to view the availability groups that are configured for the SQL Server enabled

by Azure Arc:

1. In your Azure portal, browse to the overview page of the SQL Server enabled by Azure

Arc

2. Select

Azure portal will display the availability groups configured for the SQL Server instance on

the right

3. Select the availability group that you want to review

Azure portal displays the health and status of the Always on Availability Group similar to the

Availability Group dashboard shown in SQL Server Management Studio. This includes:

The current primary replica

Availability group state

Availability group replicas

Failover mode

```cmd
Microsoft.AzureArcData/SqlServerInstances/AvailabilityGroups
```
