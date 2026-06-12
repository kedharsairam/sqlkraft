---
title: "Secondary database is not joined"
topic: "high-availability"
description: ": Availability Database Join State : Secondary database is not joined."
tags: ["high-availability","secondary-database-is-not-joined"]
pubDate: "2025-12-01"
---

: Availability Database Join State

: Secondary database is not joined.

:

Warning

: Availability database

This policy checks the join state of the secondary database (also known as a "secondary

database replica"). The policy is in an unhealthy state when the dataset replica is not joined.

The policy is otherwise in a healthy state.

This secondary database is not joined to the availability group. The configuration of this

secondary database is incomplete.

Use Transact-SQL, PowerShell, or SQL Server Management Studio to join the secondary replica

to the availability group. For more information about joining secondary replicas to availability

groups, see

Joining a Secondary Replica to an Availability Group (SQL Server).

Overview of Always On Availability Groups (SQL Server)

Use the Always On Dashboard (SQL Server Management Studio)

Description
