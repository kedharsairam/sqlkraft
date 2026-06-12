---
title: "Start data movement"
topic: "high-availability"
description: "This topic contains information about how to start data synchronization after you add a database to an Always On availability group."
tags: ["high-availability","start-data-movement"]
pubDate: 2025-12-01
---

This topic contains information about how to start data synchronization after you add a

database to an Always On availability group. For each new primary replica, secondary

databases must be prepared on the server instances that host the secondary replicas. Then

each of these secondary databases must be manually joined to the availability group.

To start data synchronization manually, you need to connect, in turn, to each server instance

that is hosting a secondary replica for the availability group and complete the following steps:

1. Restore current backups of each primary database and its transaction log (using RESTORE

WITH NORECOVERY). You can use either of the following alternative approaches:

Manually restore a recent database backup of the primary database using RESTORE

WITH NORECOVERY, and then restore each subsequent log backup using RESTORE

WITH NORECOVERY. Perform this restore sequence on every server instance that

hosts a secondary replica for the availability group.

Manually Prepare a Secondary Database for an Availability Group (SQL Server)

If you are adding one or more log shipping primary databases to an availability

group, you might be able to migrate one or more of the corresponding secondary

databases from log shipping to Always On Availability Groups. Migrating a log

shipping secondary database requires that it use the same database name as the

primary database and that it reside on a server instance that is hosting a secondary

replica for the availability group. Furthermore, the availability group must be

configured so that the primary replica is preferred for backups and is a candidate for

performing backups (that is, that has a backup priority that is >0). Once the backup

job has run on the primary database, you will need to disable the backup job, and

７

Note

If the file paths are identical on every server instance that hosts an availability replica for

an availability group, the

,

, or

might be able to

automatically start data synchronization for you.
