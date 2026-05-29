---
title: "Some synchronous replicas are not synchronized"
topic: "high-availability"
description: |
  Article
  
  •
  
  02/01/2024
  
  Applies to:
  
  SQL Server
  
  : Synchronous Replicas Data Synchronization State
  
  : Some synchronous replicas are not synchronized.
  
  :
  
  Warning
  
  : Availability group
  
  This policy rol
tags:
  - "high-availability"
  - "some-synchronous-replicas-are-not-synchronized"
pubDate: 2025-12-01
---

Article

•

02/01/2024

Applies to:

SQL Server

: Synchronous Replicas Data Synchronization State

: Some synchronous replicas are not synchronized.

:

Warning

: Availability group

This policy rolls up the data synchronization state of all availability replicas and checks for any

availability replicas that are not in the expected synchronization state. The policy is in an

unhealthy state when any asynchronous replica is not in a SYNCHRONIZING state and any

synchronous replica is not in a SYNCHRONIZED state. The policy state is otherwise healthy.

In this availability group, at least one synchronous replica is not currently synchronized. The

replica synchronization state could be either SYNCHRONIZING or NOT SYNCHRONIZING.

Use the availability replica policy state to find the availability replica with the incorrect

synchronization state, and then resolve the issue at the availability replica.

Overview of Always On Availability Groups (SQL Server)

Use the Always On Dashboard (SQL Server Management Studio)

Description