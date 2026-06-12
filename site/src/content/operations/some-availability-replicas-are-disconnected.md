---
title: "Some availability replicas are disconnected"
topic: "high-availability"
description: ": Availability Replicas Connection State : Some availability replicas are disconnected."
tags: ["high-availability","some-availability-replicas-are-disconnected"]
pubDate: "2025-12-01"
---

: Availability Replicas Connection State

: Some availability replicas are disconnected.

:

Warning

: Availability group

This policy rolls up the connection state of all availability replicas and checks for any availability

replicas that are DISCONNECTED. The policy is in an unhealthy state when any availability

replica is DISCONNECTED. The policy is otherwise in a healthy state.

In this availability group, at least one secondary replica is not connected to the primary replica.

The connected state is DISCONNECTED.

Use the availability replica policy state to find the availability replica that is DISCONNECTED,

and then resolve the issue at the availability replica.

Overview of Always On Availability Groups (SQL Server)

Use the Always On Dashboard (SQL Server Management Studio)

Description
