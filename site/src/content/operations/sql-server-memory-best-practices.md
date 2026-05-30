---
title: "SQL Server memory best practices"
topic: "linux-operations"
description: |
  Applies to:

  SQL Server

  on Linux

  This article covers memory configuration for SQL Server on Linux, including

  memory

  limits, control group (

  ) settings, Docker container memory examples, and swap
tags:
  - "linux-operations"
  - "sql-server-memory-best-practices"
pubDate: 2025-12-01
---

Applies to:

SQL Server

on Linux

This article covers memory configuration for SQL Server on Linux, including

memory

limits, control group (

) settings, Docker container memory examples, and swap space

considerations.

To ensure there's enough free physical memory for the Linux operating system, the SQL Server

process uses only 80 percent of the physical RAM by default. For some systems with large

amounts of physical RAM, 20 percent might be a significant number. For example, on a system

with 1 TB of RAM, the default setting leaves around 200 GB of RAM unused. In this situation, you

might want to configure the memory limit to a higher value.

You can adjust this value using the

tool or the

environment

variable. For more information, see the

memory.memorylimitmb

setting that controls the

memory visible to SQL Server (in units of MB). For detailed sizing guidance, see

Guidelines for

setting memory limits on Linux and in containers

.

SQL Server detects and honors control group (cgroup) v2 constraints, starting with SQL Server

2025 (17.x) and SQL Server 2022 (16.x) Cumulative Update (CU) 20. These constraints provide

fine-grained control in the Linux kernel over CPU and memory resources, and improve resource

isolation in Docker, Kubernetes, and OpenShift environments.

In earlier versions, containerized deployments on Kubernetes clusters (for example, Azure

Kubernetes Service v1.25+) could experience out of memory (OOM) errors because SQL Server

７

Note

For storage, kernel, CPU, and network recommendations, see

.

```cmd
mssql-conf cgroup
MSSQL_MEMORY_LIMIT_MB
```
