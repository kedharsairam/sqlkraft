---
name: "sys.dm_hadr_cluster_members"
title: "sys.dm_hadr_cluster_members"
category: "availability"
description: "If the Windows Server failover cluster (WSFC) node hosts a local instance of SQL Server that is enabled for Always On availability groups and has WSFC quorum, the view returns a row for each member that constitutes the quorum, and the state of that member. This set includes all nodes in the cluster (returned with the disk or file-share witness, if any."
tags: ["availability", "dmv"]
pubDate: 2026-05-29
syntax: "sys.dm_hadr_cluster_members"
---

## Description

If the Windows Server failover cluster (WSFC) node hosts a local instance of SQL Server that is enabled for Always On availability groups and has WSFC quorum, the view returns a row for each member that constitutes the quorum, and the state of that member. This set includes all nodes in the cluster (returned with the disk or file-share witness, if any. The row returned for a given member contains information

## Syntax

`sys.dm_hadr_cluster_members`
