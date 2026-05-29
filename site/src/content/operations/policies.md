---
title: "Policies"
topic: "high-availability"
description: |
  Article
  
  •
  
  09/27/2023
  
  Applies to:
  
  SQL Server
  
  The Always On availability groups health model evaluates a set of predefined policy based
  
  management (PBM) policies. You can use these for viewing the
tags:
  - "high-availability"
  - "policies"
pubDate: 2025-12-01
---

Article

•

09/27/2023

Applies to:

SQL Server

The Always On availability groups health model evaluates a set of predefined policy based

management (PBM) policies. You can use these for viewing the health of an availability group

and its availability replicas and databases in SQL Server.

Always On predefined policies

A set of built-in policies that allow a database administrator to check an availability group and

its availability replicas and databases for compliance with the states that are defined by the

Always On policies.

Always On availability groups

A high-availability and disaster-recovery solution that provides an enterprise-level alternative

to database mirroring.

availability group

A container for a discrete set of user databases, known as

availability databases

, that fail over

together.

availability replica

An instantiation of an availability group that is hosted by a specific instance of SQL Server and

that maintains a local copy of each availability database that belongs to the availability group.

Two types of availability replicas exist: a single

primary replica

and one to four

secondary

replicas

. The server instances that host the availability replicas for a given availability group

must reside on different nodes of a single Windows Server Failover Clustering (WSFC) cluster.

availability database

A database that belongs to an availability group. For each availability database, the availability

group maintains a single read-write copy (the

primary database

) and one to four read-only

copies (

secondary databases

).

Always On Dashboard

A SQL Server Management Studio dashboard that provides an at-a-glance view of the health of

an availability group. For more information, see

Always On Dashboard

, later in this article.