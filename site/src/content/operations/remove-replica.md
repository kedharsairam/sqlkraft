---
title: "Remove replica"
topic: "high-availability"
description: "This topic describes how to remove a secondary replica from an Always On availability group by using SQL Server Management Studio, Transact-SQL, or Po"
tags: ["high-availability","remove-replica"]
pubDate: 2025-12-01
---

This topic describes how to remove a secondary replica from an Always On availability group

by using SQL Server Management Studio, Transact-SQL, or PowerShell in SQL Server.

This task is supported only on the primary replica.

Only a secondary replica can be removed from an availability group.

You must be connected to the server instance that hosts the primary replica of the

availability group.

Requires ALTER AVAILABILITY GROUP permission on the availability group, CONTROL

AVAILABILITY GROUP permission, ALTER ANY AVAILABILITY GROUP permission, or CONTROL

SERVER permission.

1. In Object Explorer, connect to the server instance that hosts the primary replica, and

expand the server tree.

2. Expand the

node and the

node.

3. Select the availability group, and expand the

node.

4. This step depends on whether you want to remove multiple replicas or only one replica,

as follows:

To remove multiple replicas, use the

pane to view and select

all the replicas that you want to remove. For more information, see

Use the Object
