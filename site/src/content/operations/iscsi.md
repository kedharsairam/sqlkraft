---
title: "iSCSI"
topic: "linux-operations"
description: |
  SQL Server on Linux

  Applies to:

  SQL Server

  on Linux

  This article explains how to configure iSCSI storage for a failover cluster instance (FCI) on Linux.

  iSCSI uses networking to present disks fro
tags:
  - "linux-operations"
  - "iscsi"
pubDate: 2025-12-01
---

SQL Server on Linux

Applies to:

SQL Server

on Linux

This article explains how to configure iSCSI storage for a failover cluster instance (FCI) on Linux.

iSCSI uses networking to present disks from a server known as a target to servers. The servers

connecting to the iSCSI target require that an iSCSI initiator is configured. The disks on the target

are given explicit permissions so that only the initiators that should be able to access them can

do so. The target itself should be highly available and reliable.

While this section doesn't cover how to configure an iSCSI target since it's specific to the type of

source you use, ensure that the security for the disks that will be used by the cluster nodes is

configured.

The target should never be configured on any of the FCI nodes if using a Linux-based iSCSI

target. For performance and availability, iSCSI networks should be separate from networks used

by regular network traffic on both the source and the client servers. Networks used for iSCSI

should be fast. Remember that network does consume some processor bandwidth, so plan

accordingly if using a regular server.

The most important thing to ensure is completed on the target is that the disks that are created

are assigned the proper permissions so that only those servers participating in the FCI have

access to them. An example is shown here from the Microsoft iSCSI target where

is

the name created, and in this case, the IP addresses of the nodes are assigned so that

appears to them.

Important iSCSI target information

```cmd
linuxnodes1
NewFCIDisk1.vhdx
```
