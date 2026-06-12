---
title: "Availability database is suspended"
topic: "high-availability"
description: "08/29/2025 : Availability Database Suspension State : Availability database is suspended. : Warning : Availability database This policy checks the state of data movement"
tags: ["high-availability","availability-database-is-suspended"]
pubDate: "2025-12-01"
---

: Availability Database Suspension State

: Availability database is suspended.

:

Warning

: Availability database

This policy checks the state of data movement of the secondary database (also known as a

"secondary database replica"). The policy is in an unhealthy state when the data movement is

suspended. The policy is otherwise in a healthy state.

Data synchronization on this availability database might have been suspended because of the

following:

Due to an error, the system might have suspended data synchronization.

The database administrator might have suspended data synchronization for maintenance

purposes.

Resume data synchronization by right-clicking the availability group and selecting. If the issue persists, check the availability group in the Event log, and then

diagnose why the system suspended data movement.

Description
