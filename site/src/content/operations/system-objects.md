---
title: "System Objects"
topic: "high-availability"
description: "10/21/2025 - Windows only This article serves as a reference page to all the various system objects that can be used when working with availability groups (AGs). Descripti"
tags: ["high-availability","system-objects"]
pubDate: 2025-12-01
---

- Windows only

This article serves as a reference page to all the various system objects that can be used when

working with availability groups (AGs).

Description

sys.availability_databases_cluster

Contains one row for each availability database on the

instance of SQL Server hosting an availability replica for any

availability group (AG) in the Windows Server Failover

Clustering (WSFC) cluster, regardless of whether the local

copy database has been joined to the AG yet.

sys.availability_group_listener_ip_addresses

Returns a row for every IP address that is associated with

any AG listener in the Windows Server Failover Clustering

(WSFC) cluster.

sys.availability_group_listeners

For each AG, returns either zero rows indicating that no

network name is associated with the AG, or returns a row for

each availability-group listener configuration in the

Windows Server Failover Clustering (WSFC) cluster.

sys.availability_groups

Returns a row for each AG for which the local instance of

hosts an availability replica. Each row contains a

cached copy of the AG metadata.

sys.availability_groups_cluster

Returns a row for each AG in the Windows Server Failover

Clustering (WSFC). Each row contains the AG metadata from

the WSFC cluster.

sys.availability_read_only_routing_lists

Returns a row for the read only routing list of each

availability replica in an AG in the WSFC failover cluster.

sys.availability_replicas

Returns a row for each of the availability replicas that

belong to any AG in the WSFC failover cluster.

ﾉ

Expand table
