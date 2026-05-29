---
title: "Distributed availability groups"
topic: "high-availability"
description: |
  Article
  
  •
  
  05/19/2025
  
  Applies to:
  
  SQL Server
  
  A distributed availability group (AG) is a special type of availability group that spans two
  
  separate availability groups. Distributed availability gr
tags:
  - "high-availability"
  - "distributed-availability-groups"
pubDate: 2025-12-01
---

Article

•

05/19/2025

Applies to:

SQL Server

A distributed availability group (AG) is a special type of availability group that spans two

separate availability groups. Distributed availability groups are available starting with SQL

Server 2016.

This article describes the distributed availability group feature. To configure a distributed

availability group, see

Configure distributed availability groups

.

A distributed availability group is a special type of availability group that spans two separate

availability groups. The availability groups that participate in a distributed availability group

don't need to be in the same location. They can be physical, virtual, on-premises, in the public

cloud, or anywhere that supports an availability group deployment. This includes cross-domain

and even cross-platform - such as between an availability group hosted on Linux and one

hosted on Windows. As long as two availability groups can communicate, you can configure a

distributed availability group with them.

A traditional availability group has resources configured in a Windows Server Failover Cluster

(WSFC) or if on Linux, Pacemaker. A distributed availability group doesn't configure anything in

the underlying cluster (WSFC or Pacemaker). Everything about it is maintained within SQL

Server. To learn how to view information for a distributed availability group, see

Viewing

distributed availability group information

.

A distributed availability group requires that the underlying availability groups have a listener.

Rather than provide the underlying server name for a standalone instance (or in the case of a

SQL Server failover cluster instance [FCI], the value associated with the network name resource)

as you would with a traditional availability group, you specify the configured listener for the

distributed availability group with the parameter ENDPOINT_URL when you create it. Although

each underlying availability group of the distributed availability group has a listener, a

distributed availability group has no listener.

The following figure shows a high-level view of a distributed availability group that spans two

availability groups (AG 1 and AG 2), each configured on its own WSFC. The distributed

availability group has a total of four replicas, with two in each availability group. Each

availability group can support up to the maximum number of replicas, so a distributed

availability group can have up to 18 total replicas.