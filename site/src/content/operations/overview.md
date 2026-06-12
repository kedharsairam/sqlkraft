---
title: "Overview"
topic: "high-availability"
description: ""
tags: ["high-availability","overview"]
pubDate: "2025-12-01"
---

ﾃ

Summarize this article for me

Log shipping allows you to automatically send transaction log backups from a

primary database

on a

primary server

instance to one or more

secondary databases

on separate

secondary server

instances. The transaction log backups are applied to each of the secondary

databases individually. An optional third server instance, known as the

monitor server

, records

the history and status of backup and restore operations and, optionally, raises alerts if these

operations fail to occur as scheduled.

Log shipping consists of three operations:

1. Back up the transaction log at the primary server instance.

2. Copy the transaction log file to the secondary server instance.

3. Restore the log backup on the secondary server instance.

The log can be shipped to multiple secondary server instances. In such cases, operations 2 and

3 are duplicated for each secondary server instance.

A log shipping configuration doesn't automatically fail over from the primary server to the

secondary server. If the primary database becomes unavailable, any of the secondary databases

can be brought online manually.

You can use a secondary database for reporting purposes.

In addition, you can configure alerts for your log shipping configuration.

The following figure shows a log shipping configuration with the primary server instance, three

secondary server instances, and a monitor server instance. The figure illustrates the steps

performed by backup, copy, and restore jobs, as follows:

1. The primary server instance runs the backup job to back up the transaction log on the

primary database. This server instance then places the log backup into a primary log-

backup file, which it sends to the backup folder. In this figure, the backup folder is on a

shared directory-the

backup share.
