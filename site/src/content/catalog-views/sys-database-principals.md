---
name: "sys.database_principals"
title: "sys.database_principals"
category: "compatibility"
description: "Returns a row for each security principal in a SQL Server database."
tags: ["compatibility","catalog-view"]
pubDate: 2026-05-29
syntax: |
  SELECT pr.principal_id, pr.name, pr.type_desc,
              pr.authentication_type_desc, pe.state_desc, pe.permission_name
              FROM sys.database_principals AS pr
              JOIN sys.database_permissions AS pe
              ON pe.grantee_principal_id = pr.principal_id;
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns a row for each security principal in a SQL Server database.

## Syntax

```sql
SELECT pr.principal_id, pr.name, pr.type_desc,
pr.authentication_type_desc, pe.state_desc, pe.permission_name
FROM sys.database_principals AS pr
JOIN sys.database_permissions AS pe
ON pe.grantee_principal_id = pr.principal_id;
```

## Permissions

The following query lists the permissions explicitly granted or denied to database principals. The following query joins sys.database_principals and sys.database_permissions to sys.objects and sys.schemas to list permissions granted or denied to specific schema objects. ） Important The permissions of fixed database roles do not appear in sys.database_permissions. Therefore, database principals may have additional permissions not listed here. The following query lists the permissions explicitly granted or denied to database principals. The following query joins and to and to list permissions granted or denied to specific schema objects. Principals (Database Engine) sys.server_principals (Transact-SQL) Security Catalog Views (Transact-SQL) Contained Database Users - Making Your Database Portable Connecting to Azure SQL with Microsoft Entra authentication ） Important The permissions of fixed database roles do not appear in. Therefore, database principals may have additional permissions not listed here. See Also SQL Server 2005 view When referenced in a user database, system tables which were announced as deprecated in SQL Server 2000 (such as or ), are now bound to the back- compatibility view in the schema. Since the SQL Server 2000 system tables have been deprecated for multiple versions, this change is not considered a breaking change. Example: If a user creates a user-table called in a user-database, in SQL Server 2008, the statement in that database would return the values from the user table. Beginning in SQL Server 2012, this practice will return data from the system view. Catalog Views (Transact-SQL) Mapping System Tables to System Views (Transact-SQL) See Also Specifies the first schema that will be searched by the server when it resolves the names of objects. schema_name can be a schema that doesn't exist in the database. If the new application role name already exists in the database, the statement fails. When the name, password, or default schema of an application role is changed the ID associated with the role isn't changed. Application roles are visible in the catalog view. Beginning with SQL Server 2012 (11.x), SQL Server and Azure SQL DB used a SHA-512 hash combined with a 32-bit random and unique salt. This method made it statistically infeasible for attackers to deduce passwords. SQL Server 2025 (17.x) Preview introduces an iterated hash algorithm, RFC2898, also known as a password-based key derivation function (PBKDF). This algorithm still uses SHA-512 but hashes the password multiple times (100,000 iterations), significantly slowing down brute-force attacks. This change enhances password protection in response to evolving security threats and helps customers comply with NIST SP 800-63b guidelines. This security enhancement uses a stronger hashing algorithm, which may slightly increase login time for SQL Authentication logins. The impact is generally negligible in environments with connection pooling, but may be more noticeable in scenarios without pooling or where login latency is closely monitored. Requires ALTER ANY APPLICATION ROLE permission on the database. To change the default schema, the user also needs ALTER permission on the application role. An application role can alter its own default schema, but not its name or password. ） Important Password expiration policy isn't applied to application role passwords. For this reason, take extra care in selecting strong passwords. Applications that invoke application roles must store their passwords. ７ Note Schemas aren't equivalent to database users. Use to identify any differences between database users and schemas. Information about database principals is visible in the sys.database_principals catalog view. Information about database-level permissions is visible in the sys.database_permissions catalog view. A database user is a database-level securable contained by the database that is its parent in the permissions hierarchy. The most specific and limited permissions that can be granted on a database user are listed in the following table, together with the more general permissions that include them by implication. CONTROL CONTROL CONTROL IMPERSONATE CONTROL CONTROL ALTER CONTROL ALTER ANY USER VIEW DEFINITION CONTROL VIEW DEFINITION A database role is a database-level securable contained by the database that is its parent in the permissions hierarchy. The most specific and limited permissions that can be granted on a database role are listed in the following table, together with the more general permissions that include them by implication. CONTROL CONTROL CONTROL TAKE OWNERSHIP CONTROL CONTROL ALTER CONTROL ALTER ANY ROLE VIEW DEFINITION CONTROL VIEW DEFINITION ﾉ Expand table ﾉ Expand table SQL sys.database_permissions (Transact-SQL) sys.database_principals (Transact-SQL) GRANT Database Permissions (Transact-SQL) DENY Database Permissions (Transact-SQL) Permissions (Database Engine) Principals (Database Engine) See Also GRANT Database Principal Permissions (Transact-SQL) DENY Database Principal Permissions (Transact-SQL) sys.database_principals (Transact-SQL) sys.database_permissions (Transact-SQL) CREATE USER (Transact-SQL) CREATE APPLICATION ROLE (Transact-SQL) CREATE ROLE (Transact-SQL) GRANT (Transact-SQL) Permissions (Database Engine) Principals (Database Engine) See Also

## Examples

### Example 1

`weekly_receipts`

### Example 2

```sql
987Gbv876sPYY5m23
```

### Example 3

`Sales`

### Example 4

```sql
CREATE
APPLICATION
ROLE weekly_receipts
WITH
PASSWORD
=
'987G^bv876sPY)Y5m23'
, DEFAULT_SCHEMA = Sales;
GO
```
