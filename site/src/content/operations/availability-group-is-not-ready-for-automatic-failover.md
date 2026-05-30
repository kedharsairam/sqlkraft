---
title: "Availability group is not ready for automatic failover"
topic: "high-availability"
description: |
  Article

  •

  02/01/2024

  Applies to:

  SQL Server

  : Availability Group Automatic Failover Readiness

  : Availability group is not ready for automatic failover.

  :

  : Availability group

  This policy chec
tags:
  - "high-availability"
  - "availability-group-is-not-ready-for-automatic-failover"
pubDate: 2025-12-01
---

Article

•

02/01/2024

Applies to:

SQL Server

: Availability Group Automatic Failover Readiness

: Availability group is not ready for automatic failover.

:

: Availability group

This policy checks to verify that the availability group has at least one secondary replica that is

failover ready. The policy is in an unhealthy state and an alert is raised when the failover mode

of the primary replica is automatic, however none of the secondary replicas in the availability

group are failover ready.

The policy is in a healthy state when at least one secondary replica is automatic failover ready.

The availability group is not ready for

automatic failover

. The primary replica is configured for

automatic failover; however, the secondary replica is not ready for automatic failover. The

secondary replica that is configured for automatic failover might be unavailable or its

data

synchronization state is currently not SYNCHRONIZED

.

Following are possible solutions for this issue:

Verify that at least one secondary replica is configured as

automatic failover

. If there is not

a secondary replica configured as automatic failover, update the configuration of a

secondary replica to be the automatic failover target with synchronous commit.

Use the policy to verify that the data is in a synchronization state and the automatic

failover target is SYNCHRONIZED, and then resolve the issue at the availability replica.

Description
