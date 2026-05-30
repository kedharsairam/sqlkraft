---
title: "Log Shipping & Replication"
topic: "high-availability"
description: |
  Article

  •

  04/11/2023

  Applies to:

  SQL Server

  Log shipping involves two copies of a single database that typically reside on different

  computers. At any given time, only one copy of the database i
tags:
  - "high-availability"
  - "log-shipping-replication"
pubDate: 2025-12-01
---

Article

•

04/11/2023

Applies to:

SQL Server

Log shipping involves two copies of a single database that typically reside on different

computers. At any given time, only one copy of the database is currently available to clients.

This copy is known as the primary database. Updates made by clients to the primary database

are propagated by means of log shipping to the other copy of the database, known as the

secondary database. Log shipping involves applying the transaction log from every insertion,

update, or deletion made on the primary database onto the secondary database.

Log shipping can be used in conjunction with replication, with the following behavior:

Replication does not continue after a log shipping failover. If a failover occurs, replication

agents do not connect to the secondary, so transactions are not replicated to Subscribers.

If a failback to the primary occurs, replication resumes. All transactions that log shipping

copies from the secondary back to the primary are replicated to Subscribers.

If the primary is permanently lost, the secondary can be renamed so that replication can

continue. The remainder of this topic describes the requirements and procedures for

handling this case. The example given is the publication database, which is the most

common database to log ship, but a similar process can also be applied to subscription

and distribution databases.

For information about recovering databases involved in replication without any need to

reconfigure replication, see

Back Up and Restore Replicated Databases

.

Be aware of the following requirements and considerations:

If a primary contains more than one publication database, log ship all of the publication

databases to the same secondary.

７

Note

Use Always On availability groups, rather than log shipping, to provide availability for the

publication database. For more information, see

.
