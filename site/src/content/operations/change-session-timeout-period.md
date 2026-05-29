---
title: "Change session-timeout period"
topic: "high-availability"
description: |
  Article
  
  •
  
  09/04/2024
  
  Applies to:
  
  SQL Server
  
  This topic describes how to configure the session-timeout period of an Always On availability
  
  replica by using SQL Server Management Studio, Transact-
tags:
  - "high-availability"
  - "change-session-timeout-period"
pubDate: 2025-12-01
---

Article

•

09/04/2024

Applies to:

SQL Server

This topic describes how to configure the session-timeout period of an Always On availability

replica by using SQL Server Management Studio, Transact-SQL, or PowerShell in SQL Server.

The session-timeout period is a replica property that controls how many seconds (in seconds)

that an availability replica waits for a ping response from a connected replica before

considering the connection to have failed. By default, a replica waits 10 seconds for a ping

response. This replica property applies only the connection between a given secondary replica

and the primary replica of the availability group. For more information about the session-

timeout period, see

Overview of Always On Availability Groups (SQL Server)

.

You must be connected to the server instance that hosts the primary replica.

We recommend that you keep the time-out period at 10 seconds or greater. Setting the value

to less than 10 seconds creates the possibility of a heavily loaded system missing PINGs and

declaring a false failure.

Requires ALTER AVAILABILITY GROUP permission on the availability group, CONTROL

AVAILABILITY GROUP permission, ALTER ANY AVAILABILITY GROUP permission, or CONTROL

SERVER permission.

1. In Object Explorer, connect to the server instance that hosts the primary replica, and

expand the server tree.

2. Expand the

node and the

node.