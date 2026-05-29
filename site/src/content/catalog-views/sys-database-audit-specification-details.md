---
name: 'sys.database_audit_specification_details'
title: 'sys.database_audit_specification_details'
category: 'objects'
description: 'role, and members of the'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Principals with the

or


## permissions, the
role, and members of the

fixed database role have access to this catalog view. In

addition, the principal must not be denied

permission.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

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

sys.server_audit_specification_details (Transact-SQL)

sys.database_audit_specifications (Transact-SQL)

sys.dm_server_audit_status (Transact-SQL)

sys.dm_audit_actions (Transact-SQL)

sys.dm_audit_class_type_map (Transact-SQL)

Create a Server Audit and Server Audit Specification

See Also
