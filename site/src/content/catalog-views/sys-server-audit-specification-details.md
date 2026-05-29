---
name: 'sys.server_audit_specification_details'
title: 'sys.server_audit_specification_details'
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

Azure SQL Managed Instance

Contains information about the server audit specification details (actions) in a SQL Server audit

on a server instance. For more information, see

SQL Server Audit (Database Engine)

. For a list of

all audit_action_id's and their names, query

sys.dm_audit_actions (Transact-SQL)

.


## Description
server_specification_id

ID of the audit server specification

audit_action_id

ID of the audit action

audit_action_name

Name of group or name of audit action

class

Reserved

class_desc

Reserved

major_id

Reserved

minor_id

Reserved

audited_principal_id

Reserved

audited_result

Audited result:

- SUCCESS AND FAILURE

- SUCCESS

- FAILURE

is_group

Whether the audited object is a group:

0 - Not a group

1 - Group

ﾉ

Expand table

Principals with the

or

permission have

access to this catalog view. In addition, the principal must not be denied

permission.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Security Catalog Views (Transact-SQL)

CREATE SERVER AUDIT (Transact-SQL)

ALTER SERVER AUDIT (Transact-SQL)

DROP SERVER AUDIT (Transact-SQL)

CREATE SERVER AUDIT SPECIFICATION (Transact-SQL)

ALTER SERVER AUDIT SPECIFICATION (Transact-SQL)

DROP SERVER AUDIT SPECIFICATION (Transact-SQL)

CREATE DATABASE AUDIT SPECIFICATION (Transact-SQL)

ALTER DATABASE AUDIT SPECIFICATION (Transact-SQL)

DROP DATABASE AUDIT SPECIFICATION (Transact-SQL)

ALTER AUTHORIZATION (Transact-SQL)

sys.fn_get_audit_file (Transact-SQL)

sys.server_audits (Transact-SQL)

sys.server_file_audits (Transact-SQL)

sys.server_audit_specifications (Transact-SQL)

sys.database_audit_specifications (Transact-SQL)

sys.database_audit_specification_details (Transact-SQL)

sys.dm_server_audit_status (Transact-SQL)

sys.dm_audit_actions (Transact-SQL)

sys.dm_audit_class_type_map (Transact-SQL)

Create a Server Audit and Server Audit Specification

See Also
