---
name: 'sys.column_encryption_keys'
title: 'sys.column_encryption_keys'
category: 'objects'
description: 'SQL Server 2016 (13.x) and later versions'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Article

•

02/28/2023

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

Synapse Analytics

Analytics Platform System (PDW)


## Returns information about column encryption keys (CEKs) created with the
CREATE COLUMN

ENCRYPTION KEY

statement. Each row represents a CEK.


## Description
The name of the CEK.

ID of the CEK.

Date the CEK was created.

Date the CEK was last modified.

Requires the

permission.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

CREATE COLUMN ENCRYPTION KEY (Transact-SQL)

ALTER COLUMN ENCRYPTION KEY (Transact-SQL)

DROP COLUMN ENCRYPTION KEY (Transact-SQL)

CREATE COLUMN MASTER KEY (Transact-SQL)

Security Catalog Views (Transact-SQL)

sys.column_encryption_key_values (Transact-SQL)

Always Encrypted

Always Encrypted with secure enclaves

Overview of Key Management for Always Encrypted

Manage keys for Always Encrypted with secure enclaves

ﾉ

Expand table

See Also
