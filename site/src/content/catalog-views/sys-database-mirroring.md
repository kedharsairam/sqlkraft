---
name: 'sys.database_mirroring'
title: 'sys.database_mirroring'
category: 'objects'
description: 'UNLIMITED indicates that mirroring doesn''t inhibit'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
UNLIMITED indicates that mirroring doesn't inhibit

the redo queue. This is the default setting.

MB for maximum size of the redo queue in mega

bytes. Note that if the queue size was specified as

kilobytes or gigabytes, the Database Engine converts

the value into megabytes.

If the database isn't online, this column is NULL.

The local end-of-log that has been flushed to disk.

This is comparable to the hardened LSN from the

mirror server (see the

column).

The maximum LSN that replication can send.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Requires VIEW SERVER PERFORMANCE STATE permission on the server.

Catalog Views (Transact-SQL)

ALTER DATABASE (Transact-SQL)

sys.database_mirroring_witnesses (Transact-SQL)

sys.database_mirroring_endpoints (Transact-SQL)

Databases and Files Catalog Views (Transact-SQL)

Querying the SQL Server System Catalog FAQ

Last updated on 03/03/2026


## Permissions for SQL Server 2022 and later
Related content
