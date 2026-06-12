---
title: "Configure (HA add-on)"
topic: "linux-operations"
description: "on Linux This guide provides instructions to create a two-node shared disk failover cluster for SQL Server on Red Hat Enterprise Linux. The clustering layer is based on Red"
tags: ["linux-operations","configure-ha-add-on"]
pubDate: 2025-12-01
---

on Linux

This guide provides instructions to create a two-node shared disk failover cluster for SQL

Server on Red Hat Enterprise Linux. The clustering layer is based on Red Hat Enterprise Linux

(RHEL)

HA add-on

built on top of

Pacemaker. The SQL Server instance is active on either

one node or the other.

As the following diagram shows, storage is presented to two servers. Clustering components -

Corosync and Pacemaker - coordinate communications and resource management. One of the

servers has the active connection to the storage resources and the SQL Server. When

Pacemaker detects a failure, the clustering components are responsible for moving the

resources to the other node.

For more information on cluster configuration, resource agents options, and management, visit

RHEL reference documentation.

At this point, SQL Server integration with Pacemaker isn't as coupled as with WSFC on

Windows. From within SQL Server, there's no knowledge about the presence of the cluster, all

orchestration is outside in and the service is controlled as a standalone instance by Pacemaker.

Also for example, cluster dmvs

and

will no records.

To use a connection string that points to a string server name and not use the IP, they will have

to register in their DNS server the IP used to create the virtual IP resource (as explained in the

７

Note

Access to Red Hat HA add-on and documentation requires a subscription.

```cmd
sys.dm_os_cluster_nodes sys.dm_os_cluster_properties
```
