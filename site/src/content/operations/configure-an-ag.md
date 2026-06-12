---
title: "Configure an AG"
topic: "linux-operations"
description: "on Linux This article describes how to create a SQL Server Always On availability group (AG) for high availability on Linux. There are two configuration types for AGs."
tags: ["linux-operations","configure-an-ag"]
pubDate: 2025-12-01
---

on Linux

This article describes how to create a SQL Server Always On availability group (AG) for high

availability on Linux. There are two configuration types for AGs. A

high availability

configuration uses a cluster manager to provide business continuity. This configuration can

also include read-scale replicas. This article explains how to create the AG for high availability.

You can also create an AG without a cluster manager for

read-scale. The AG for read scale only

provides read-only replicas for performance scale-out. It doesn't provide high availability. To

create an AG for read-scale, see

Configure a SQL Server availability group for read-scale on

Linux.

Configurations that guarantee high availability and data protection require either two or three

synchronous commit replicas. With three synchronous replicas, the AG can automatically

recover even if one server isn't available. For more information, see

High availability and data

protection for availability group configurations.

All servers must be either physical or virtual, and virtual servers must be on the same

virtualization platform. This requirement exists because the fencing agents are platform

specific. See

Policies for Guest Clusters.

The steps to create an AG on Linux servers for high availability differ from the steps on a

Windows Server failover cluster. The following list describes the high-level steps:

1.

Installation guidance for SQL Server on Linux.

2. Create the AG. This step is covered in this current article.

3. Configure a cluster resource manager, like Pacemaker.

）

Important

All three servers in the AG need to be on the same platform - physical or virtual -

because Linux high availability uses fencing agents to isolate resources on servers.

The fencing agents are specific for each platform.
