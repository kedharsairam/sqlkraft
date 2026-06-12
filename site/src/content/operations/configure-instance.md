---
title: "Configure instance"
topic: "high-availability"
description: "This article contains information about the requirements for configuring an instance of SQL Server to support Always On availability groups in SQL Ser"
tags: ["high-availability","configure-instance"]
pubDate: 2025-12-01
---

This article contains information about the requirements for configuring an instance of SQL

Server to support Always On availability groups in SQL Server.

Always On Availability Groups

A high-availability and disaster-recovery solution that provides an enterprise-level replacement

for database mirroring. An

availability group

supports a failover environment for a discrete set

of user databases, known as

availability databases

, that fail over together.

An instantiation of an availability group hosted by a specific instance of SQL

Server and that maintains a local copy of each availability database that belongs to the

availability group. Two availability replicas exist: a single

primary replica

and one to four

secondary replicas. The server instances that host the availability replicas for a given availability

group must reside on different nodes of a single Windows Server Failover Clustering (WSFC)

cluster.

database mirroring endpoint

An endpoint is a SQL Server object that enables SQL Server to communicate over the network.

To participate in database mirroring and/or Always On availability groups a server instance

requires a unique, dedicated endpoint. All mirroring and availability group connections on a

server instance use the same database mirroring endpoint. This special-purpose endpoint is

used exclusively to receive these connections from other server instances.

）

Important

For essential information about Always On availability groups prerequisites and

restrictions for Windows Server Failover Clustering (WSFC) nodes and instances of SQL

Server, see

Prerequisites, Restrictions, and Recommendations for Always On Availability.
