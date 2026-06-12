---
title: "Causes of long I/O requests"
topic: "io-fundamentals"
description: "All I/Os are issued in the calling threads unless the affinity I/O option is in use. The"
tags: ["io-fundamentals", "architecture"]
pubDate: 2026-05-29
---

All I/Os are issued in the calling threads unless the affinity I/O option is in use. The

affinity

I/O mask

option binds SQL Server disk I/O to a specified subset of CPUs. In high-end SQL

Server online transactional processing (OLTP) environments, this extension can enhance the

performance of SQL Server threads issuing I/Os.

Multiple page I/Os are accomplished with scatter-gather I/O, which allows data to be

transferred into or out of noncontiguous areas of memory. SQL Server can quickly fill or

flush the buffer cache while avoiding multiple physical I/O requests.

The buffer manager reports any I/O request that is outstanding for at least 15 seconds. This

process helps the system administrator distinguish between SQL Server problems and I/O

subsystem problems. Error message

MSSQLSERVER_833

is reported and appears in the SQL

Server error log as follows:

A long I/O can be either a read or a write operation. The message doesn't currently indicate

which. Long-I/O messages are warnings, not errors. They don't indicate problems with SQL Server

but with the underlying I/O system. The messages help the system administrator find the cause

of poor SQL Server response times more quickly, and distinguish problems that are outside the

control of SQL Server. As such, they don't require any action, but the system administrator should

investigate why the I/O request took so long, and whether the time is justifiable.

A long I/O message can indicate that an I/O is permanently blocked and will never complete

(known as lost I/O), or merely that it isn't complete yet. You can't tell from the message which

scenario is the case, although a lost I/O often leads to a latch timeout.

Long I/Os often indicate a SQL Server workload that's too intense for the disk subsystem. An

inadequate disk subsystem might be indicated when:

Multiple long I/O messages appear in the error log during a heavy SQL Server workload.

Performance Monitor counters show long disk latencies, long disk queues, or no disk idle

time.

```sql
has encountered ## occurrence(s) of I/O requests taking longer than 15 seconds to complete on file [##] in database [##] (#). The OS file handle is 0x00000.
The offset of the latest long I/O is: 0x00000.
```
