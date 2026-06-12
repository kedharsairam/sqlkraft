---
title: "Peer-to-peer replicated databases"
topic: "upgrade"
description: "on Windows This article provides guidance on how to upgrade or patch SQL Server instances that participate in peer-to-peer (P2P) replication , both outside of an Always On"
tags: ["upgrade","peer-to-peer-replicated-databases"]
pubDate: 2025-12-01
---

on Windows

This article provides guidance on how to upgrade or patch SQL Server instances that

participate in

peer-to-peer (P2P) replication

, both outside of an Always On availability group

and for databases that are within an Always On availability group.

If your replication topology includes other types of replication, such as snapshot, merge or

transactional replication, see

Upgrade or patch replicated databases

for more information.

The steps in this section provide guidance on how to upgrade or patch SQL Server instances

that are participating in peer-to-peer (P2P) replication outside of an Always On availability

group.

The following table describes the roles and names of the servers that participate in the

replication topology used in the example:

The SQL Server instance that hosts the replication databases for the first peer in the peer-to-peer

topology.

The SQL Server instance that hosts the replication databases for the second peer in the peer-to-

peer topology.

The remote distributor for Peer1.

The remote distributor for Peer2.

When patching or upgrading peer-to-peer replicated databases outside of an availability

group, follow these steps:

1. Stop incoming traffic to

by stopping all applications and distribution agents from

any other peers that replicate to this instance. For example, stop the distribution agent on.

ﾉ

Expand table
