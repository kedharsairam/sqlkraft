---
name: 'sys.column_encryption_key_values'
title: 'sys.column_encryption_key_values'
category: 'objects'
description: 'Azure SQL Managed Instance'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance


## Returns information about encrypted values of column encryption keys (CEKs) created with
either the

CREATE COLUMN ENCRYPTION KEY

or the

ALTER COLUMN ENCRYPTION KEY

(Transact-SQL)

statement. Each row represents a value of a CEK, encrypted with a column

master key (CMK).


## Description
ID of the CEK in the database.

ID of the column master key that was used to encrypt

the CEK value.

CEK value encrypted with the CMK specified in

column_master_key_id.

Name of an algorithm used to encrypt the CEK value.

Name of the encryption algorithm used to encrypt the

value. The algorithm for the system providers must be

.

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

ﾉ

Expand table

See Also

Security Catalog Views (Transact-SQL)

sys.column_encryption_keys (Transact-SQL)

sys.column_master_keys (Transact-SQL)

sys.columns (Transact-SQL)

Always Encrypted

Always Encrypted with secure enclaves

Overview of Key Management for Always Encrypted

Manage keys for Always Encrypted with secure enclaves
