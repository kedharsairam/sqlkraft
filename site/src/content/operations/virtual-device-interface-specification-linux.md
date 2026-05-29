---
title: "Virtual Device Interface specification (Linux)"
topic: "linux-operations"
description: |
  SQL Server on Linux VDI client SDK
  
  Article
  
  •
  
  01/21/2025
  
  Applies to:
  
  SQL Server
  
  - Linux
  
  This article covers the interfaces provided by the SQL Server on Linux virtual device interface
  
  (VDI) cli
tags:
  - "linux-operations"
  - "virtual-device-interface-specification-linux"
pubDate: 2025-12-01
---

SQL Server on Linux VDI client SDK

Article

•

01/21/2025

Applies to:

SQL Server

- Linux

This article covers the interfaces provided by the SQL Server on Linux virtual device interface

(VDI) client SDK.

Independent software vendors (ISVs) can use the Virtual Backup Device application

programming interface (API) to integrate SQL Server into their products. In general, VDI on

Linux behaves similarly to VDI on Windows with the following changes:

Windows shared memory becomes POSIX shared memory.

Windows semaphores become POSIX semaphores.

Windows types like

and

are changed to integer equivalents.

The COM interfaces are removed and replaced with a pair of C++ classes.

SQL Server on Linux doesn't support named instances, so references to instance name

have been removed.

The shared library is implemented in

, installed at

.

This article is an addendum to

Virtual device interface (VDI) reference

that details the SQL

Server VDI Specifications on Windows.

Also review the sample VDI backup solution on the

SQL Server Samples GitHub repository

.

On Linux, POSIX primitives are owned by the user creating them and their default group. For

objects created by SQL Server, these are owned by the

user and the

group by

default. To allow sharing between SQL Server and the VDI client, one of the following two

methods is recommended:

1. Run the VDI client as the

user.

７

Note

For SQL Server 2022 (16.x) on Linux, you can

instead.

```cmd
HRESULT
DWORD
libsqlvdi.so
/opt/mssql/lib/libsqlvdi.so
mssql
```