---
title: "With Microsoft Entra authentication"
topic: "migration"
description: |
  Applies to:
  
  SQL Server 2022 (16.x)
  
  This article provides steps to configure Transactional and Snapshot replication by using
  
  authentication with Microsoft Entra ID (
  
  formerly Azure Active Directory
tags:
  - "migration"
  - "with-microsoft-entra-authentication"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2022 (16.x)

This article provides steps to configure Transactional and Snapshot replication by using

authentication with Microsoft Entra ID (

formerly Azure Active Directory

) for

SQL Server enabled

by Azure Arc

.

Microsoft Entra authentication support for replication was introduced in SQL Server 2022 (16.x)

Cumulative Update (CU) 6, and made generally available in CU 12. When you use Microsoft

Entra authentication for replication, the only different step is the first step. Specifically, create a

Microsoft Entra login, and grant sysadmin permissions.

After that, use the Microsoft Entra login in the replication stored procedures to configure

Transactional or Snapshot replication as you normally would.

To configure replication with Microsoft Entra authentication, you must meet the following

prerequisites:

Have SQL Server 2022

enabled by Azure-Arc

starting with

Cumulative Update 6

.

Configured Microsoft Entra authentication for every server in the replication topology.

Review

Tutorial: Set up Microsoft Entra authentication for SQL Server with app

registration

to learn more.

A supported version of

SQL Server Management Studio (SSMS)

.

The user connecting to the publisher and subscriber is a member of the

fixed

server role.

The connection must be encrypted using a certificate from a trusted Certificate Authority

(CA) or a self-signed certificate.

７

Note

Starting with SQL Server 2022 CU 6, disable Microsoft Entra authentication for replication

by using session trace flag 11561.