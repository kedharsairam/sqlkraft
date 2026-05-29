---
title: "Dialog"
topic: "high-availability"
description: |
  Article
  
  •
  
  03/03/2023
  
  Applies to:
  
  SQL Server
  
  This topic contains information about how to use the
  
  dialog box of
  
  SQL Server Management Studio to create an Always On availability group on instance
tags:
  - "high-availability"
  - "dialog"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

This topic contains information about how to use the

dialog box of

SQL Server Management Studio to create an Always On availability group on instances of SQL

Server that are enabled for Always On availability groups. An

availability group

defines a set of

user databases that will fail over as a single unit and a set of failover partners, known as

availability replicas

, that support failover.

Before creating an availability group, verify that the instances of SQL Server that host

availability replicas reside on different Windows Server Failover Clustering (WSFC) node

within the same WSFC failover cluster. Also, verify that each of the server instance is

enabled for Always On availability groups and meets all other Always On availability

groups prerequisites. For more information, we strongly recommend that you read

Prerequisites, Restrictions, and Recommendations for Always On Availability Groups (SQL

Server)

.

Before you create an availability group, ensure that every server instance that will host an

availability replica has a fully functioning database mirroring endpoint. For more

information, see

The Database Mirroring Endpoint (SQL Server)

.

To use the

dialog box, you need to know the names of the server

instances that will host availability replicas. Also, you need know the names of any

databases that you intend to add to your new availability group, and you need to ensure

７

Note

For an introduction to availability groups, see

.

７

Note

For information about alternative ways to create an availability group, see

,

later in this topic.