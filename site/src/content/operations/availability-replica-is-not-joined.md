---
title: "Availability replica is not joined"
topic: "high-availability"
description: ": Availability Replica Join State : Availability Replica is not joined."
tags: ["high-availability","availability-replica-is-not-joined"]
pubDate: 2025-12-01
---

: Availability Replica Join State

: Availability Replica is not joined.

:

Warning

: Availability replica

This policy checks the join state of the availability replica. The policy is in an unhealthy state

when the availability replica is added to the availability group, but is not joined properly. The

policy is otherwise in a healthy state.

The secondary replica is not joined to the availability group. For an availability replica to be

successfully joined to the availability group, the join state must be Joined Standalone Instance

(1) or Joined Failover Cluster (2).

Use Transact-SQL, PowerShell, or SQL Server Management Studio to join the secondary replica

to the availability group. For more information about joining secondary replicas to availability

groups, see

Joining a Secondary Replica to an Availability Group (SQL Server).

Overview of Always On Availability Groups (SQL Server)

Use the Always On Dashboard (SQL Server Management Studio)

Description
