---
title: "Subscribers"
topic: "high-availability"
description: |
  Applies to:

  SQL Server

  When an Always On availability group (AG) fails over, containing a database that is a replication

  subscriber, the replication subscription might fail. For transactional repli
tags:
  - "high-availability"
  - "subscribers"
pubDate: 2025-12-01
---

SQL Server

When an Always On availability group (AG) fails over, containing a database that is a replication

subscriber, the replication subscription might fail. For transactional replication push

subscribers, the distribution agent will continue to replicate automatically after a failover if the

subscription was created using the AG listener name. For transactional replication pull

subscribers, the distribution agent will continue to replicate automatically after a failover, if the

subscription was created using the AG listener name and the original subscriber server is up

and running. This is because the distribution agent jobs only get created on the original

subscriber (primary replica of the AG). For merge subscribers, a replication administrator must

manually reconfigure the subscriber, by recreating the subscription.

replication supports the automatic failover of the publisher and the automatic

failover of transactional subscribers. Merge subscribers can be part of an AG. However, manual

actions are required to configure the new subscriber after a failover. AGs can't be combined

with WebSync and SQL Server Compact scenarios.

For transactional replication, use the following steps to configure and fail over a subscriber AG:

1. Before creating the subscription, add the subscriber database to the appropriate AG.

2. Add the subscriber's AG listener as a linked server to all nodes of the AG. This step

ensures that all potential failover partners are aware of and can connect to the listener.

3. Using the script in the

Create a transactional replication push subscription

section, create

the subscription using the name of the AG listener of the subscriber. After a failover, the

listener name always remains valid, whereas the actual server name of the subscriber

depends on the actual node that became the new primary.

７

Note
