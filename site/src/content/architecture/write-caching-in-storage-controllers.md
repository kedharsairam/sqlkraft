---
title: "Write caching in storage controllers"
topic: "query-processing"
description: "A component in the I/O path (for example, a driver, controller, or firmware) can cause long I/Os"
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

A component in the I/O path (for example, a driver, controller, or firmware) can cause long I/Os

by continually postponing servicing an old I/O request, in favor of servicing newer requests. This

problem can occur in interconnected environments, such as

iSCSI

and Fibre Channel networks

(either due to a misconfiguration or path failure). The Performance Monitor tool can make this

problem difficult to confirm because most I/Os are being serviced promptly. Workloads that

perform large amounts of sequential I/O, such as backup and restore, table scans, sorting,

creating indexes, bulk loads, and zeroing out files, can aggravate long I/O requests.

Isolated long I/Os that don't appear related to any of the previous conditions can be caused by a

hardware or driver problem. The system event log might contain a related event that helps to

diagnose the problem.

Slow I/O can be caused by queries that aren't written efficiently or tuned properly with indexes

and statistics. Another common factor in I/O latency is the presence of antivirus or other security

programs that scan database files. This scanning software might extend to the network layer,

which adds network latency, in turn indirectly affecting database latency. Although the scenario

described about

15-second I/O

is more common with hardware components, shorter I/O delays

are more frequently observed with unoptimized queries or misconfigured antivirus programs.

For detailed information on how to address these issues, see

Troubleshoot slow SQL Server

performance caused by I/O issues.

For information on how to configure antivirus protection on SQL Server, see

Configure antivirus

software to work with SQL Server.

I/O transfers that don't use a cache can take much longer on mechanical drives because of hard

drive spin rates, the mechanical time needed to move the drive heads, and other limiting factors.

installations target systems that provide caching controllers. These controllers disable

the on-disk caches and provide stable media caches to satisfy SQL Server I/O requirements. They

avoid performance problems related to storage seek and write times by using the various

optimizations of the caching controller.

７

Note

### Configure persistent memory

### (PMEM) for SQL Server on Windows

### Configure persistent memory (PMEM) for SQL

### Server on Linux
