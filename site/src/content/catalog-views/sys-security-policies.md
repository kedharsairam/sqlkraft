---
name: "sys.security_policies"
title: "sys.security_policies"
category: "security"
description: "SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Returns a row for each security policy in the database."
tags: ["security", "catalog-view"]
pubDate: 2026-05-29
---

## Description

SQL Server 2016 (13.x) and later versions SQL database in Microsoft Fabric Returns a row for each security policy in the database. Name of the security policy, unique within the database. ID of the owner of the security policy, as registered to the database. NULL if the owner is determined via the schema. ID of the schema where the object resides. ID of the object to which the policy belongs. Must be 0.

## Permissions

Applies to: SQL Server 2016 (13.x) and later versions Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics SQL database in Microsoft Fabric Returns a row for each security policy in the database. Description name Name of the security policy, unique within the database. object_id ID of the security policy. principal_id ID of the owner of the security policy, as registered to the database. NULL if the owner is determined via the schema. schema_id ID of the schema where the object resides. parent_object_id ID of the object to which the policy belongs. Must be 0. type Must be . type_desc . create_date UTC date the security policy was created. modify_date UTC date the security policy was last modified. is_ms_shipped Always false. is_enabled Security policy specification state: 0 = disabled 1 = enabled is_not_for_replication Policy was created with the NOT FOR REPLICATION option. uses_database_collation Uses the same collation as the database. is_schemabinding_enabled Schemabinding state for the security policy: 0 or NULL = enabled 1 = disabled ﾉ Expand table
