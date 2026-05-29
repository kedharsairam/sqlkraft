---
name: 'sys.database_recovery_status'
title: 'sys.database_recovery_status (Transact-'
category: 'objects'
description: 'NULL= Database is offline, or the database will not start.'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
NULL= Database is offline, or the database will not start.

Identifier of the starting recovery fork.

NULL= Database is offline, or the database will not start.

If

is not equal (!=) to

,

is the log sequence

number of the current fork point. Otherwise, the value is

NULL.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Catalog Views (Transact-SQL)

Databases and Files Catalog Views (Transact-SQL)

RESTORE HEADERONLY (Transact-SQL)

Querying the SQL Server System Catalog FAQ

See Also
