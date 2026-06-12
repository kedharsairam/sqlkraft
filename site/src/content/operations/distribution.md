---
title: "Distribution"
topic: "migration"
description: |
  Article

  •

  09/27/2024

  Applies to:

  SQL Server

  Azure SQL Managed Instance

  The Distributor is a server that contains the distribution database, which stores metadata and

  history data for all types
tags:
  - "migration"
  - "distribution"
pubDate: 2025-12-01
---

Article

•

09/27/2024

SQL Server

Azure SQL Managed Instance

The Distributor is a server that contains the distribution database, which stores metadata and

history data for all types of replication and transactions for transactional replication. To set up

replication, you must configure a Distributor. Each Publisher can be assigned to only a single

Distributor instance, but multiple publishers can share a Distributor. The Distributor uses these

additional resources on the server where it is located:

Additional disk space if the snapshot files for the publication are stored on the Distributor

(which they typically are).

Additional disk space to store the distribution database.

Additional processor usage by replication agents for push subscriptions running on the

Distributor.

The server you select as the Distributor should have adequate disk space and processor power

to support replication and any other activities on that server. When you configure the

Distributor, you specify the following:

A snapshot folder, which is used, by default, for all Publishers that use this Distributor.

Ensure that this folder is already shared and has the appropriate permissions set. For

more information, see

Secure the Snapshot Folder.

A name and file locations for the distribution database. The distribution database cannot

be renamed after it is created. To use a different name for the database, you must disable

distribution and reconfigure it.

Any Publishers authorized to use the Distributor. If you specify Publishers other than the

instance on which the Distributor runs, you must also specify a password for the

connections the Publishers make to the remote Distributor.

For transactional replication, after you configure distribution, we recommend that you:

Size the distribution database appropriately. Test replication with a typical load for your

system to determine how much space is required to store commands. Ensure the

database is large enough to store commands without having to auto-grow frequently. For

more information about changing the size of a database, see

ALTER DATABASE (Transact-

SQL).

Set the

option on the distribution database. For more information, see

Strategies for Backing Up and Restoring Snapshot and Transactional Replication

and
