---
title: "Change replica failover mode"
topic: "high-availability"
description: "This topic describes how to change the failover mode of an availability replica in an Always On availability group in SQL Server by using SQL Server M"
tags: ["high-availability","change-replica-failover-mode"]
pubDate: 2025-12-01
---

This topic describes how to change the failover mode of an availability replica in an Always On

availability group in SQL Server by using SQL Server Management Studio, Transact-SQL, or

PowerShell. The failover mode is a replica property that determines the failover mode for

replicas that run under synchronous-commit availability mode. For more information, see

Failover and Failover Modes (Always On Availability Groups)

and

Availability Modes (Always On

Availability Groups).

This task is supported only on primary replicas. You must be connected to the server

instance that hosts the primary replica.

Failover Cluster Instances (FCIs) do not support automatic failover by

availability groups, so any availability replica that is hosted by an FCI can only be

configured for manual failover.

Requires ALTER AVAILABILITY GROUP permission on the availability group, CONTROL

AVAILABILITY GROUP permission, ALTER ANY AVAILABILITY GROUP permission, or CONTROL

SERVER permission.

1. In Object Explorer, connect to the server instance that hosts the primary replica, and

expand the server tree.

2. Expand the

node and the

node.

3. Click the availability group whose replica you want to change.

4. Right-click the replica, and click.

Prerequisites and Restrictions
