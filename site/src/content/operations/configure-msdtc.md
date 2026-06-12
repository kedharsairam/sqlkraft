---
title: "Configure MSDTC"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  This article describes how to configure the Microsoft Distributed Transaction Coordinator

  (MSDTC) on Linux.

  MSDTC on Linux is supported on SQL Server 2017 (14.x) C
tags:
  - "linux-operations"
  - "configure-msdtc"
pubDate: 2025-12-01
---

SQL Server

on Linux

This article describes how to configure the Microsoft Distributed Transaction Coordinator

(MSDTC) on Linux.

MSDTC on Linux is supported on SQL Server 2017 (14.x) Cumulative Update 16 and later versions.

You enable distributed transactions on SQL Server on Linux by introducing MSDTC and remote

procedure call (RPC) endpoint mapper functionality within SQL Server. By default, an RPC

endpoint-mapping process listens on port 135 for incoming RPC requests and provides

registered components information to remote requests. Remote requests can use the information

returned by endpoint mapper to communicate with registered RPC components, such as MSDTC

services.

A process requires super user privileges to bind to well-known ports (port numbers less than

1024. on Linux. To avoid starting SQL Server with root privileges for the RPC endpoint mapper

process, system administrators must use

to create Network Address Translation to route

traffic on port 135 to the SQL Server instance's RPC endpoint-mapping process.

MSDTC uses two configuration parameters for the

utility:

Description

The TCP port that the RPC endpoint mapper process binds to.

The port that the MSDTC server listens to. If not set, the MSDTC

service uses a random ephemeral port on service restarts, and

firewall exceptions need to be reconfigured to ensure that MSDTC

service can continue communication.

For more information about these settings and other related MSDTC settings, see

Configure SQL

Server on Linux with the mssql-conf tool.

ﾉ

Expand table

```cmd
network.rpcport distributedtransaction.servertcpport
```
