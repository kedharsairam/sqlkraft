---
title: "View replica properties"
topic: "high-availability"
description: "This topic describes how to view the properties of an availability replica for an Always On availability group by using SQL Server Management Studio o"
tags: ["high-availability","view-replica-properties"]
pubDate: 2025-12-01
---

This topic describes how to view the properties of an availability replica for an Always On

availability group by using SQL Server Management Studio or Transact-SQL in SQL Server.

1. In Object Explorer, connect to the server instance that hosts the primary replica, and

expand the server tree.

2. Expand the

node and the

node.

3. Expand the availability group to which the availability replica belongs, and expand the

node.

4. Right-click the availability replica whose properties you want to view, and select the

command.

5. In the

dialog box, use the

page to view the

properties of this replica. If you are connected to the primary replica, you can change the

following properties: availability mode, failover mode, connection access for the primary

role, read-access for the secondary role (readable-secondary), and the session-timeout

value. For more information, see

Availability Replica Properties (General Page).

[!NOTE]

If the cluster type is none, you cannot change the failover mode.

To view the properties and states of availability replicas, use the following views and system

function:

sys.availability_replicas

Returns a row for every availability replica in each availability group for which the local instance
