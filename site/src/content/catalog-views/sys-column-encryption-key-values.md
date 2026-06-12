---
name: "sys.column_encryption_key_values"
title: "sys.column_encryption_key_values"
category: "compatibility"
description: "Returns information about encrypted values of column encryption keys (CEKs) created with statement. Each row represents a value of a CEK, encrypted with a column ID of the CEK in the database."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

Returns information about encrypted values of column encryption keys (CEKs) created with statement. Each row represents a value of a CEK, encrypted with a column ID of the CEK in the database.

## Permissions

Article • 02/28/2023 Returns information about encrypted values of column encryption keys (CEKs) created with either the CREATE COLUMN ENCRYPTION KEY or the ALTER COLUMN ENCRYPTION KEY (Transact-SQL) statement. Each row represents a value of a CEK, encrypted with a column master key (CMK). Description ID of the CEK in the database. ID of the column master key that was used to encrypt the CEK value. CEK value encrypted with the CMK specified in column_master_key_id. Name of an algorithm used to encrypt the CEK value. Name of the encryption algorithm used to encrypt the value. The algorithm for the system providers must be. Requires the permission. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration. CREATE COLUMN ENCRYPTION KEY (Transact-SQL) ALTER COLUMN ENCRYPTION KEY (Transact-SQL) DROP COLUMN ENCRYPTION KEY (Transact-SQL) CREATE COLUMN MASTER KEY (Transact-SQL) ﾉ Expand table See Also
