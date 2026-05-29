---
title: "Contained availability groups"
topic: "high-availability"
description: |
  ﾃ
  
  Summarize this article for me
  
  Applies to:
  
  SQL Server 2022 (16.x)
  
  A contained availability group is an Always On availability group (AG) that supports:
  
  managing metadata objects (users, logins, 
tags:
  - "high-availability"
  - "contained-availability-groups"
pubDate: 2025-12-01
---

ﾃ

Summarize this article for me

Applies to:

SQL Server 2022 (16.x)

A contained availability group is an Always On availability group (AG) that supports:

managing metadata objects (users, logins, permissions, SQL Agent jobs, and so on) at the

AG level in addition to the instance level.

specialized contained system databases within the AG.

This article details the similarities, differences, and functionalities of contained AGs.

AGs generally consist of one or more user databases intended to operate as a coordinated

group, and which are replicated on some number of nodes in a cluster. When there's a failure

in the node, or in the health of SQL Server on the node that hosts the primary copy, the group

of databases moves as a unit to another replica node in the AG. All of the user databases stay

synchronized across all replicas of the AG, either in synchronous or asynchronous mode.

This architecture works well for applications that only interact with that set of user databases.

However, challenges arise when applications also rely on objects such as users, logins,

permissions, agent jobs, and other objects that are stored in one of the system databases

(

or

). To ensure that applications function smoothly and predictably, the admin

must

manually

ensure that any change to these objects is duplicated across all replica

instances in the AG. If you add a new instance to the AG, you can automatically or manually

seed the databases in a straightforward process. However, you must reconfigure all of the

system database customizations on the new instance to match the other replicas.

Contained AGs extend the concept of the group of databases being replicated to include

relevant portions of the

and

databases. Think of it as the execution context for

applications using the contained AG. The idea is that the contained AG environment includes

settings that affect the application relying on them. As such, the contained AG environment

concerns all databases the application interacts with, the authentication it uses (logins, users,

permissions), any scheduled jobs that it expects to be running, and other configuration settings

that impact the application.

This concept differs from contained databases, which use a different mechanism for the user

accounts, by storing the user information within the database itself. Contained databases only

```cmd
master
msdb
master
msdb
```