---
title: "Failover & failover modes"
topic: "high-availability"
description: |
  06/16/2025

  Applies to:

  SQL Server

  This article describes failover and failover modes for SQL Server

  Always On availability groups

  .

  Within the context of an availability group, the primary role
tags:
  - "high-availability"
  - "failover-failover-modes"
pubDate: 2025-12-01
---

06/16/2025

Applies to:

SQL Server

This article describes failover and failover modes for SQL Server

Always On availability groups

.

Within the context of an availability group, the primary role and secondary role of availability

replicas are typically interchangeable in a process known as

failover

. Three forms of failover

exist: automatic failover (without data loss), planned manual failover (without data loss), and

forced manual failover (with possible data loss), typically called

forced failover

. Both automatic

and planned manual failover preserve all your data. An availability group fails over at the

availability-replica level. That is, an availability group fails over to one of its secondary replicas

(the current

failover target

).

During the failover, the failover target takes over the primary role, recovers its databases, and

brings them online as the new primary databases. The former primary replica, when available,

switches to the secondary role, and its databases become secondary databases. Potentially,

these roles can switch back and forth (or to a different failover target) in response to multiple

failures or for administrative purposes.

The forms of failover that a given availability replica supports is specified by the

failover mode

property. For a given availability replica, the possible failover modes depend on the

availability

mode

of the replica, as follows:

support two settings-automatic or manual. The

"automatic" setting supports both automatic failover and manual failover. To prevent data

loss, automatic failover and planned failover require that the failover target be a

synchronous-commit secondary replica with a healthy synchronization state (this

indicates that every secondary database on the failover target is synchronized with its

corresponding primary database). Whenever a secondary replica doesn't meet both of

７

Note

Unless

is configured, issues at the database level, such

as a database becoming suspect due to the loss of a data file, deletion of a database, or

corruption of a transaction log, don't cause an availability group to failover.
