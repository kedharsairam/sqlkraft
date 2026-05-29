---
title: "Database Mirroring Monitor Overview"
topic: "high-availability"
description: |
  Article
  
  •
  
  11/18/2022
  
  Applies to:
  
  SQL Server
  
  If you have the correct permissions, you can use Database Mirroring Monitor to monitor any
  
  subset of the mirrored databases on a server instance. Moni
tags:
  - "high-availability"
  - "database-mirroring-monitor-overview"
pubDate: 2025-12-01
---

Article

•

11/18/2022

Applies to:

SQL Server

If you have the correct permissions, you can use Database Mirroring Monitor to monitor any

subset of the mirrored databases on a server instance. Monitoring enables you to verify

whether and how well data is flowing in the database mirroring session. Database Mirroring

Monitor is also useful for troubleshooting the cause of reduced data flow.

You can register any of your mirrored databases for monitoring on each of the failover partners

individually. When you register a database, Database Mirroring Monitor caches the following

information about the database:

Database name

The names of the two partner server instances

The last known roles of each partner (principal or mirror)

To monitor database mirroring, you must be a member of either the

fixed server role

or the

fixed database role in the

database on the server instance. If you

are a member of

or

on only one of the partner server instances, the

monitor can connect only to that partner; the monitor cannot retrieve information from the

other partner.

If you are a member of just

on a server instance, you will have limited

permissions on that server instance. You will only be able to view the most recent status row. If

you connect to a server instance using

permissions, Database Mirroring Monitor

informs you that you have limited permissions.

）

Important

The

fixed database role is created in the

database when the first

database is registered in Database Mirroring Monitor. The new

role has no

members until a system administrator assigns users to the role.