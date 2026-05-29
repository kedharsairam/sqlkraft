---
name: 'sys.server_audits'
title: 'sys.server_audits'
category: 'objects'
description: 'SHUTDOWN SERVER INSTANCE'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
CONTINUE

SHUTDOWN SERVER INSTANCE

FAIL_OPERATION

0 - Disabled

1 - Enabled

Maximum time, in milliseconds, to wait before writing to disk. If 0,

the audit will guarantee a write before an event can continue.

The predicate expression that is applied to the event.

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

sys.server_file_audits (Transact-SQL)

sys.server_audit_specifications (Transact-SQL)

sys.server_audit_specification_details (Transact-SQL)

See Also

sys.database_audit_specifications (Transact-SQL)

sys.database_audit_specification_details (Transact-SQL)

sys.dm_server_audit_status (Transact-SQL)

sys.dm_audit_actions (Transact-SQL)

sys.dm_audit_class_type_map (Transact-SQL)

Create a Server Audit and Server Audit Specification
