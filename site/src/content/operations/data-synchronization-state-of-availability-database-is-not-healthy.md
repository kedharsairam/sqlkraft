---
title: "Data synchronization state of availability database is not healthy"
topic: "high-availability"
description: |
  Article
  
  •
  
  03/03/2023
  
  Applies to:
  
  SQL Server
  
  : Availability Database Data Synchronization State
  
  : Data synchronization state of availability database is not healthy.
  
  :
  
  Warning
  
  : Availability d
tags:
  - "high-availability"
  - "data-synchronization-state-of-availability-database-is-not-healthy"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

: Availability Database Data Synchronization State

: Data synchronization state of availability database is not healthy.

:

Warning

: Availability database

This policy rolls up the data synchronization state of all availability databases (also known as

"database replicas") in the availability replica. The policy is in an unhealthy sate when any

database replica is not in the expected data synchronization state. The policy is otherwise in a

healthy state.

The data synchronization state of this availability database is unhealthy. On an asynchronous-

commit availability replica, every availability database should be in the SYNCHRONIZING state.

On a synchronous-commit replica, every availability database must be in the SYNCHRONIZED

state.

Use the database replica policy to find the database replica with an unhealthy data

synchronization state, and then resolve the issue at the database replica.

Overview of Always On Availability Groups (SQL Server)

Use the Always On Dashboard (SQL Server Management Studio)

Description