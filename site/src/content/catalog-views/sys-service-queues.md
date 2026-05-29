---
name: 'sys.service_queues'
title: 'sys.service_queues'
category: 'objects'
description: 'Contains a row for each object in the database that is a service queue, with'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Article

•

02/28/2023

Applies to:

SQL Server

Contains a row for each object in the database that is a service queue, with

=

SQ.


## Description
For a list of columns that this view inherits, see

sys.objects (Transact-SQL)

.

Maximum number of the concurrent readers

allowed in the queue.

Three-part name of the activation procedure.

ID of the EXECUTE AS database principal.

NULL by default or if EXECUTE AS CALLER.

ID of the specified principal if EXECUTE AS SELF

EXECUTE AS <principal>.

-2 = EXECUTE AS OWNER.

1 = Activation is enabled.

1 = Receive is enabled.

1 = Enqueue is enabled.

1 = Messages are retained until dialog end.

: SQL Server 2012 (11.x) and later.

1 = Poison message handling is enabled.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

ﾉ

Expand table

Object Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

See Also
