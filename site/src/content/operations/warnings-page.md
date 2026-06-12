---
title: "Warnings Page"
topic: "high-availability"
description: |
  Article

  •

  02/01/2024

  Applies to:

  SQL Server

  Displays a read-only list of warnings supported on database mirroring events and the specified

  warning threshold values, if available.

  Start Database
tags:
  - "high-availability"
  - "warnings-page"
pubDate: 2025-12-01
---

Article

•

02/01/2024

SQL Server

Displays a read-only list of warnings supported on database mirroring events and the specified

warning threshold values, if available.

Start Database Mirroring Monitor (SQL Server Management Studio)

Warning

The warnings for which you can define a threshold include:

Warning

Specifies how many kilobytes (KB) of unsent log will generate a warning on the

principal server instance. This warning helps measure the potential for data loss in

terms of KB, and is particularly relevant for high-performance mode. However, the

warning is also relevant for high-safety mode when mirroring is paused or

suspended because the partners become disconnected.

Specifies how many KB of unrestored log will generate a warning on the mirror

server instance. This warning is useful for measuring failover time in terms of

kilobytes.

Failover time

consists mainly of the time that the former mirror server

requires to roll forward any log remaining in its redo queue, plus a short

additional time.

Note: For an automatic failover, the time for the system to notice the error is

independent of the failover time.

For more information, see

Estimate the Interruption of Service During Role

Switching (Database Mirroring).

Specifies the number of minutes worth of transactions that can accumulate in the

send queue before a warning is generated on the principal server instance. This

warning helps measure the potential for data loss in terms of time, and is

particularly relevant for high-performance mode. However, the warning is also

relevant for high-safety mode when mirroring is paused or suspended because

the partners become disconnected.

ﾉ

Expand table
