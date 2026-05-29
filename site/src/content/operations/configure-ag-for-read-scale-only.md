---
title: "Configure AG for read-scale only"
topic: "linux-operations"
description: |
  07/03/2025

  Applies to:

  SQL Server

  - Linux

  This article explains how to create a SQL Server Always On Availability Group (AG) on Linux

  without

  a cluster manager. This architecture provides read-s
tags:
  - "linux-operations"
  - "configure-ag-for-read-scale-only"
pubDate: 2025-12-01
---

07/03/2025

Applies to:

SQL Server

- Linux

This article explains how to create a SQL Server Always On Availability Group (AG) on Linux

without

a cluster manager. This architecture provides read-scale only. It

doesn't

provide high

availability.

There are two types of architectures for availability groups. An architecture for

high availability

uses a

cluster manager

to provide improved business continuity. To create the high-availability

architecture, see

Configure SQL Server Always On Availability Group for high availability on

Linux

.

An availability group with

can include replicas hosted on different

operating system platforms. It can't support high availability.

Before you create the availability group, you need to:

Set your environment so that all the servers that will host availability replicas can

communicate.

Install SQL Server.

On Linux, you must create an availability group before you add it as a cluster resource to be

managed by the cluster. This document provides an example that creates the availability group.

1. Update the computer name for each host.

Each SQL Server instance name must be:

15 characters or fewer.

Unique within the network.

To set the computer name, edit

. The following script lets you edit

with

:

Bash

```cmd
CLUSTER_TYPE = NONE
/etc/hostname
/etc/hostname
sudo vi /etc/hostname
```
