---
title: "Fail over - wizard"
topic: "high-availability"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  This topic describes how to perform a planned manual failover or forced manual failover

  (forced failover) on an Always On availability group by using
tags:
  - "high-availability"
  - "fail-over-wizard"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

This topic describes how to perform a planned manual failover or forced manual failover

(forced failover) on an Always On availability group by using SQL Server Management Studio,

Transact-SQL, or PowerShell in SQL Server. An availability group fails over at the level of an

availability replica. If you fail over to a secondary replica in the SYNCHRONIZED state, the

wizard performs a planned manual failover (without data loss). If you fail over to a secondary

replica in the UNSYNCHRONIZED or NOT SYNCHRONIZING state, the wizard performs a forced

manual failover-also known as a

forced failover

(with possible data loss). Both forms of manual

failover transition the secondary replica to which you are connected to the primary role. A

planned manual failover currently transitions the former primary replica to the secondary role.

After a forced failover, when the former primary replica comes online, it transitions to the

secondary role.

Before your first planned manual failover, see the "Before You Begin" section in

Perform a

Planned Manual Failover of an Availability Group (SQL Server)

.

Before your first forced failover, see the "Before You Begin" and "Follow Up: Essential Tasks

After a Forced Failover" sections in

Perform a Forced Manual Failover of an Availability Group

(SQL Server)

.

A failover command returns as soon as the target secondary replica has accepted the

command. However, database recovery occurs asynchronously after the availability group

has finished failing over.

You must be connected to the server instance that hosts an availability replica that is

currently available.

Prerequisites for Using the Failover Availability Group Wizard
