---
title: "Database Snapshots"
topic: "high-availability"
description: "You can take advantage of a mirror database that you are maintaining for availability purposes to offload reporting."
tags: ["high-availability","database-snapshots-2"]
pubDate: 2025-12-01
---

You can take advantage of a mirror database that you are maintaining for availability purposes

to offload reporting. To use a mirror database for reporting, you can create a database

snapshot on the mirror database and direct client connection requests to the most recent

snapshot. A database snapshot is a static, read-only, transaction-consistent snapshot of its

source database as it existed at the moment of the snapshot's creation. To create a database

snapshot on a mirror database, the database must be in the synchronized mirroring state.

Unlike the mirror database itself, a database snapshot is accessible to clients. As long as the

mirror server is communicating with the principal server, you can direct reporting clients to

connect to a snapshot. Note that because a database snapshot is static, new data is not

available. To make relatively recent data available to your users, you must create a new

database snapshot periodically and have applications direct incoming client connections to the

newest snapshot.

A new database snapshot is almost empty, but it grows over time as more and more database

pages are updated for the first time. Because every snapshot on a database grows

incrementally in this way, each database snapshot consumes as much resources as a normal

database. Depending on the configurations of the mirror server and principal server, having an

excessive number of database snapshots on a mirror database might decrease performance on

the principal database. Therefore, we recommend that you keep only a few relatively recent

snapshots on your mirror databases. Typically, after you create a replacement snapshot, you

should redirect incoming queries to the new snapshot and drop the earlier snapshot after any

current queries complete.

If role switching occurs, the database and its snapshots are restarted, temporarily

disconnecting users. Afterwards, the database snapshots remain on the server instance where

they were created, which has become the new principal database. Users can continue to use

the snapshots after the failover. However, this places an additional load on the new principal

server. If performance is a concern in your environment, we recommend that you create a

snapshot on the new mirror database when it becomes available, redirect clients to the new

snapshot, and drop all of the database snapshots from the former mirror database.

７

Note

For more information about database snapshots, see.
