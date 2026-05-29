---
title: "Change replica availability"
topic: "high-availability"
description: |
  Article
  
  •
  
  09/04/2024
  
  Applies to:
  
  SQL Server
  
  This topic describes how to change the availability mode of an availability replica in an Always
  
  On availability group in SQL Server by using SQL Serv
tags:
  - "high-availability"
  - "change-replica-availability"
pubDate: 2025-12-01
---

Article

•

09/04/2024

Applies to:

SQL Server

This topic describes how to change the availability mode of an availability replica in an Always

On availability group in SQL Server by using SQL Server Management Studio, Transact-SQL, or

PowerShell. The availability mode is a replica property that controls the whether the replica

commits asynchronously or synchronously.

Asynchronous-commit mode

maximizes

performance at the expense of high availability and supports only forced manual failover (with

possible data loss), typically called

forced failover

.

Synchronous-commit mode

emphasizes high

availability over performance and, once the secondary replica is synchronized, supports manual

failover and, optionally, automatic failover.

You must be connected to the server instance that hosts the primary replica.

Requires ALTER AVAILABILITY GROUP permission on the availability group, CONTROL

AVAILABILITY GROUP permission, ALTER ANY AVAILABILITY GROUP permission, or CONTROL

SERVER permission.

1. In Object Explorer, connect to the server instance that hosts the primary replica, and

expand the server tree.

2. Expand the

node and the

node.

3. Click the availability group whose replica you want to change.

4. Right-click the replica, and click

.

5. In the

dialog box, use the

drop list to

change the availability mode of this replica.