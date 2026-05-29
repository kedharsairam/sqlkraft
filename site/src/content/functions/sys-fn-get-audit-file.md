---
name: 'sys.fn_get_audit_file'
title: 'sys.fn_get_audit_file'
category: 'system'
description: 'Azure SQL Managed Instance'
tags: ["function"]
pubDate: 2026-05-29
---

SQL Server 2019 (15.x) and earlier versions require

permission on the

server.

SQL Server 2022 (16.x) and later versions require

permission

on the server.

This example reads from a file that is named

.

SQL

For a full example about how to create an audit, see

SQL Server Audit (Database Engine)

.

Selecting rows from

within a Create Table As Select (CTAS) or

is a limitation when running on Azure Synapse Analytics. Although the query completes

successfully and no error messages appear, there are no rows present in the table created

using CTAS or

.

System catalog views:

sys.server_audit_specifications (Transact-SQL)

SQL Server

SQL Server

sys.server_audit_specification_details (Transact-SQL)

sys.database_audit_specifications (Transact-SQL)

sys.database_audit_specification_details (Transact-SQL)

Transact-SQL:

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

Create a Server Audit and Server Audit Specification

sys.dm_server_audit_status (Transact-SQL)

sys.dm_audit_actions (Transact-SQL)

sys.dm_audit_class_type_map (Transact-SQL)

sys.server_audits (Transact-SQL)

sys.server_file_audits (Transact-SQL)

Last updated on 11/18/2025

Related content

```sql
CONTROL SERVER
```

```sql
VIEW SERVER SECURITY AUDIT
```

```sql
\\serverName\Audit\HIPAA_AUDIT.sqlaudit
```

```sql
sys.fn_get_audit_file
```

```sql
INSERT
INTO
```

```sql
INSERT INTO
```

```sql
SELECT
*
FROM
sys.fn_get_audit_file(
'\\serverName\Audit\HIPAA_AUDIT.sqlaudit'
,
DEFAULT
,
DEFAULT
);
GO
```
