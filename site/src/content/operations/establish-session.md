---
title: "Establish session"
topic: "high-availability"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  After the mirror database is prepared (see

  Prepare a Mirror Database for Mirroring (SQL

  Server)

  ), you can establish a database mirroring session. T
tags:
  - "high-availability"
  - "establish-session"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

After the mirror database is prepared (see

Prepare a Mirror Database for Mirroring (SQL

Server)

), you can establish a database mirroring session. The principal, mirror, and witness

server instances must be separate server instances, which should be on separate host systems.

1. Create the mirror database. For more information, see

Prepare a Mirror Database for

Mirroring (SQL Server)

.

2. Set up security on each server instance.

Each server instance in a database mirroring session requires a database mirroring

endpoint. If the endpoint does not exist, you must create it.

７

Note

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use Always On availability groups instead.

）

Important

We recommend that you configure database mirroring during off-peak hours because

configuring mirroring can impact performance.

７

Note

A given server instance can participate in multiple concurrent database mirroring sessions

with the same or different partners. A server instance can be a partner in some sessions

and a witness in other sessions. The mirror server instance must be running the same

edition of SQL Server as the principal server instance. Database mirroring is not available

in every edition of Microsoft SQL Server. For a list of features that are supported by the

editions of SQL Server, see

. Also,

we strongly recommend that they run on comparable systems that can handle identical

workloads.
