---
title: "Configure read-only routing"
topic: "high-availability"
description: |
  Article

  •

  03/15/2025

  Applies to:

  SQL Server

  To configure an Always On availability group to support read-only routing in SQL Server, you

  can use either Transact-SQL or PowerShell.

  Read-only rou
tags:
  - "high-availability"
  - "configure-read-only-routing"
pubDate: 2025-12-01
---

Article

•

03/15/2025

Applies to:

SQL Server

To configure an Always On availability group to support read-only routing in SQL Server, you

can use either Transact-SQL or PowerShell.

Read-only routing

refers to the ability of SQL Server

to route qualifying read-only connection requests to an available Always On

readable

secondary replica

(that is, a replica that is configured to allow read-only workloads when

running under the secondary role). To support read-only routing, the availability group must

possess an

availability group listener

. Read-only clients must direct their connection requests

to this listener, and the client's connection strings must specify the application intent as "read-

only." That is, they must be

read-intent connection requests

.

Read-only routing is available in SQL Server 2016 (13.x) and later.

The availability group must possess an availability group listener. For more information,

see

Create or Configure an Availability Group Listener (SQL Server)

.

One or more availability replicas must be configured to accept read-only in the secondary

role (that is, to be

readable secondary replicas

). For more information, see

Configure

Read-Only Access on an Availability Replica (SQL Server)

.

You must be connected to the server instance that hosts the current primary replica.

If using a SQL Login, make sure the account is configured correctly. For more information,

see

Management of Logins and Jobs for the Databases of an Availability Group (SQL

Server)

.

７

Note

For information about how to configure a readable secondary replica, see

.
