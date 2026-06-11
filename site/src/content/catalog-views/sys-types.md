---
name: "sys.types"
title: "sys.types"
category: "compatibility"
description: "Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each system and user-defined type."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  INNER
  JOIN
  sys.types t
  ON
  c.user_type_id = t.user_type_id
  WHERE
  object_id = object_id(
  'dbo.sample'
  );
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each system and user-defined type. Name of the type. Is unique within the schema. ID of the internal system type. ID of the type. Is unique within the database. data type is an internal data type based ID of the schema to which the type belongs. ID of the individual owner if different from schema owner. By default, schema-contained objects are owned by the schema owner. However,

## Syntax

```sql
INNER
JOIN sys.types t
ON c.user_type_id = t.user_type_id
WHERE object_id = object_id(
'dbo.sample'
);
```

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric SQL database in Microsoft Fabric Contains a row for each parameter of a partition function. Description ID of the partition function to which this parameter belongs. ID of the parameter. Is unique within the partition function, beginning with 1. ID of the system type of the parameter. Corresponds to the column of the catalog view. Maximum length of the parameter in bytes. Precision of the parameter if numeric-based; otherwise, 0. Scale of the parameter if numeric-based; otherwise, 0. Name of the collation of the parameter if character-based; otherwise, NULL. ID of the type. Is unique within the database. For system data types, = . The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . Partition Function Catalog Views (Transact-SQL) Catalog Views (Transact-SQL) sys.partition_functions (Transact-SQL) sys.partition_range_values (Transact-SQL) ﾉ Expand table See Also SQL Server 2005 view When referenced in a user database, system tables which were announced as deprecated in SQL Server 2000 (such as or ), are now bound to the back- compatibility view in the schema. Since the SQL Server 2000 system tables have been deprecated for multiple versions, this change is not considered a breaking change. Example: If a user creates a user-table called in a user-database, in SQL Server 2008, the statement in that database would return the values from the user table. Beginning in SQL Server 2012, this practice will return data from the system view . Catalog Views (Transact-SQL) Mapping System Tables to System Views (Transact-SQL) Last updated on 11/18/2025 See Also
