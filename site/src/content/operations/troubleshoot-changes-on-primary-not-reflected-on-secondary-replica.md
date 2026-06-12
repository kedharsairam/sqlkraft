---
title: "Troubleshoot: Changes on primary not reflected on secondary replica"
topic: "high-availability"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  The client application completes an update on the primary replica successfully, but querying

  the secondary replica shows that the change is not reflec
tags:
  - "high-availability"
  - "troubleshoot-changes-on-primary-not-reflected-on-secondary-replica"
pubDate: 2025-12-01
---

Article

•

03/03/2023

SQL Server

The client application completes an update on the primary replica successfully, but querying

the secondary replica shows that the change is not reflected. This case assumes that your

availability has a healthy synchronization state. In most cases, this behavior resolves itself after

a few minutes.

If changes are still not reflected on the secondary replica after a few minutes, there may be a

bottleneck in the synchronization work flow. The location of the bottleneck depends on

whether the secondary replica is set to synchronous commit or asynchronous commit.

Each successful update on the primary replica has already been synchronized to the secondary

replica, or that the log records have already been flushed for hardening on the secondary

replica. Therefore, the bottleneck should be in the redo process that happens after the log is

flushed on the secondary replica.

However, once redo is caught up, all read workloads on the secondary replica are snapshot

isolation:

Long-running transactions on the primary replica

Redo on secondary replica

Since asynchronous commit acknowledges a transaction as soon as it is flushed to the local

disk, the bottleneck can be anywhere after that point:

Long-running transactions on the primary replica

Network latency or throughput

Log harden on the secondary replica

Redo on the secondary replica
