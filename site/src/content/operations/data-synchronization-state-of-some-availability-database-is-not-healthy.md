---
title: "Data synchronization state of some availability database is not healthy"
topic: "high-availability"
description: ": Availability Replica Data Synchronization State : Data synchronization state of some availability database is not healthy. : Warning : Availabili"
tags: ["high-availability","data-synchronization-state-of-some-availability-database-is-not-healthy"]
pubDate: 2025-12-01
---

: Availability Replica Data Synchronization State

: Data synchronization state of some availability database is not healthy.

:

Warning

: Availability replica

This policy checks the data synchronization state of the availability database (also known as a

"database replica"). The policy is in an unhealthy state when the data synchronization state is

NOT SYNCHRONIZING or the state is not SYNCHRONIZED for the synchronous-commit

database replica.

At least one availability database on the replica has an unhealthy data synchronization state. If

this is an asynchronous-commit availability replica, all availability databases should be in the

SYNCHRONIZING state. If this is a synchronous-commit availability replica, all availability

databases should be in the SYNCHRONIZED state. This issue can be caused by the following:

The availability replica might be disconnected.

The data movement might be suspended.

The database might not be accessible.

There might be a temporary delay issue due to network latency or the load on the

primary or secondary replica.

Resolve any connection or data movement suspend issues. Check the events for this issue

using SQL Server Management Studio, and find the database error. Follow the troubleshooting

Description
