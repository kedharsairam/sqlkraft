---
title: "Failover to secondary"
topic: "high-availability"
description: "Failing over to a log shipping secondary is useful if the primary server instance fails or requires maintenance. Typically, the primary and secondary"
tags: ["high-availability","failover-to-secondary"]
pubDate: 2025-12-01
---

Failing over to a log shipping secondary is useful if the primary server instance fails or requires

maintenance.

Typically, the primary and secondary databases are unsynchronized, because the primary

database continues to be updated after its latest backup job. Also, in some cases, recent

transaction log backups have not been copied to the secondary server instances, or some

copied log backups might still not have been applied to the secondary database. We

recommend that you begin by synchronizing all of the secondary databases with the primary

database, if possible.

For information about log shipping jobs, see

About Log Shipping (SQL Server).

To fail over to a secondary database:

1. Copy any uncopied backup files from the backup share to the copy destination folder of

each secondary server.

2. Apply any unapplied transaction log backups in sequence to each secondary database.

For more information, see

Apply Transaction Log Backups (SQL Server).

3. If the primary database is accessible back up the active transaction log and apply the log

backup to the secondary databases. You may need to set the database to

single-user

mode

to obtain exclusive access before issuing the restore command, and then switch it

back to multi-user after the restore completes.

If the original primary server instance is not damaged, back up the tail of the transaction

log of the primary database using WITH NORECOVERY. This leaves the database in the

restoring state and therefore unavailable to users. Eventually you will be able to roll this

database forward by applying transaction log backups from the replacement primary

database.

For more information, see

Transaction Log Backups (SQL Server).
