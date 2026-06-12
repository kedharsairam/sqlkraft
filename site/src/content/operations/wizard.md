---
title: "Wizard"
topic: "high-availability"
description: "This topic describes how to use the in SQL Server Management Studio to create and configure an Always On availability group in SQL Server. An availa"
tags: ["high-availability","wizard"]
pubDate: 2025-12-01
---

This topic describes how to use the

in SQL Server Management

Studio to create and configure an Always On availability group in SQL Server. An

availability

group

defines a set of user databases that will fail over as a single unit and a set of failover

partners, known as

availability replicas

, that support failover.

We strongly recommend that you read this section before attempting to create your first

availability group.

In most cases, you can use the New Availability Group Wizard to complete all of the tasks

require to create and configure an availability group. However, you might need to complete

some of the tasks manually.

If you are using a Windows Server Failover Cluster (WSFC) cluster type to host availability

group, verify that the instances of SQL Server that host the availability replicas reside on

different cluster servers (or nodes) within the same WSFC. Also, verify that each of the

server instances meets all other Always On availability groups prerequisites. For more

information, we strongly recommend that you read

Prerequisites, Restrictions, and

Recommendations for Always On Availability Groups (SQL Server).

If a server instance that you select to host an availability replica is running under a

domain user account and does not yet have a database mirroring endpoint, the wizard

can create the endpoint and grant CONNECT permission to the server instance service

account. However, if the SQL Server service is running as a built-in account, such as Local

System, Local Service, or Network Service, or a nondomain account, you must use

certificates for endpoint authentication, and the wizard will be unable to create a

７

Note

For an introduction to availability groups, see.

Prerequisites, Restrictions, and Recommendations
