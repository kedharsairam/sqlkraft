---
title: "Configure persistent memory (PMEM)"
topic: "linux-operations"
description: |
  SQL Server on Linux

  Applies to:

  SQL Server

  on Linux

  This article describes how to configure the persistent memory (PMEM) for SQL Server 2019

  (15.x) and later versions on Linux.

  SQL Server 2019 (
tags:
  - "linux-operations"
  - "configure-persistent-memory-pmem"
pubDate: 2025-12-01
---

SQL Server on Linux

Applies to:

SQL Server

on Linux

This article describes how to configure the persistent memory (PMEM) for SQL Server 2019

(15.x) and later versions on Linux.

SQL Server 2019 (15.x) introduced many in-memory features that use persistent memory. This

article covers the steps required to configure persistent memory for SQL Server on Linux.

In Linux, use the

utility.

Install

to configure PMEM device from

Installing NDCTL

.

Use

to create a namespace. Namespaces are interleaved across PMEM NVDIMMs

and can provide different types of user-space access to memory regions on the device.

is default and desired mode for SQL Server.

Bash

７

Note

The term

enlightenment

was introduced to convey the concept of working with a

persistent memory aware file system. Direct access to the file system from user-space

applications is facilitated using memory mapping (

). When a memory mapping for

a file is created the application can issue load/store instructions bypassing the I/O stack

completely. This is considered an "enlightened" file access method from the perspective of

the host extension application (which is the code that allows SQLPAL interact with the

Windows or Linux OS).

```cmd
ndctl ndctl ndctl fsdax mmap()
```
