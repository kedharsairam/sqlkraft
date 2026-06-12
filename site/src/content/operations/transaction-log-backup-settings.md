---
title: "Transaction Log Backup Settings"
topic: "high-availability"
description: "Use this dialog box to configure and modify the transaction log backup settings for a log shipping configuration. For an explanation of log shipping"
tags: ["high-availability","transaction-log-backup-settings"]
pubDate: 2025-12-01
---

Use this dialog box to configure and modify the transaction log backup settings for a log

shipping configuration.

For an explanation of log shipping concepts, see

About Log Shipping (SQL Server).

Type the network share to your backup folder in this box. The local folder where your

transaction log backups are saved must be shared so that the log shipping copy jobs can copy

these files to the secondary server. You must grant read permissions on this network share to

the proxy account under which the copy job will run at the secondary server instance. By

default, this is the SQLServerAgent service account of the secondary server instance, but an

administrator can choose another proxy account for the job.

Type the local drive letter and path to the backup folder if the backup folder is located on the

primary server. If the backup folder is not located on the primary server, you can leave this

blank.

If you specify a local path here, the BACKUP command will use this path to create the

transaction log backups; otherwise, if no local path is specified, the BACKUP command will use

the network path specified in the

box.

Specify the length of time you want transaction log backups to remain in your backup directory

before being deleted.

７

Note

If the SQL Server service account is running under the local system account on the primary

server, you must create the backup folder on the primary server and specify the local path

to that folder here. The SQL Server service account of the primary server instance must

have Read and Write permissions on this folder.
