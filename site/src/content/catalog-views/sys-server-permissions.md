---
name: "sys.server_permissions"
title: "sys.server_permissions"
category: "security"
description: "Returns one row for each server-level permission. Identifies class of thing on which permission exists. Description of class on which permission exists. One of the ID of the securable on which permission exists, interpreted according to class. For most, this is just the kind of ID that applies to what the class represents. Interpretation for non-standard is as Secondary ID of thing on which permis"
tags: ["security","catalog-view"]
pubDate: "2026-05-29"
syntax: |
  SELECT pr.principal_id, pr.name, pr.type_desc,
      pe.state_desc, pe.permission_name
      FROM sys.server_principals AS pr
      JOIN sys.server_permissions AS pe
      ON pe.grantee_principal_id = pr.principal_id;
---

## Description

Returns one row for each server-level permission. Identifies class of thing on which permission exists. Description of class on which permission exists. One of the ID of the securable on which permission exists, interpreted according to class. For most, this is just the kind of ID that applies to what the class represents. Interpretation for non-standard is as Secondary ID of thing on which permission exists, interpreted

## Syntax

```sql
SELECT pr.principal_id, pr.name, pr.type_desc,
pe.state_desc, pe.permission_name
FROM sys.server_principals AS pr
JOIN sys.server_permissions AS pe
ON pe.grantee_principal_id = pr.principal_id;
```

## Permissions

Article • 02/28/2023 Analytics Platform System (PDW) Returns one row for each server-level permission. Description Identifies class of thing on which permission exists. 100 = Server 101 = Server-principal 105 = Endpoint 108 = Availability Group Description of class on which permission exists. One of the following values: ID of the securable on which permission exists, interpreted according to class. For most, this is just the kind of ID that applies to what the class represents. Interpretation for non-standard is as follows: 100 = Always 0 Secondary ID of thing on which permission exists, interpreted according to class. Server-principal-ID to which the permissions are granted. Server-principal-ID of the grantor of these permissions. Server permission type. For a list of permission types, see the next table. ﾉ Expand table SQL database in Microsoft Fabric Many of the system tables from earlier releases of SQL Server are now implemented as a set of views. These views are known as compatibility views, and they are meant for backward compatibility only. The compatibility views expose the same metadata that was available in SQL Server 2000 (8.x). However, the compatibility views do not expose any of the metadata related to features that are introduced in SQL Server 2005 (9.x) and later. Therefore, when you use new features, such as Service Broker or partitioning, you must switch to using the catalog views. Another reason for upgrading to the catalog views is that compatibility view columns that store user IDs and type IDs may return NULL or trigger arithmetic overflows. This is because you can create more than 32,767 users, groups, and roles, and 32,767 data types. For example, if you were to create 32,768 users, and then run the following query:. If ARITHABORT is set to ON, the query fails with an arithmetic overflow error. If ARITHABORT is set to OFF, the column returns NULL. To avoid these problems, we recommend that you use the new catalog views that can handle the increased number of user IDs and type IDs. The following table lists the columns that are subject to this overflow. SQL Server 2005 view ﾉ Expand table

## Examples

### Example 1

```sql
SELECT pr.principal_id, pr.name, pr.type_desc,
pe.state_desc, pe.permission_name
FROM sys.server_principals AS pr
JOIN sys.server_permissions AS pe
ON pe.grantee_principal_id = pr.principal_id;
```
