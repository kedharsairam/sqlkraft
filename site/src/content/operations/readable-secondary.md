---
title: "Readable secondary"
topic: "high-availability"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  The Always On availability groups active secondary capabilities include support for read-only

  access to one or more secondary replicas (

  readable sec
tags:
  - "high-availability"
  - "readable-secondary"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

The Always On availability groups active secondary capabilities include support for read-only

access to one or more secondary replicas (

readable secondary replicas

). A readable secondary

replica can be in either synchronous-commit availability mode, or asynchronous-commit

availability mode. A readable secondary replica allows read-only access to all its secondary

databases. However, readable secondary databases are not set to read-only. They are dynamic.

A given secondary database changes as changes on the corresponding primary database are

applied to the secondary database. For a typical secondary replica, the data, including durable

memory optimized tables, in the secondary databases is in near real time. Furthermore, full-text

indexes are synchronized with the secondary databases. In many circumstances, data latency

between a primary database and the corresponding secondary database is only a few seconds.

Security settings that occur in the primary databases are persisted to the secondary databases.

This includes users, database roles, and applications roles together with their respective

permissions and transparent data encryption (TDE), if enabled on the primary database.

Always On availability groups also supports the re-routing of read-intent connection requests

to a readable secondary replica (

read-only routing

). For information about read-only routing,

see

Using a Listener to Connect to a Read-Only Secondary Replica (Read-Only Routing)

.

Directing read-only connections to readable secondary replicas provides the following benefits:

Offloads your secondary read-only workloads from your primary replica, which conserves

its resources for your mission critical workloads. If you have mission critical read-workload

or the workload that cannot tolerate latency, you should run it on the primary.

Improves your return on investment for the systems that host readable secondary

replicas.

７

Note

Though you cannot write data to secondary databases, you can write to read-write

databases on the server instance that hosts the secondary replica, including user

databases and system databases such as

.
