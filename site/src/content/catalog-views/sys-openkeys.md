---
name: "sys.openkeys"
title: "sys.openkeys"
category: "compatibility"
description: "SQL database in Microsoft Fabric This catalog view returns information about encryption keys that are open in the current ID of the database that contains the key."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

SQL database in Microsoft Fabric This catalog view returns information about encryption keys that are open in the current ID of the database that contains the key. Name of the database that contains the key. ID of the key. The ID is unique within the database. Name of the key. Unique within the database. GUID of the key. Unique within the database. Date and time when the key was opened. 1 if the key is valid in metadata. 0 if the key is not found in metadata.

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric This catalog view returns information about encryption keys that are open in the current session. Description ID of the database that contains the key. Name of the database that contains the key. ID of the key. The ID is unique within the database. Name of the key. Unique within the database. GUID of the key. Unique within the database. Date and time when the key was opened. 1 if the key is valid in metadata. 0 if the key is not found in metadata. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . Encryption Hierarchy OPEN SYMMETRIC KEY (Transact-SQL) Last updated on 11/18/2025 ﾉ Expand table See Also
