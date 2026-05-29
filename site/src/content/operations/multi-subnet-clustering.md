---
title: "Multi-Subnet Clustering"
topic: "high-availability"
description: |
  SQL Server multi-subnet clustering
  
  08/26/2025
  
  Applies to:
  
  SQL Server
  
  A SQL Server multi-subnet failover cluster is a configuration in which each failover cluster node
  
  is connected to a different 
tags:
  - "high-availability"
  - "multi-subnet-clustering"
pubDate: 2025-12-01
---

SQL Server multi-subnet clustering

08/26/2025

Applies to:

SQL Server

A SQL Server multi-subnet failover cluster is a configuration in which each failover cluster node

is connected to a different subnet or a different set of subnets. These subnets can be in the

same location or in geographically dispersed sites. Clusters in geographically dispersed sites

are sometimes referred to as

stretch clusters

. Because there's no shared storage that all the

nodes can access, data should be replicated between the data storage on the multiple subnets.

When you replicate data, there's more than one copy of the data available. Therefore, a multi-

subnet failover cluster provides a disaster recovery solution in addition to high availability.

The following illustration represents a two-node, two-subnet failover cluster instance (FCI) in

SQL Server.

Following are some examples of SQL Server FCIs that use multiple subnets:

SQL Server multi-subnet failover cluster (two