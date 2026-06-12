---
title: "View Always On failover cluster"
topic: "azure-synapse"
description: |
  Article

  •

  07/30/2024

  Applies to:

  SQL Server

  Azure portal provides information about SQL Server failover cluster instances when they are

  enabled by Azure Arc. The Azure SQL extension agent must b
tags:
  - "azure-synapse"
  - "view-always-on-failover-cluster"
pubDate: 2025-12-01
---

Article

•

07/30/2024

SQL Server

Azure portal provides information about SQL Server failover cluster instances when they are

enabled by Azure Arc. The Azure SQL extension agent must be installed on all the nodes of the

failover cluster instance. The agents project the installation into Azure as a SQL

Server enabled by Azure Arc resource.

For details about failover cluster instances, review

Always On failover cluster instances (SQL

Server).

You can see all the resources like network name, databases and all the nodes in the

corresponding resource group.

In Azure portal,

lists all instances of SQL Server that are

enabled by Azure Arc.

To list only the failover cluster instances:

1. Select.

2. Set

to

instance type

equals.

3. Select.

）

Important

To view the latest features, make sure the server resource has the latest extension. The

latest extension information is published at. To update extensions, follow the instructions at either of these locations:
