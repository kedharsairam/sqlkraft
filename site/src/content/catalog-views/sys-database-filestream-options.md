---
name: 'sys.database_filestream_options'
title: 'sys.database_filestream_options (Transact-'
category: 'databases-files'
description: 'Displays information about the level of non-transactional access to FILESTREAM data in'
tags: ["catalog-view", "databases-files"]
pubDate: 2026-05-29
---

SQL)

Article

•

02/28/2023

Applies to:

SQL Server

Displays information about the level of non-transactional access to FILESTREAM data in

FileTables that is enabled. Contains one row for each database in the SQL Server instance.

For more information about FileTables, see

FileTables (SQL Server)

.


## Description
The ID of the database. This value is unique within the

SQL Server instance.

The database-level directory for all FileTable namespaces.

The level of non-transactional access to FILESTREAM data

that is enabled. The level of access is set by the

NON_TRANSACTED_ACCESS option of the

or

statement.

This setting has one of the following values:

0 - Not enabled. This is the default value. This level is set

by providing the value

for the

option.

1 - Read-only access. This level is set by providing the

value

for the

option.

3 - Full access. This level is set by providing the value

for the

option.

5 - In transition to READONLY

6 - In transition to OFF

The description of the level of non-transactional access

identified in non_transacted_access.

This setting has one of the following values:

NONE - This is the default value.

ﾉ

Expand table


## Description
READ_ONLY

FULL

IN_TRANSITION_TO_READ_ONLY

IN_TRANSITION_TO_OFF

Enable the Prerequisites for FileTable

See Also
