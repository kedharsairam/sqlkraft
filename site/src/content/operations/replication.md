---
title: "Replication"
topic: "high-availability"
description: |
  Article

  •

  11/18/2022

  Applies to:

  SQL Server

  Database mirroring can be used in conjunction with replication to improve availability for the

  publication database. Database mirroring involves two c
tags:
  - "high-availability"
  - "replication"
pubDate: 2025-12-01
---

Article

•

11/18/2022

SQL Server

Database mirroring can be used in conjunction with replication to improve availability for the

publication database. Database mirroring involves two copies of a single database that typically

reside on different computers. At any given time, only one copy of the database is currently

available to clients. This copy is known as the principal database. Updates made by clients to

the principal database are applied on the other copy of the database, known as the mirror

database. Mirroring involves applying the transaction log from every insertion, update, or

deletion made on the principal database onto the mirror database.

Replication failover to a mirror is fully supported for publication databases, with limited

support for subscription databases. Database mirroring is not supported for the distribution

database. For information about recovering a distribution database or subscription database

without any need to reconfigure replication, see

Back Up and Restore Replicated Databases.

Be aware of the following requirements and considerations when using replication with

database mirroring:

The principal and mirror must share a Distributor. We recommend that this be a remote

Distributor, which provides greater fault tolerance if the Publisher has an unplanned

failover.

Replication supports mirroring the publication database for merge replication and for

transactional replication with read-only Subscribers or queued updating Subscribers.

Immediate updating Subscribers, Oracle Publishers, Publishers in a peer-to-peer

topology, and republishing are not supported.

７

Note

After a failover, the mirror becomes the principal. In this topic, "principal" and "mirror"

always refer to the original principal and mirror.
