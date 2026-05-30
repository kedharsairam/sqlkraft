---
title: "Use MSDTC with containers"
topic: "linux-operations"
description: |
  SQL Server Linux containers

  07/03/2025

  Applies to:

  SQL Server

  - Linux

  This article explains how to set up SQL Server Linux containers for distributed transactions,

  including special requirements
tags:
  - "linux-operations"
  - "use-msdtc-with-containers"
pubDate: 2025-12-01
---

SQL Server Linux containers

07/03/2025

Applies to:

SQL Server

- Linux

This article explains how to set up SQL Server Linux containers for distributed transactions,

including special requirements and scenarios.

SQL Server container images can use the Microsoft Distributed Transaction Coordinator

(MSDTC), which is required for distributed transactions. To understand the communications

requirements for MSDTC, see

How to configure the Microsoft Distributed Transaction

Coordinator (MSDTC) on Linux

.

To enable MSDTC transaction in SQL Server containers, you must set two new environment

variables:

: the TCP port that RPC endpoint mapper service binds to and listens on.

: the port that MSDTC service is configured to listen on.

The following example shows how to use these environment variables to pull and run a single

SQL Server 2019 (15.x) container configured for MSDTC. This allows it to communicate with any

application on any hosts.

Bash

７

Note

SQL Server 2017 (14.x) runs in root containers by default, whereas SQL Server 2019 (15.x)

and later containers run as a non-root user.

）

Important

The

environment variable is deprecated. Use

instead.

```cmd
MSSQL_RPC_PORT
MSSQL_DTC_TCP_PORT
SA_PASSWORD
MSSQL_SA_PASSWORD
```
