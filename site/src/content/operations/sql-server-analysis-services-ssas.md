---
title: "SQL Server Analysis Services (SSAS)"
topic: "high-availability"
description: "- Windows only An Always On availability group is a predefined collection of SQL Server relational databases that failover together when conditions t"
tags: ["high-availability","sql-server-analysis-services-ssas"]
pubDate: "2025-12-01"
---

- Windows only

An Always On availability group is a predefined collection of SQL Server relational databases

that failover together when conditions trigger a failover in any one database, redirecting

requests to a mirrored database on another instance in the same availability group. If you are

using availability groups as your high availability solution, you can use a database in that group

as a data source in an Analysis Services tabular or multidimensional solution. All of the

following Analysis Services operations work as expected when using an availability database:

processing or importing data, querying relational data directly (using ROLAP storage or

DirectQuery mode), and writeback.

Processing and querying are read-only workloads. You can improve performance by offloading

these workloads to a readable secondary replica. Additional configuration is required for this

scenario. Use the checklist in this topic to ensure you follow all the steps.

You must have a SQL Server login on all replicas. You must be a

to configure

availability groups, listeners, and databases, but users only need

permissions to

access the database from an Analysis Services client.

Use a data provider that supports the tabular data stream (TDS) protocol version 7.4 or newer,

such as the SQL Server Native Client 11.0 or the Data Provider for SQL Server in.NET

Framework 4.02. The secondary replica role must be configured for read-only

connections, the availability group must have a routing list, and the connection in the Analysis

Services data source must specify the availability group listener. Instructions are provided in

this topic.

Unless your Analysis Services solution includes writeback, you can configure a data source

connection to use a readable secondary replica. If you have a fast network connection, the

secondary replica has very low data latency, providing nearly identical data as the primary
