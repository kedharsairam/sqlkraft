---
title: "Backup on Secondary Replica"
topic: "high-availability"
description: "The Always On availability groups active secondary capabilities include support for taking backups on secondary replicas. Backup operations can put significant strain on I/O"
tags: ["high-availability","backup-on-secondary-replica"]
pubDate: "2025-12-01"
---

The Always On availability groups active secondary capabilities include support for taking

backups on secondary replicas. Backup operations can put significant strain on I/O and CPU

(with backup compression). Offloading backups to a synchronized or synchronizing secondary

replica allows you to use the resources on server instance that hosts the primary replica for

your tier-1 workloads.

To perform a full database backup on a secondary replica, you must take a

Copy-only backups

,

since copy-only backups don't impact the log chain or clear the differential bitmap. Consider:

Copy-only backups don't prevent the truncation of the transaction log on other replicas.

A copy-only backup prevents log truncation on the secondary replica while it's executing

the copy-only backup, for the duration of the backup.

If the transaction log is truncated on the primary replica to an LSN that is between the

first and last LSN of the transaction log of the secondary replica executing the copy-only

backup, you might see the following error in the log of the secondary replica:

While the backup is likely to succeed, synchronization fails for that secondary replica until

the copy-only backup completes, and, if the secondary replica is set to synchronous

commit, write workloads on the primary replica might be blocked until the log can harden

on the secondary replica. After the backup completes, the log is truncated on the

secondary replica, at which point it should synchronize again. If you encounter error 9019

while running a copy-only backup on a secondary replica, then run the full backup on the

primary replica instead.

７

Note

statements aren't allowed on either the primary or secondary databases of an

availability group.

```cmd
Error 9019: The virtual log file sequence 0x%08x at offset 0x%016I64x bytes in file
'%ls' is active and cannot be overwritten with sequence 0x%08x for database '%ls'.
RESTORE
```
