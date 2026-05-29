---
title: "Some availability replicas are not synchronizing data"
topic: "high-availability"
description: |
  Article

  •

  01/14/2025

  Applies to:

  SQL Server

  : Availability Replicas Data Synchronization State

  : Some availability replicas are not synchronizing data.

  :

  Warning

  : Availability group

  This po
tags:
  - "high-availability"
  - "some-availability-replicas-are-not-synchronizing-data"
pubDate: 2025-12-01
---

Article

•

01/14/2025

Applies to:

SQL Server

: Availability Replicas Data Synchronization State

: Some availability replicas are not synchronizing data.

:

Warning

: Availability group

This policy rolls up the data synchronization state of all availability replicas in the availability

group and checks if the synchronization of any availability replica is not operational. The policy

is in an unhealthy state if any of the data synchronization states of the availability replica is

NOT SYNCHRONIZING.

This policy is in a healthy state if none of the data synchronization states of the availability

replica is NOT SYNCHRONIZING.

In this availability group, at least one secondary replica has a NOT SYNCHRONIZING

synchronization state and is not receiving data from the primary replica.

Use the availability replica policy state to find the availability replica with a NOT

SYNCHRONIZING state, and then resolve the issue at the availability replica.

Overview of Always On Availability Groups (SQL Server)

Use the Always On Dashboard (SQL Server Management Studio)

Description
