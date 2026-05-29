---
title: "Migrating to Windows Server 2012 & 2016"
topic: "high-availability"
description: |
  Article
  
  •
  
  03/03/2023
  
  Windows Server 2008, Windows Server 2008 R2, and Windows Server 2012 prevent Windows
  
  Server failover clusters from performing in-place operating system upgrades, capping the
  
  
tags:
  - "high-availability"
  - "migrating-to-windows-server-2012-2016"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Windows Server 2008, Windows Server 2008 R2, and Windows Server 2012 prevent Windows

Server failover clusters from performing in-place operating system upgrades, capping the

allowed version of SQL Server for a cluster. Once the cluster is upgraded to at least Windows

Server 2012 R2, the cluster can remain up-to-date.

Prior to performing any of the migration strategies, a parallel Windows Server failover

cluster with Windows Server 2016/2012 R2 must be prepared. All nodes comprising SQL

Server failover cluster instances (FCIs) must be joined to the Windows cluster with the

parallel FCIs installed. Any standalone machines

be joined to the Windows

Server failover cluster prior to migration. User databases should be synchronized on the

new environment prior to migration.

All destination instances must be running the same version of SQL Server as their parallel

instance in the original environment, with the same instance names and IDs, and installed

with the same features. Installation paths and directory structure should be identical on

the destination machines. This does not include FCI virtual network names, which must be

different prior to migration. Any features enabled by the original instance (Always On,

FILESTREAM, etc.) should be enabled on the destination instance.

The parallel cluster should have no Always On availability groups installed prior to

migration.

Downtime when migrating a cluster that uses strictly Availability Groups (with or without

SQL FCIs) can be greatly limited by using Distributed Availability Groups, but this does

require that all instances run SQL Server 2016 (13.x) RTM (or above) versions.

All migration strategies require SQL Server sysadmin role. All Windows users used by SQL

Server services (i.e. Windows account running replication agents) must have the OS level

permissions on each machine in the new environment.

Any network file shares and network mapped drives used in the original SQL Server

cluster environment must still exist and remain accessible by the target cluster with the

same permissions as the original instances.