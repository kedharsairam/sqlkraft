---
title: "Remote blob store (RBS)"
topic: "high-availability"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  Always On availability groups can provide a high-availability and disaster recovery solution for

  SQL Server

  Remote Blob Store (RBS)

  BLOB objects (bl
tags:
  - "high-availability"
  - "remote-blob-store-rbs"
pubDate: 2025-12-01
---

Article

•

03/03/2023

SQL Server

Always On availability groups can provide a high-availability and disaster recovery solution for

SQL Server

Remote Blob Store (RBS)

BLOB objects (blobs). Always On availability groups

protects any RBS metadata and schemas stored in an availability database by replicating them

to the secondary replicas. This is the SharePoint Content Database. Generally speaking, SQL

Server stores this RBS metadata independently from the blob.

The protection for RBS BLOB data depends on the BLOB Store Location, as follows:

The same database that contains the RBS

metadata (stored using a RBS remote

FILESTREAM provider)

Yes

Another database in the same instance of SQL

Server (stored using a RBS remote FILESTREAM

provider)

Yes

We recommend that you put this database in the same

availability group as the database that contains the

RBS metadata.

Another database in a different instance of SQL

Server (stored using a RBS remote FILESTREAM

provider)

Yes

This database must be in a separate availability group.

A third-party BLOB store

No

To protect this BLOB data, use the high-availability

mechanisms of the BLOB store provider.

RBS maintainers need to be targeted on the primary replica.

ﾉ

Expand table
