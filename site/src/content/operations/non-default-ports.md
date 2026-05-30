---
title: "Non-default ports"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  You can configure replication with SQL Server on Linux instances listening on any port configured

  with the

  mssql-conf setting. The port needs to be appended to the
tags:
  - "linux-operations"
  - "non-default-ports"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

You can configure replication with SQL Server on Linux instances listening on any port configured

with the

mssql-conf setting. The port needs to be appended to the server name

during configuration if the following conditions are true:

Replication set-up involves an instance of SQL Server on Linux

Any instance (Windows or Linux) is listening on a nondefault port.

The server name of an instance can be found by running

on the instance. Don't use

the IP address instead of the server name. Using the IP address for the publisher, distributor, or

subscriber might result in an error.

listens on port 1500 on Linux. To configure

for distribution, run

with

. For example:

listens on port 1500 on Linux. To configure a publisher for the distributor, run

with

. For example:

７

Note

Creating SQL Server replication on Linux with nondefault port will only work with SQL Server

2019 and above.

```cmd
network.tcpport
@@SERVERNAME
Server1
Server1 sp_adddistributor
```
