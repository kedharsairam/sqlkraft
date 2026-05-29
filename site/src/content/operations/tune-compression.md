---
title: "Tune compression"
topic: "high-availability"
description: |
  Article

  •

  01/26/2024

  Applies to:

  SQL Server

  By default, SQL Server compresses data streams where appropriate for availability groups.

  Compression reduces network traffic, increases CPU load, and
tags:
  - "high-availability"
  - "tune-compression"
pubDate: 2025-12-01
---

Article

•

01/26/2024

Applies to:

SQL Server

By default, SQL Server compresses data streams where appropriate for availability groups.

Compression reduces network traffic, increases CPU load, and might induce latency. You must

be a member of the

fixed server role to enable compression. The following table

shows when SQL Server uses compression for availability group log streams:

Synchronous-commit replica

Not compressed

Asynchronous-commit replicas

Compressed

During automatic seeding

Not compressed

TDE enabled and asynchronous-commit in database

Compressed

TDE enabled and synchronous-commit in database

Not compressed

For most scenarios, we don't recommend changing these settings. You can use global trace

flags to test changing these settings. SQL Server applies global trace flags to the entire

instance. All of the availability groups in the instance are affected by these settings.

The following table shows trace flags that change the default compression behavior for SQL

Server.

Description

1462

Disables log stream compression for availability groups with asynchronous replicas. This feature

is enabled by default on asynchronous replicas to optimize network bandwidth.

9567

Enables compression of the data stream for availability groups during automatic seeding.

During automatic seeding, compression can significantly reduce the transfer time, and increase

the load on the processor.

ﾉ

Expand table

ﾉ

Expand table
