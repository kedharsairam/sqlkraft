---
name: "sys.server_audit_specification_details"
title: "sys.server_audit_specification_details"
category: "compatibility"
description: "Contains information about the server audit specification details (actions) in a SQL Server audit on a server instance. For more information, see SQL Server Audit (Database Engine) all audit_action_id's and their names, query sys.dm_audit_actions (Transact-SQL) ID of the audit server specification Name of group or name of audit action Whether the audited object is a group:"
tags: ["compatibility","catalog-view"]
pubDate: "2026-05-29"
---

## Description

Contains information about the server audit specification details (actions) in a SQL Server audit on a server instance. For more information, see SQL Server Audit (Database Engine) all audit_action_id's and their names, query sys.dm_audit_actions (Transact-SQL) ID of the audit server specification Name of group or name of audit action Whether the audited object is a group:

## Permissions

Article • 02/28/2023 Contains information about the server audit specification details (actions) in a SQL Server audit on a server instance. For more information, see SQL Server Audit (Database Engine). For a list of all audit_action_id's and their names, query sys.dm_audit_actions (Transact-SQL). Description server_specification_id ID of the audit server specification audit_action_id ID of the audit action audit_action_name Name of group or name of audit action class Reserved class_desc Reserved major_id Reserved minor_id Reserved audited_principal_id Reserved audited_result Audited result: - SUCCESS AND FAILURE - SUCCESS - FAILURE is_group Whether the audited object is a group: 0 - Not a group 1 - Group ﾉ Expand table sys.server_audit_specification_details (Transact-SQL) sys.database_audit_specifications (Transact-SQL) sys.database_audit_specification_details (Transact-SQL) Transact-SQL: CREATE SERVER AUDIT (Transact-SQL) ALTER SERVER AUDIT (Transact-SQL) DROP SERVER AUDIT (Transact-SQL) CREATE SERVER AUDIT SPECIFICATION (Transact-SQL) ALTER SERVER AUDIT SPECIFICATION (Transact-SQL) DROP SERVER AUDIT SPECIFICATION (Transact-SQL) CREATE DATABASE AUDIT SPECIFICATION (Transact-SQL) ALTER DATABASE AUDIT SPECIFICATION (Transact-SQL) DROP DATABASE AUDIT SPECIFICATION (Transact-SQL) ALTER AUTHORIZATION (Transact-SQL) Create a Server Audit and Server Audit Specification sys.dm_server_audit_status (Transact-SQL) sys.dm_audit_actions (Transact-SQL) sys.dm_audit_class_type_map (Transact-SQL) sys.server_audits (Transact-SQL) sys.server_file_audits (Transact-SQL)
