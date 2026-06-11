---
name: "sys.database_scoped_credentials"
title: "sys.database_scoped_credentials"
category: "compatibility"
description: "SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Returns one row for each database scoped credential in the database."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Returns one row for each database scoped credential in the database. Name of the database scoped credential. Is unique in the ID of the database scoped credential. Is unique in the database. ID of the database principal who owns the key. Name of the identity to use. It does not have to be unique. Time at which the database scoped credential was created.

## Permissions

SQL) Applies to: SQL Server 2016 (13.x) and later versions Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics SQL database in Microsoft Fabric Returns one row for each database scoped credential in the database. Description Name of the database scoped credential. Is unique in the database. ID of the database scoped credential. Is unique in the database. ID of the database principal who owns the key. Name of the identity to use. It does not have to be unique. Time at which the database scoped credential was created. Time at which the database scoped credential was last modified. Type of database scoped credential. Returns for database scoped credentials. ID of the object that the database scoped credential is mapped to. Returns for database scoped credentials Requires permission on the database. Credentials (Database Engine) CREATE DATABASE SCOPED CREDENTIAL (Transact-SQL) ALTER DATABASE SCOPED CREDENTIAL (Transact-SQL) DROP DATABASE SCOPED CREDENTIAL (Transact-SQL) CREATE CREDENTIAL (Transact-SQL) sys.credentials (Transact-SQL) ﾉ Expand table Related content Applies to: SQL Server 2016 (13.x) and later versions Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics SQL database in Microsoft Fabric Returns one row for each database scoped credential in the database. Description credential_id ID of the database scoped credential. Is unique in the database. name Name of the database scoped credential. Is unique in the database. credential_identity Name of the identity to use. This will generally be a Windows user. It does not have to be unique. create_date Time at which the database scoped credential was created. modify_date Time at which the database scoped credential was last modified. target_type Type of database scoped credential. Returns NULL for database scoped credentials. target_id ID of the object that the database scoped credential is mapped to. Returns 0 for database scoped credentials Requires permission on the database. Credentials (Database Engine) CREATE DATABASE SCOPED CREDENTIAL (Transact-SQL) ALTER DATABASE SCOPED CREDENTIAL (Transact-SQL) ） Important This feature will be removed in a future version of SQL Server. Avoid using this feature in new development work, and plan to modify applications that currently use this feature. Use instead. ﾉ Expand table See Also sys.database_scoped_credentials Credentials (Database Engine) Security Catalog Views (Transact-SQL) Principals (Database Engine) CREATE CREDENTIAL (Transact-SQL)

## Code Blocks

`name`

`credential_id`

`principal_id`

`credential_identity`

`create_date`
