---
name: "sys.schemas"
title: "Schemas - sys.schemas"
category: "compatibility"
description: "Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Contains a row for each database schema."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  SELECT pr.principal_id, pr.name, pr.type_desc,
  pr.authentication_type_desc, pe.state_desc, pe.permission_name
  FROM sys.database_principals AS pr
  JOIN sys.database_permissions AS pe
  ON pe.grantee_principal_id = pr.principal_id;
---

## Description

Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Contains a row for each database schema. Name of the schema. Is unique within the database. ID of the schema. Is unique within the database. ID of the principal that owns this schema. Database schemas act as namespaces or containers for objects, such as tables, views, procedures, and functions, that can be found in the Each schema has an owner. The owner is a security

## Syntax

```sql
SELECT pr.principal_id, pr.name, pr.type_desc,
pr.authentication_type_desc, pe.state_desc, pe.permission_name
FROM sys.database_principals AS pr
JOIN sys.database_permissions AS pe
ON pe.grantee_principal_id = pr.principal_id;
```

## Permissions

Article • 07/19/2024 Applies to: SQL Server Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric Contains a row for each database schema. Description Name of the schema. Is unique within the database. ID of the schema. Is unique within the database. ID of the principal that owns this schema. Database schemas act as namespaces or containers for objects, such as tables, views, procedures, and functions, that can be found in the catalog view. Each schema has an owner. The owner is a security principal . Requires membership in the role. Principals (Database Engine) System catalog views (Transact-SQL) sys.objects (Transact-SQL) ７ Note Database schemas are different from XML schemas, which are used to define the content model of XML documents. ﾉ Expand table Related content The following query lists the permissions explicitly granted or denied to database principals. The following query joins sys.database_principals and sys.database_permissions to sys.objects and sys.schemas to list permissions granted or denied to specific schema objects. ） Important The permissions of fixed database roles do not appear in sys.database_permissions. Therefore, database principals may have additional permissions not listed here. sys.schemas (Transact-SQL) sys.syscharsets (Transact-SQL) Last updated on 11/18/2025

## Examples

### Example 1

`CountBy1`

### Example 2

```sql
SELECT sch.name +
'.'
+ seq.name
AS
[
Sequence schema and name
]
FROM sys.sequences
AS seq
JOIN sys.schemas
AS sch
ON seq.schema_id = sch.schema_id ;
GO
```

### Example 3

```sql
DROP
SEQUENCE
CountBy1 ;
GO
```
