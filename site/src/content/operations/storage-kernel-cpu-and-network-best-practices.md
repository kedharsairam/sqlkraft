---
title: "Storage, kernel, CPU, and network best practices"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  This article covers operating system and hardware configuration recommendations to maximize

  performance for SQL Server on Linux, including storage, kernel, CPU, and
tags:
  - "linux-operations"
  - "storage-kernel-cpu-and-network-best-practices"
pubDate: 2025-12-01
---

SQL Server

on Linux

This article covers operating system and hardware configuration recommendations to maximize

performance for SQL Server on Linux, including storage, kernel, CPU, and network settings.

Storage configuration recommendation

Kernel and CPU settings for high performance

configuration

The storage subsystem that hosts data, transaction logs, and other associated files (such as

checkpoint files for in-memory OLTP) should manage both average and peak workloads

gracefully.

In on-premises environments, the storage vendor normally supports appropriate hardware RAID

configuration with striping across multiple disks to ensure appropriate IOPS, throughput, and

redundancy. However, this support can differ across different storage vendors and different

storage offerings with varying architectures.

For SQL Server on Linux deployed on Azure Virtual Machines, consider using software RAID to

ensure appropriate IOPS and throughput. For storage considerations when configuring SQL

Server on Azure virtual machines, see

Configure storage for SQL Server on Azure VMs.

The following example shows how to create software RAID in Linux on an Azure Virtual Machine.

Use the appropriate number of data disks for the required throughput and IOPS for volumes

７

Note

For memory configuration and container memory limits, see

memory on Linux.
