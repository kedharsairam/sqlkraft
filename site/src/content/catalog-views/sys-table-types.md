---
name: "sys.table_types"
title: "sys.table_types"
category: "compatibility"
description: "SQL database in Microsoft Fabric Displays properties of user-defined table types in SQL Server. A table type is a type from which table variables or table-valued parameters could be declared. Each table type has a that is a foreign key into the catalog view."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
---

## Description

SQL database in Microsoft Fabric Displays properties of user-defined table types in SQL Server. A table type is a type from which table variables or table-valued parameters could be declared. Each table type has a that is a foreign key into the catalog view. You can use this ID column to query various catalog views, in a way that is similar to an regular table, to discover the structure of the table type such as its columns and constraints.

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric Displays properties of user-defined table types in SQL Server. A table type is a type from which table variables or table-valued parameters could be declared. Each table type has a that is a foreign key into the sys.objects catalog view. You can use this ID column to query various catalog views, in a way that is similar to an column of a regular table, to discover the structure of the table type such as its columns and constraints. Description <inherited columns> For a list of columns that this view inherits, see sys.types (Transact- SQL) . Object identification number. This number is unique within a database. : SQL Server 2014 (12.x) and later. The following are the possible values: 0 = is not memory optimized 1 = is memory optimized A value of 0 is the default value. Table types are always created with DURABILITY = SCHEMA_ONLY. Only the schema is persisted on disk. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . ﾉ Expand table See Also
