---
title: "Troubleshoot: Availability group exceeded RPO"
topic: "high-availability"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  After you perform a forced manual failover on an availability group to an asynchronous-

  commit secondary replica, you may find that data loss is more
tags:
  - "high-availability"
  - "troubleshoot-availability-group-exceeded-rpo"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

After you perform a forced manual failover on an availability group to an asynchronous-

commit secondary replica, you may find that data loss is more than your recovery point

objective (RPO). Or, when you calculate the potential data loss of an asynchronous-commit

secondary replica using the method in

Monitor Performance for Always On Availability Groups

,

you find that it exceeds your RPO.

A synchronous-commit secondary replica guarantees zero data loss, but the potential data loss

of an asynchronous-commit secondary replica depends on how much log is still waiting to be

hardened on the secondary replica.

The following sections describe the common causes for high potential data loss of an

asynchronous-commit secondary replica, assuming that you do not have a systemic

performance issue in your server instance that is unrelated to availability groups.

1.

High network latency or low network throughput causes log build-up on the primary

replica

2.

Disk I/O bottleneck slows down log hardening on the secondary replica

The most common reason for the databases exceeding their RPO is that they cannot be sent to

the secondary replica fast enough.

The primary replica activates flow control on the log send when it has exceeded the maximum

allowable number of unacknowledged messages sent over to the secondary replica. Until some

of these messages have been acknowledged, no more log blocks can be sent to the secondary

replica. Since data loss can be prevented only when they have been hardened on the

secondary replica, the build-up of unsent log messages increases potential data loss.
