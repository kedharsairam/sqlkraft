---
title: "Prerequisites, restrictions, & recommendations"
topic: "high-availability"
description: |
  Prerequisites, restrictions, and
  
  Applies to:
  
  SQL Server
  
  This article describes considerations for deploying Always On availability groups, including
  
  prerequisites, restrictions, and recommendation
tags:
  - "high-availability"
  - "prerequisites-restrictions-recommendations"
pubDate: 2025-12-01
---

Prerequisites, restrictions, and

Applies to:

SQL Server

This article describes considerations for deploying Always On availability groups, including

prerequisites, restrictions, and recommendations for host computers, Windows Server failover

clusters (WSFC), server instances, and availability groups. For each of these components

security considerations and required permissions, if any, are indicated.

Depending on the SQL Server components and features you'll use with Always On availability

groups, you might need to install additional .NET hotfixes identified in the following table. You

can install the hotfixes in any order.

Reporting

Services

Hotfix for .NET 3.5 SP1 adds support to SQL Client for Always

On features of Read-intent, readonly, and

multisubnetfailover. The hotfix needs to be installed on each

Reporting Services report server.

KB 2654347:

Hotfix for

.NET 3.5 SP1 to add

support for Always On

features

To support the Always On availability groups feature, ensure that every computer that is to

participate in one or more availability groups meets the following fundamental requirements:

）

Important

Before you deploy Always On availability groups, we strongly recommend that you read

every section of this topic.

ﾉ

Expand table

ﾉ

Expand table