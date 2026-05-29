---
name: 'sys.server_audit_specifications'
title: 'sys.server_audit_specifications (Transact-'
category: 'objects'
description: 'Azure SQL Managed Instance'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

SQL)

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Managed Instance

Contains information about the server audit specifications in a SQL Server audit on a server

instance. For more information on SQL Server Audit, see

SQL Server Audit (Database Engine)

.


## Description
Name of the server specification.

ID of the

.

Date the audit server specification was created.

Date the audit server specification was last modified.

Audit specification state:

0 - DISABLED

1 -ENABLED

GUID for the audit that contains this specification. Used

during enumeration of member server audit specifications

during server startup.

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

ﾉ

Expand table

See Also

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

sys.server_audit_specification_details (Transact-SQL)

sys.database_audit_specifications (Transact-SQL)

sys.database_audit_specification_details (Transact-SQL)

sys.dm_server_audit_status (Transact-SQL)

sys.dm_audit_actions (Transact-SQL)

sys.dm_audit_class_type_map (Transact-SQL)

Create a Server Audit and Server Audit Specification
