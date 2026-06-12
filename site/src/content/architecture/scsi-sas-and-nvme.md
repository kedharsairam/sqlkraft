---
title: "SCSI, SAS, and NVMe"
topic: "query-processing"
description: "### Windows Hardware Compatibility Program"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

### Windows Hardware Compatibility Program

Also review the following archived content:

2000 I/O Basics

I/O Basics Chapter 2

The concepts in these two articles remain broadly applicable to current versions of SQL Server.

Enhanced caching controller systems disable on-disk cache and provide a functional battery-

backed caching solution. These caches can maintain the data in the cache for several days and

even allow the caching card to be placed in a second computer. When power is properly

restored, the unwritten data is completely flushed before any further data access is allowed. Many

of these systems allow you to establish a percentage of read versus write cache for optimal

performance. Some systems contain large memory storage areas. Some hardware vendors

provide high-end battery-backed drive caching systems with multiple gigabytes of cache. These

systems can significantly improve database performance. Battery-backed caching solutions

provide the durability and consistency of data that SQL Server expects.

Storage subsystems exist in many types. Two common examples are RAID (redundant array of

independent disks) and SAN (storage area network). These systems typically use SCSI-based

drives. The following section describes high-level storage considerations.

SCSI, SAS, and NVMe storage devices:

Are typically designed for heavy-duty use.

Are typically targeted at multiuser, server-based implementations.

Typically have better mean time to failure rates than other implementations.

Contain sophisticated heuristics to help predict imminent failures.

７

Note

supports Internet Small Computer System Interface (iSCSI) technology

components that meet the requirements of the.

Although SQL Server doesn't interact directly with iSCSI, it operates seamlessly because

Windows presents iSCSI storage as standard drives. SQL Server can then read from, and

### iSCSI Target Server Scalability

### Limits
