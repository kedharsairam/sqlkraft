---
title: "Forced manual failover"
topic: "high-availability"
description: "10/06/2025 This article describes how to perform a forced failover (with possible data loss) on an Always On availability group by using SQL Server Management Studio, Transa"
tags: ["high-availability","forced-manual-failover"]
pubDate: "2025-12-01"
---

This article describes how to perform a forced failover (with possible data loss) on an Always

On availability group by using SQL Server Management Studio, Transact-SQL, or PowerShell in. A forced failover is a form of manual failover that is intended strictly for disaster

recovery, when a

planned manual failover

isn't possible. If you force failover to an

unsynchronized secondary replica, some data loss is possible. Therefore, we strongly

recommend that you force failover only if you must restore service to the availability group

immediately and you're willing to risk losing data.

After a forced failover, the failover target to which the availability group was failed over

becomes the new primary replica. The secondary databases in the remaining secondary

replicas are suspended and must be manually resumed. When the former primary replica

becomes available, it transitions to the secondary role, causing the former primary databases to

become secondary databases and transition into the

state. Before you resume a

given secondary database, you might be able to recover lost data from it. However, notice that

transaction log truncation is delayed on a given primary database while any of its secondary

databases is suspended.

Performing a forced failover is necessary in the following emergency situations:

After forcing quorum on the WSFC cluster (

forced quorum

), you need to force failover

each availability group (with possible data loss). Forcing failover is required because the

real state of the WSFC cluster values might have been lost. However, you can avoid data

loss, if you are able to force failover on the server instance that was hosting the replica

that was the primary replica before you forced quorum or to a secondary replica that was

synchronized before you forced quorum. For more information, see

Potential Ways to

Avoid Data Loss After Quorum is Forced

, later in this article.

）

Important

Data synchronization with the primary database doesn't occur until the secondary

database is resumed. For information about resuming a secondary database, see

later in this article.

）

Important

```cmd
SUSPENDED
```
