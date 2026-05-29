---
title: "Pacemaker basics"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  Starting with SQL Server 2017 (14.x), SQL Server is supported on both Linux and Windows. Like

  Windows-based SQL Server deployments, SQL Server databases and instanc
tags:
  - "linux-operations"
  - "pacemaker-basics"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

Starting with SQL Server 2017 (14.x), SQL Server is supported on both Linux and Windows. Like

Windows-based SQL Server deployments, SQL Server databases and instances need to be

highly available under Linux. This article covers the basic information to understand Pacemaker

with Corosync, and how to plan and deploy it for SQL Server configurations.

All of the currently supported distributions ship a high availability add-on/extension, which is

based on the Pacemaker clustering stack. This stack incorporates two key components:

Pacemaker and Corosync. All the components of the stack are:

The core clustering component that coordinates things across the clustered

machines.

A framework and set of APIs that provides things like quorum, the ability to

restart failed processes, and so on.

Provides things like logging.

Specific functionality provided so that an application can integrate with

Pacemaker.

Scripts/functionality that help with isolating nodes and deal with them if

they are having issues.

This solution is in some ways similar to, but in many ways different from deploying clustered

configurations using Windows. In Windows, the availability form of clustering, called a

Windows Server failover cluster (WSFC), is built into the operating system, and the feature that

enables the creation of a WSFC, failover clustering, is disabled by default. In Windows, AGs and

FCIs are built on top of a WSFC, and share tight integration because of the specific resource

DLL that is provided by SQL Server. This tightly coupled solution is possible by and large

because it's all from one vendor.

７

Note

The cluster stack is commonly referred to as Pacemaker in the Linux world.
