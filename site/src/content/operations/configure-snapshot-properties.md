---
title: "Configure snapshot properties"
topic: "migration"
description: |
  Article

  •

  09/27/2024

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  Snapshot properties can be defined and modified programmatically using replication stored

  procedures, where the stored pro
tags:
  - "migration"
  - "configure-snapshot-properties"
pubDate: 2025-12-01
---

Article

•

09/27/2024

SQL Server

Azure SQL Managed Instance

Snapshot properties can be defined and modified programmatically using replication stored

procedures, where the stored procedures used depend on the type of publication.

1. At the Publisher, execute

sp_addpublication. Specify a publication name for

,

a value of either

or

for

, and one or more of the

following snapshot-related parameters:

- specify a path if the snapshot for this publication is accessed

from that location instead of or in addition to the snapshot default folder.

- specify a value of

if the snapshot files in the alternate

snapshot folder are compressed in the Microsoft CAB file format.

- specify the file name and full path of a

file that will be

executed at the Subscriber during initialization before the initial snapshot is applied.

- specify the file name and full path of a

file that will be

executed at the Subscriber during initialization after the initial snapshot is applied.

- specify a value of

if the snapshot is available

only in a non-default location.

For more information about creating publications, see

Create a Publication.

1. At the Publisher, execute

sp_addmergepublication. Specify a publication name for

, a value of either

or

for

, and one or more

of the following snapshot-related parameters:

- specify a path if the snapshot for this publication is accessed

from that location instead of or in addition to the snapshot default folder.

- specify a value of

if the snapshot files in the alternate

snapshot folder are compressed in the CAB file format.

```cmd
@publication
@repl_freq
@alt_snapshot_folder
@compress_snapshot
@pre_snapshot_script
```
