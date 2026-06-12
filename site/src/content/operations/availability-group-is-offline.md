---
title: "Availability group is offline"
topic: "high-availability"
description: ": Availability Group Online State : Availability group is offline."
tags: ["high-availability","availability-group-is-offline"]
pubDate: "2025-12-01"
---

: Availability Group Online State

: Availability group is offline.

:

: Availability group

This policy checks the online or offline state of the availability group. The policy is in an

unhealthy state and an alert is raised when the cluster resource of the availability group is

offline or the availability group does not have a primary replica.

The policy state is healthy when the cluster resource of the availability group is online and the

availability group has a primary replica.

This issue can be caused by a failure in the server instance that hosts the primary replica or by

the Windows Server Failover Cluster (WSFC) availability group resource going offline. Following

are possible causes for the availability group to be offline:

The availability group is not configured with automatic failover mode. The primary replica

becomes unavailable and the role of all replicas in the availability group become

RESOLVING.

The primary replica instance service is down or unresponsive.

The availability group has a connectivity issue with the cluster.

The availability group is configured with automatic failover mode and does not complete

successfully.

During the automatic failover, the primary readiness check on the target replica fails,

and there is no replica available to become the new primary.

The availability group resource in the cluster becomes offline.

Description
