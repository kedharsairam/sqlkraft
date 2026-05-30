---
title: "Database snapshots"
topic: "high-availability"
description: |
  Applies to:

  SQL Server

  You can create a database snapshot on a primary or secondary database in an availability

  group. The replica role must be either

  or

  , and can't be in the

  state.

  You should
tags:
  - "high-availability"
  - "database-snapshots"
pubDate: 2025-12-01
---

Applies to:

SQL Server

You can create a database snapshot on a primary or secondary database in an availability

group. The replica role must be either

or

, and can't be in the

state.

You should create database snapshots when the database synchronization state is

or

. However, you can still create database snapshots when the

database synchronization state is

.

A database snapshot on a secondary replica continues to work if the replica is

from the primary replica.

Some Always On availability groups conditions cause both the source database and its

database snapshots to restart, temporarily disconnecting users. These conditions are as follows:

The primary replica changes roles. This change can happen because the current primary

replica goes offline and comes back online on the same server instance, or because the

availability group fails over.

The database enters the secondary role.

If the availability replica that hosts database snapshots fails over, the database snapshots

remain on the server instance where you created them. You can continue to use the snapshots

after the failover. If performance is a concern in your environment, create database snapshots

only on secondary databases hosted by a secondary replica that is configured for manual

failover mode.

If you ever manually fail over the availability group to this secondary replica, you can create a

new set of database snapshots on another secondary replica, redirect clients to the new

database snapshots, and drop all of the database snapshots from the now primary databases.

７

Note

Creating database snapshots on any database adds CPU and I/O overhead because of

copy-on-write activity. On database replicas, this overhead can reduce redo throughput

and affect other operations, especially as the number of snapshots increases.

```cmd
PRIMARY
SECONDARY
RESOLVING
SYNCHRONIZING
SYNCHRONIZED
```
