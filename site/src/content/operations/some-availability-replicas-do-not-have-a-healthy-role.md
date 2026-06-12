---
title: "Some availability replicas do not have a healthy role"
topic: "high-availability"
description: ": Availability Replicas Role State : Some availability replicas do not have a healthy role."
tags: ["high-availability","some-availability-replicas-do-not-have-a-healthy-role"]
pubDate: "2025-12-01"
---

: Availability Replicas Role State

: Some availability replicas do not have a healthy role.

:

Warning

: Availability group

This policy rolls up the connection state of all availability replicas and checks if there are any

availability replicas that are not in a healthy role. The policy is in an unhealthy state when any

availability replica is neither primary nor secondary. The policy is otherwise in a healthy state.

In this availability group, at least one availability replica does not currently have the primary or

secondary role.

Use the availability replica policy state to find the availability replica whose role is not primary

or secondary, and then resolve the issue at the availability replica.

Overview of Always On Availability Groups (SQL Server)

Use the Always On Dashboard (SQL Server Management Studio)

Description
