---
title: "Warning thresholds on performance"
topic: "high-availability"
description: "This topic contains information about the SQL Server events for which warning thresholds can be configured and managed for database mirroring."
tags: ["high-availability","warning-thresholds-on-performance"]
pubDate: "2025-12-01"
---

This topic contains information about the SQL Server events for which warning thresholds can

be configured and managed for database mirroring. You can use the Database Mirroring

Monitor or the

,

, and

stored procedures. This topic also contains information about

configuring alerts on database mirroring events.

After monitoring is established for a mirrored database, a system administrator can configure

warning thresholds on several key performance metrics. Also, an administrator can configure

alerts on these and other database mirroring events.

The following table lists the performance metrics for which warnings can be configured,

describes the corresponding warning threshold, and lists the corresponding Database

Mirroring Monitor label.

Warning threshold

Unsent log

Specifies how many kilobytes (KB) of unsent log generate a

warning on the principal server instance. This warning helps

measure the potential for data loss in terms of KB and is especially

relevant for high-performance mode. However, the warning is also

relevant for high-safety mode when mirroring is paused or

suspended because the partners become disconnected.

Unrestored log

Specifies how many KB of unrestored log generate a warning on

the mirror server instance. This warning helps measure failover

time.

Failover time

consists mainly of the time that the former

mirror server requires to roll forward any log remaining in its redo

queue, plus a short additional time.

Note: For an automatic failover, the time for the system to notice

ﾉ

Expand table
