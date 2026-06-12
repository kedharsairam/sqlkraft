---
title: "Transaction log file size management"
topic: "io-fundamentals"
description: "Hot add CPU is the ability to dynamically add CPUs to a running system."
tags: ["io-fundamentals","architecture"]
pubDate: 2026-05-29
---

Hot add CPU is the ability to dynamically add CPUs to a running system. Adding CPUs can

occur physically by adding new hardware, logically by online hardware partitioning, or virtually

through a virtualization layer.

Requirements for hot add CPU:

Requires hardware that supports hot add CPU.

Requires a supported version of Windows Server Datacenter or Enterprise edition.

Starting with Windows Server 2012, hot add is supported on Standard edition.

Requires SQL Server Enterprise edition.

can't be configured to use soft NUMA. For more information about soft

NUMA, see

Soft-NUMA (SQL Server).

doesn't automatically use CPUs after they are added. This prevents SQL Server from

using CPUs that might be added for some other purpose. After adding CPUs, execute the

RECONFIGURE

statement, so that SQL Server recognizes the new CPUs as available resources.

If the

affinity64 mask

is configured, the affinity64 mask must be modified to use the new CPUs.

Don't use the affinity mask and affinity64 mask server configuration options to bind processors

to specific threads. These options are limited to 64 CPUs. Use the

option

of

ALTER SERVER CONFIGURATION

instead.

Don't rely on autogrow to increase the size of the transaction log file. Increasing the

transaction log must be a serial process. Extending the log can prevent transaction write

operations from proceeding until the log extension is finished. Instead, preallocate space for

the log files by setting the file size to a value large enough to support the typical workload in

the environment.

Starting with SQL Server 2025 (17.x), the hot add CPU feature is deprecated, and is

planned for removal in a future version of SQL Server. Because of known stability issues,

Microsoft recommends that you avoid using this feature in SQL Server administration in

any version of SQL Server.

## max degree of parallelism (MAXDOP)

## max worker threads

```sql
SET PROCESS AFFINITY
```
