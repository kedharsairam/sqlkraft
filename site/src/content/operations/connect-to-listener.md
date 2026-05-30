---
title: "Connect to listener"
topic: "high-availability"
description: |
  Applies to:

  SQL Server

  This article teaches you how to connect to an

  Always On availability group listener

  for SQL

  Server. An availability group listener is a virtual network name that clients us
tags:
  - "high-availability"
  - "connect-to-listener"
pubDate: 2025-12-01
---

Applies to:

SQL Server

This article teaches you how to connect to an

Always On availability group listener

for SQL

Server. An availability group listener is a virtual network name that clients use to connect to a

database hosted in an availability group. The listener provides a consistent connection

endpoint for client applications, regardless of which availability replica is currently hosting the

primary database. The listener also enables support for read-only routing and automatic

failover.

After you've

configured your listener

, update your connection strings to point to the listener so

that application traffic is automatically routed to the intended replica without having to

manually update the connection string after every failover.

Specify the availability group listener DNS name in the connection string to connect to the

primary replica for read-write access.

For example, to connect to the primary replica in SQL Server Management Studio through the

listener, enter the listener DNS name in the server name field:
