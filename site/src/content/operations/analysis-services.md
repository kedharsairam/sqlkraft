---
title: "Analysis Services"
topic: "upgrade"
description: "06/04/2025 - Windows only Analysis Services instances can be upgraded to a SQL Server version of the same server mode to take advantage of features introduced in the curren"
tags: ["upgrade","analysis-services"]
pubDate: 2025-12-01
---

- Windows only

Analysis Services instances can be upgraded to a SQL Server version of the same server mode

to take advantage of features introduced in the current release, as described in

What's new in

Analysis Services.

You can upgrade each instance in-place, independently of other instances running on the same

hardware. However, most administrators choose to install a new instance of the new version for

application testing before transferring production workloads onto the new server. But for

development or test servers, an in-place upgrade might be more convenient.

There are two basic approaches for upgrading servers and databases:

The upgrade process automatically migrates existing databases from the old instance to the

new instance. Because the metadata and binary data is compatible between the two versions,

you'll retain the data after you upgrade and you don't have to manually migrate the data.

To upgrade an existing instance, run Setup and specify the name of the existing instance as the

name of the new instance.

Backup all databases and verify that each can be restored. To learn more, see

Backup and

restore Analysis Services databases.

Identify a subset of reports, spreadsheets, or dashboard snapshots to use later as the

basis for confirming post-upgrade server operations. If possible, collect performance

７

Note

The compatibility levels of databases that are attached to a given server remain the same

unless you manually change them.
