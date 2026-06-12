---
title: "Failover Policy"
topic: "high-availability"
description: ""
tags: ["high-availability","failover-policy"]
pubDate: 2025-12-01
---

In a SQL Server failover cluster instance (FCI), only one node can own the Windows Server

Failover Cluster (WSFC) cluster resource group at a given time. The client requests are served

through this node in the FCI. In the case of a failure and an unsuccessful restart, the group

ownership is moved to another WSFC node in the FCI. This process is called failover. SQL Server

increases the reliability of failure detection and provides a flexible failover policy.

A SQL Server FCI depends on the underlying WSFC service for failover detection. Therefore,

two mechanisms determine the failover behavior for FCI: the former is native WSFC

functionality, and the latter is functionality added by SQL Server setup.

The WSFC cluster maintains the quorum configuration, which ensures a unique failover

target in an automatic failover. The WSFC service determines whether the cluster is in

optimal quorum health at all times and brings the resource group online and offline

accordingly.

The active SQL Server instance periodically reports a set of component diagnostics to the

WSFC resource group over a dedicated connection. The WSFC resource group maintains

the failover policy, which defines the failure conditions that trigger restarts and failovers.

This topic discusses the second mechanism above. For more information on the WSFC behavior

for quorum configuration and health detection, see

WSFC Quorum Modes and Voting

Configuration (SQL Server).

The failover process can be broken down into the following steps:

1.

Monitor the Health Status

2.

Determining Failures

3.

Responding to Failures

）

Important

Automatic failovers to and from an FCI are not allowed in an Always On availability group.

However, manual failovers to and from and FCI are allowed in an Always On availability

group.
