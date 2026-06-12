---
title: "NFS"
topic: "linux-operations"
description: |
  SQL Server on Linux

  07/03/2025

  Applies to:

  SQL Server

  - Linux

  This article explains how to configure NFS storage for a failover cluster instance (FCI) on Linux.

  NFS, or network file system, is a
tags:
  - "linux-operations"
  - "nfs"
pubDate: 2025-12-01
---

on Linux

07/03/2025

SQL Server

- Linux

This article explains how to configure NFS storage for a failover cluster instance (FCI) on Linux.

NFS, or network file system, is a common method for sharing disks in the Linux world but not

the Windows one. Similar to iSCSI, NFS can be configured on a server or some sort of

appliance or storage unit as long as it meets the storage requirements for SQL Server.

The source hosting NFS (either a Linux server or something else) must be using/compliant with

version 4.2 or later. Earlier versions don't work with SQL Server on Linux.

When configuring the folders to be shared on the NFS server, make sure they follow these

guidelines general options:

to ensure that the folder can be read from and written to

to ensure guaranteed writes to the folder

Don't use

as an option; it's considered a security risk

Make sure the folder has full rights (

) applied

Ensure that your security standards are enforced for accessing. When configuring the folder,

make sure that only the servers participating in the FCI should see the NFS folder. In the

following example, a modified

on a Linux-based NFS solution is shown, where

the folder is restricted to

and.

Output

1. Choose one of the servers that will participate in the FCI configuration. It doesn't matter

which one.

Important NFS server information

```cmd
rw sync no_root_squash
777
/etc/exports
```
