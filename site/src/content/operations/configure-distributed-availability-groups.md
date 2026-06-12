---
title: "Configure distributed availability groups"
topic: "high-availability"
description: |
  05/27/2025

  Applies to:

  SQL Server

  To create a distributed availability group, you must create two availability groups each with its

  own listener. You then combine these availability groups into a
tags:
  - "high-availability"
  - "configure-distributed-availability-groups"
pubDate: 2025-12-01
---

05/27/2025

SQL Server

To create a distributed availability group, you must create two availability groups each with its

own listener. You then combine these availability groups into a distributed availability group.

The following steps provide a basic example in Transact-SQL. This example doesn't cover all of

the details of creating availability groups and listeners; instead, it focuses on highlighting the

key requirements.

For a technical overview of distributed availability groups, see

Distributed availability groups.

To configure a distributed availability group, you must have the following:

A supported version of

SQL Server.

Requires

permission on the server to create an availability

group and

to fail over a distributed availability group.

Make sure the endpoints can communicate between the different availability groups in the

distributed availability group. If one availability group is set to a specific network on the

endpoint, the distributed availability group doesn't work properly. On each server that hosts a

７

Note

If you configured the listener for your availability group on your SQL Server on Azure VM

by using a distributed network name (DNN), then configuring a distributed availability

group on top of your availability group isn't supported. To learn more, see

on.

```cmd
sysadmin
```
