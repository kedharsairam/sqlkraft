---
title: "Configure with custom high availability logic"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  This article explains how to configure a SQL Server Always On availability group (AG) on Linux

  using custom high availability and failover logic. This architecture
tags:
  - "linux-operations"
  - "configure-with-custom-high-availability-logic"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

This article explains how to configure a SQL Server Always On availability group (AG) on Linux

using custom high availability and failover logic. This architecture uses

to allow manual or script-driven control over replica management. It's ideal for

environments requiring tailored high availability and failover strategies. While data

synchronization between replicas is handled by SQL Server, the high availability and failover

mechanisms must be implemented externally.

Uses a

cluster manager

to provide automated failover and enhanced business continuity.

Recommended for production environments requiring minimal downtime.

To configure this setup, see

Configure SQL Server availability group for high availability on

Linux

.

Configured with

, this model

use a cluster manager.

Supports read-only workloads and can include replicas across different operating

systems.

Not suitable for high availability scenarios.

For setup instructions, see

Configure a SQL Server availability group for read-scale on

Linux

.

Offers flexibility to implement

using external scripts.

Configured with

, allowing manual or scripted management of

availability replicas.

```cmd
CLUSTER_TYPE =
EXTERNAL
CLUSTER_TYPE = NONE
CLUSTER_TYPE = EXTERNAL
```
