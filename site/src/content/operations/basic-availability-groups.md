---
title: "Basic availability groups"
topic: "high-availability"
description: |
  10/24/2025

  Applies to:

  SQL Server

  Always On basic availability groups provide a high availability solution for SQL Server 2016

  (13.x) and later versions on Standard edition. A basic availability g
tags:
  - "high-availability"
  - "basic-availability-groups"
pubDate: 2025-12-01
---

10/24/2025

Applies to:

SQL Server

Always On basic availability groups provide a high availability solution for SQL Server 2016

(13.x) and later versions on Standard edition. A basic availability group supports a failover

environment for a single database. It is created and managed much like traditional (advanced)

availability group

with Enterprise edition. The differences and limitations of basic availability

groups are summarized in this document.

Basic availability groups replace the deprecated Database Mirroring feature, and provide a

similar level of feature support. Basic availability groups enable a primary database to maintain

a single replica. This replica can use either synchronous-commit mode or asynchronous-

commit mode. For more information about availability modes, see

Differences between

availability modes for an Always On availability group

. The secondary replica remains inactive

unless there's a need to fail over. This failover reverses the primary and secondary role

assignments, causing the secondary replica to become the primary active database. For more

information on failover, see

Failover and Failover Modes

. Basic availability groups can operate

in a hybrid environment that spans on-premises and Microsoft Azure.

Basic availability groups use a subset of features compared to advanced availability groups on

SQL Server 2016 (13.x) Enterprise edition. Basic availability groups include the following

limitations:

Limit of two replicas (primary and secondary). Basic Availability Groups for SQL Server

2017 (14.x) on Linux support an extra configuration only replica.

No read access on secondary replica.

No backups on secondary replica.

No integrity checks on secondary replicas.

No support for replicas hosted on servers running a version of SQL Server before SQL

Server 2016 (13.x).
