---
title: "Configure flexible failover policy"
topic: "high-availability"
description: "- Windows only This topic describes how to configure the flexible failover policy for an Always On availability group by using Transact-SQL or PowerS"
tags: ["high-availability","configure-flexible-failover-policy"]
pubDate: 2025-12-01
---

- Windows only

This topic describes how to configure the flexible failover policy for an Always On availability

group by using Transact-SQL or PowerShell in SQL Server. A flexible failover policy provides

granular control over the conditions that cause

automatic failover

for an availability group. By

changing the failure conditions that trigger an automatic failover and the frequency of health

checks, you can increase or decrease the likelihood of an automatic failover to support your

SLA for high availability.

The flexible failover policy of an availability group is defined by its failure-condition level and

health-check timeout threshold. On detecting that an availability group has exceeded its failure

condition level or its health-check timeout threshold, the availability group's resource DLL

responds back to the Windows Server Failover Clustering (WSFC) cluster. The WSFC cluster

then initiates an automatic failover to the secondary replica.

For an automatic failover to occur, the current primary replica and one secondary replica

must be configured for synchronous-commit availability mode with automatic failover

and the secondary replica must be synchronized with the primary replica.

2019 (15.x) increased the maximum number of synchronous replicas to 5, up

from 3 in SQL Server 2017 (14.x). You can configure this group of five replicas to have

automatic failover within the group. There is one primary replica, plus four synchronous

secondary replicas.

If an availability group exceeds its WSFC failure threshold, the WSFC cluster will not

attempt an automatic failover for the availability group. Furthermore, the WSFC resource

group of the availability group remains in a failed state until either the cluster

administrator manually brings the failed resource group online or the database

administrator performs a manual failover of the availability group. The

WSFC failure

７

Note

The flexible failover policy of an availability group cannot be configured by using SQL

Server Management Studio.
