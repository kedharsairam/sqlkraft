---
title: "Domain-independent availability groups"
topic: "high-availability"
description: |
  Article

  •

  04/26/2024

  Applies to:

  SQL Server

  Always On availability groups (AGs) require an underlying Windows Server Failover Cluster

  (WSFC). Deploying a WSFC through Windows Server 2012 R2 requ
tags:
  - "high-availability"
  - "domain-independent-availability-groups"
pubDate: 2025-12-01
---

Article

•

04/26/2024

Applies to:

SQL Server

Always On availability groups (AGs) require an underlying Windows Server Failover Cluster

(WSFC). Deploying a WSFC through Windows Server 2012 R2 required that the servers

participating in a WSFC, also known as nodes, were joined to the same domain. For more

information on Active Directory Domain Services (AD DS), see

here

.

The dependency on AD DS and WSFC is more complex than previously deployed with a

database mirroring (DBM) configuration, since DBM can be deployed across multiple data

centers using certificates, without any such dependencies. A traditional availability group

spanning more than one data center requires that all servers must be joined to the same Active

Directory domain. Different domains, even trusted domains, don't work. All the servers must be

nodes of the same WSFC. The following figure shows this configuration. SQL Server 2016 (13.x)

and later versions also have distributed AGs, which achieve this goal in a different way.

Windows Server 2012 R2 introduced an

Active Directory-detached cluster

, a specialized form of

a Windows Server failover cluster, which can be used with availability groups. This type of

WSFC still requires the nodes to be domain-joined to the same Active Directory domain, but in
