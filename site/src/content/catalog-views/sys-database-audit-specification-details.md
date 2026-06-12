---
name: "sys.database_audit_specification_details"
title: "sys.database_audit_specification_details"
category: "compatibility"
description: "Contains information about the database audit specifications in a SQL Server audit on a server instance for all databases. For more information, see SQL Server Audit (Database Engine) list of all audit_action_id's and their names, query sys.dm_audit_actions (Transact-SQL) ID of the audit specification."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

Contains information about the database audit specifications in a SQL Server audit on a server instance for all databases. For more information, see SQL Server Audit (Database Engine) list of all audit_action_id's and their names, query sys.dm_audit_actions (Transact-SQL) ID of the audit specification.

## Permissions

sys.database_audit_specification_details sys.database_ledger_transactions sys.database_ledger_blocks sys.ledger_table_history sys.ledger_column_history sys.database_ledger_digest_locations The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration. Security Center for SQL Server Database Engine and Azure SQL Database Security-Related Dynamic Management Views and Functions (Transact-SQL) See Also sys.database_audit_specifications (Transact-SQL) sys.database_audit_specification_details (Transact-SQL) sys.dm_server_audit_status (Transact-SQL) sys.dm_audit_actions (Transact-SQL) sys.dm_audit_class_type_map (Transact-SQL) Create a Server Audit and Server Audit Specification sys.server_audit_specification_details (Transact-SQL) sys.database_audit_specifications (Transact-SQL) sys.database_audit_specification_details (Transact-SQL) Transact-SQL: CREATE SERVER AUDIT (Transact-SQL) ALTER SERVER AUDIT (Transact-SQL) DROP SERVER AUDIT (Transact-SQL) CREATE SERVER AUDIT SPECIFICATION (Transact-SQL) ALTER SERVER AUDIT SPECIFICATION (Transact-SQL) DROP SERVER AUDIT SPECIFICATION (Transact-SQL) CREATE DATABASE AUDIT SPECIFICATION (Transact-SQL) ALTER DATABASE AUDIT SPECIFICATION (Transact-SQL) DROP DATABASE AUDIT SPECIFICATION (Transact-SQL) ALTER AUTHORIZATION (Transact-SQL) Create a Server Audit and Server Audit Specification sys.dm_server_audit_status (Transact-SQL) sys.dm_audit_actions (Transact-SQL) sys.dm_audit_class_type_map (Transact-SQL) sys.server_audits (Transact-SQL) sys.server_file_audits (Transact-SQL)
