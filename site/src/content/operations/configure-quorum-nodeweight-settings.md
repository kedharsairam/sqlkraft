---
title: "Configure Quorum NodeWeight Settings"
topic: "high-availability"
description: |
  Article
  
  •
  
  03/03/2023
  
  Applies to:
  
  SQL Server
  
  This topic describes how to configure NodeWeight settings for a member node in a Windows
  
  Server Failover Clustering (WSFC) cluster. NodeWeight setting
tags:
  - "high-availability"
  - "configure-quorum-nodeweight-settings"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

This topic describes how to configure NodeWeight settings for a member node in a Windows

Server Failover Clustering (WSFC) cluster. NodeWeight settings are used during quorum voting

to support disaster recovery and multi-subnet scenarios for Always On availability groups and

SQL Server Failover Cluster Instances.

,

Security

Using Powershell

,

Using Cluster.exe

This feature is supported only in Windows Server 2008 or later versions.

The user must be a domain account that is member of the local Administrators group on each

node of the WSFC cluster.

）

Important

In order to use NodeWeight settings, the following hotfix must be applied to all servers in

the WSFC cluster:

: A hotfix is available to let you configure a cluster node that does not have

quorum votes in Windows Server 2008 and in Windows Server 2008 R2



Tip

If this hotfix is not installed, the examples in this topic will return empty or NULL values for

NodeWeight.