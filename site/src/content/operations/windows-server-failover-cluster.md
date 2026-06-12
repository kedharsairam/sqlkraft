---
title: "Windows Server failover cluster"
topic: "high-availability"
description: ""
tags: ["high-availability","windows-server-failover-cluster"]
pubDate: "2025-12-01"
---

This article provides an overview of using a Windows Server Failover Cluster (WSFC) with SQL

Server for high availability and disaster recovery. A

Windows Server Failover Cluster

(WSFC) is a

group of independent servers that work together to increase the availability of applications and

services. SQL Server takes advantage of WSFC services and capabilities to support Always On

availability groups and SQL Server failover cluster instances.

Windows Server Failover Cluster (WSFC) A WSFC is a group of independent servers that work

together to increase the availability of applications and services.

Node

A server that is participating in a WSFC.

Cluster resource

A physical or logical entity that can be owned by a node, brought online and taken offline,

moved between nodes, and managed as a cluster object. A cluster resource can be owned by

only a single node at any point in time.

Role

A collection of cluster resources managed as a single cluster object to provide specific

functionality. For SQL Server, a role will be either an Always On availability group (AG) or

Always On failover cluster instance (FCI). A role contains all of the cluster resources that are

required for an AG or FCI. Failover and failback always act in context of roles. For an FCI, the

role contains an IP address resource, a network name resource, and the SQL Server resources.

An AG role contains the AG resource, and if a listener is configured, a network name and an IP

resource.

Network name resource

A logical server name that is managed as a cluster resource. A network name resource must be

used with an IP address resource. These entries might require objects in Active Directory

Domain Services and/or DNS.

Resource dependency

A resource on which another resource depends. If resource A depends on resource B, then B is

a dependency of A. Resource A won't be able to start without resource B.
