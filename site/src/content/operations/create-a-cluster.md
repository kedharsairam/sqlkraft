---
title: "Create a cluster"
topic: "high-availability"
description: |
  Article
  
  •
  
  09/28/2023
  
  Applies to:
  
  SQL Server
  
  To install or upgrade a SQL Server failover cluster instance (FCI), you must run the Setup
  
  program on each node of the underlying Windows Server failo
tags:
  - "high-availability"
  - "create-a-cluster"
pubDate: 2025-12-01
---

Article

•

09/28/2023

Applies to:

SQL Server

To install or upgrade a SQL Server failover cluster instance (FCI), you must run the Setup

program on each node of the underlying Windows Server failover cluster. To add a node to an

existing SQL Server failover cluster instance, you must run SQL Server Setup on the node that is

to be added to the SQL Server failover cluster instance. Do not run Setup on the active node to

manage the other nodes.

Depending on how the nodes are clustered, the SQL Server failover cluster instance is

configured in the following ways:

Nodes on the same subnet or the same set of subnets - The IP address resource

dependency is set to AND for these types of configurations.

Nodes on different subnets - The IP address resource dependency is set to OR and this

configuration is called a SQL Server multi-subnet failover cluster instance configuration.

For more information, see

SQL Server Multi-Subnet Clustering (SQL Server)

.

The following options are available for SQL Server failover cluster installation:

SQL Server integrated failover cluster installation consists of the following steps:

Create and configure a single-node SQL Server failover cluster instance. When you

configure the node successfully, you have a fully functional failover cluster instance. At

this point, it does not have high availability because there is only one node in the failover

cluster instance.

On each node to be added to the SQL Server failover cluster instance, run Setup with Add

Node functionality to add that node.

If the node you are adding has additional or different subnets, Setup allows you to

specify additional IP addresses. If the node you are adding is on a different subnet, you

also need to confirm the IP address resource dependency change to OR. For more

information on the different possible scenarios during Add Node operations, see

Add

or Remove Nodes in an Always On Failover Cluster Instance (Setup)

.

SQL Server Advanced/Enterprise failover cluster installation consists of the following steps: