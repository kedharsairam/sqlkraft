---
title: "Configure FailureConditionLevel"
topic: "high-availability"
description: "Use the FailureConditionLevel property to set the conditions for the Always On Failover Cluster Instance (FCI) to fail over or restart."
tags: ["high-availability","configure-failureconditionlevel"]
pubDate: "2025-12-01"
---

Use the FailureConditionLevel property to set the conditions for the Always On Failover Cluster

Instance (FCI) to fail over or restart. Changes to this property are applied immediately without

requiring a restart of the Windows Server Failover Cluster (WSFC) service or the FCI resource.

FailureConditionLevel Property Settings

,

Security

PowerShell

,

Failover

Cluster Manager

,

Transact-SQL

The failure conditions are set on an increasing scale. For levels 1-5, each level includes all the

conditions from the previous levels in addition to its own conditions. This means that with each

level, there is an increased probability of a failover or restart. For more information, see the

"Determining Failures" section of the

Failover Policy for Failover Cluster Instances

topic.

Requires ALTER SETTINGS and VIEW SERVER STATE permissions.

1. Start an elevated Windows PowerShell via.

2. Import the

module to enable cluster cmdlets.

3. Use the

cmdlet to find the SQL Server resource, then use

cmdlet to set the

property for a Failover Cluster

To configure FailureConditionLevel settings
