---
title: "Always On Dashboard"
topic: "high-availability"
description: |
  Article

  •

  02/26/2024

  Applies to:

  SQL Server

  Database administrators use the Always On Availability Group dashboard to obtain an at-a-

  glance view the health of an availability group and its avai
tags:
  - "high-availability"
  - "always-on-dashboard"
pubDate: 2025-12-01
---

Article

•

02/26/2024

Applies to:

SQL Server

Database administrators use the Always On Availability Group dashboard to obtain an at-a-

glance view the health of an availability group and its availability replicas and databases in SQL

Server. Some of the typical uses for the availability group dashboard are:

Choosing a replica for a manual failover.

Estimating data loss if you force failover.

Evaluating data-synchronization performance.

Evaluating the performance impact of a synchronous-commit secondary replica

The dashboard provides key availability group states and performance indicators allowing

you to easily make high availability operational decisions using the following types of

information.

Replica roll-up state

Synchronization mode and state

Estimate Data Loss

Estimated Recovery Time (redo catch up)

Database Replica details

Synchronization mode and state

Time to restore log

You must be connected to the instance of SQL Server (server instance) that hosts either the

primary replica or a secondary replica of an availability group.

Requires CONNECT, VIEW SERVER STATE, and VIEW ANY DEFINITION permissions.

1. In Object Explorer, connect to the instance of SQL Server on which you want to run the

Always On Dashboard.
