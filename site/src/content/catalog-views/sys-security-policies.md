---
name: 'sys.security_policies'
title: 'sys.security_policies'
category: 'security'
description: 'SQL Server 2016 (13.x) and later versions'
tags: ["catalog-view", "security"]
pubDate: 2026-05-29
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

Azure Synapse Analytics

SQL database in Microsoft Fabric


## Returns a row for each security policy in the database.

## Description
name

Name of the security policy, unique within the database.

object_id

ID of the security policy.

principal_id

ID of the owner of the security policy, as registered to the

database. NULL if the owner is determined via the schema.

schema_id

ID of the schema where the object resides.

parent_object_id

ID of the object to which the policy belongs. Must be 0.

type

Must be

.

type_desc

.

create_date

UTC date the security policy was created.

modify_date

UTC date the security policy was last modified.

is_ms_shipped

Always false.

is_enabled

Security policy specification state:

0 = disabled

1 = enabled

is_not_for_replication

Policy was created with the NOT FOR REPLICATION option.

uses_database_collation

Uses the same collation as the database.

is_schemabinding_enabled

Schemabinding state for the security policy:

0 or NULL = enabled

1 = disabled

ﾉ

Expand table

Principals with the

permission have access to all objects in this

catalog view as well as anyone with

on the object.

Row-Level Security

sys.security_predicates (Transact-SQL)

CREATE SECURITY POLICY (Transact-SQL)

Security Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

Principals (Database Engine)

Last updated on 11/18/2025

See Also
