---
title: "Create clustered DTC"
topic: "high-availability"
description: |
  Article

  •

  11/25/2024

  Applies to:

  SQL Server

  - Windows only

  This article walks you through a complete configuration of a clustered DTC resource for a SQL

  Server Always On availability group (AG)
tags:
  - "high-availability"
  - "create-clustered-dtc"
pubDate: 2025-12-01
---

Article

•

11/25/2024

Applies to:

SQL Server

- Windows only

This article walks you through a complete configuration of a clustered DTC resource for a SQL

Server Always On availability group (AG). The complete configuration can take up to an hour to

complete.

The walkthrough creates a clustered DTC resource and the SQL Server AGs to align with the

requirements at

How to cluster the DTC service for an Always On availability group

.

The walkthrough uses PowerShell and Transact-SQL (T-SQL) scripts. Many of the T-SQL scripts

require

SQLCMD Mode

to be enabled. For more information on

SQLCMD Mode

, see

Edit

SQLCMD Scripts with Query Editor

. The PowerShell module

must be

imported. For more information about importing a PowerShell module, see

Importing a

PowerShell Module

. This walkthrough is based on the following configuration options:

All requirements from

Prerequisites, restrictions, and recommendations for Always On

availability groups

are met.

The domain is

.

The user has the Create Computer objects permission in the OU where the DTC Network

Name resource will be created.

The user is a domain user with administrator rights on all nodes in the cluster.

A file share called

has been created for backups.

The default instances of SQL Server are named

and

.

The same service account is used on all instances of SQL Server.

The user is a member of the fixed SQL Server role sysadmin on all instances of SQL Server.

The default outcome of transactions that DTC can't resolve will be set to

.

The mirroring endpoint will use port

.

No other AGs or clustered DTC resources exist.

Cluster details (Existing):

Name:

Network Name:

Nodes:

Shared storage:

(Owned by

)

Cluster details (To be created):

Network Name resource:

DTC Network Name resource:

```cmd
FailoverClusters contoso.lab sqlbackups
SQLNODE1
SQLNODE2
```
