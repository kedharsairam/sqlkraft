---
title: "Configure Distribution in AG"
topic: "migration"
description: |
  Article
  
  •
  
  12/17/2024
  
  Applies to:
  
  SQL Server
  
  This article explains how to set up a SQL Server replication distribution database in an Always
  
  On availability group (AG).
  
  SQL Server 2017 CU6 and S
tags:
  - "migration"
  - "configure-distribution-in-ag"
pubDate: 2025-12-01
---

Article

•

12/17/2024

Applies to:

SQL Server

This article explains how to set up a SQL Server replication distribution database in an Always

On availability group (AG).

SQL Server 2017 CU6 and SQL Server 2016 SP2-CU3 introduces support for replication

distribution database in an AG through the following mechanisms:

The distribution database AG needs to have a listener. When the publisher adds the

distributor, it uses the listener name as the distributor name.

The replication jobs are created with the listener name as the distributor name.

Replication snapshot, log reader and distribution agent (push subscription) jobs created

on the distribution server gets created on all secondary replicas of the AG for Distribution

DB.

A new job monitors the state (primary or secondary in AG) of the distribution databases

and disables or enables the replication jobs based on the distribution databases state.

After a distribution database in the AG is configured based on the steps described below,

replication configuration and run time jobs can run properly before and after distribution

database AG failover.

Configuring distribution database to be included in an AG.

Configuring replication such as publications and subscriptions before and after AG

failover.

Replication jobs functional before and after failover.

Removing replication at distributor and publisher when distribution database is in AG.

Adding or removing nodes to existing distribution database AG.

A distributor may have multiple distribution databases. Each distribution database can be

in its own AG and can be not in any AG. Multiple distribution databases can share an AG.

７

Note

Distribution agent jobs for pull subscriptions are created on the subscriber server and not

on the distribution server.