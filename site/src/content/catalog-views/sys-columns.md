---
name: "sys.columns"
title: "sys.columns"
category: "objects"
description: "Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns a row for each column of an object that has columns, such as views or tables. The following list contains the object types that have columns: Table-valued assembly functions (FT) Inline table-valued SQL functions (IF) Table-valued SQL functions (TF) ID of the object to which this column belongs. Name of the column. Is unique "
tags: ["objects", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  sp_tableoption
  'text in row'
---

## Description

Analytics Platform System (PDW) SQL database in Microsoft Fabric Returns a row for each column of an object that has columns, such as views or tables. The following list contains the object types that have columns: Table-valued assembly functions (FT) Inline table-valued SQL functions (IF) Table-valued SQL functions (TF) ID of the object to which this column belongs. Name of the column. Is unique within the object.

## Syntax

```sql
sp_tableoption
'text in row'
```

## Arguments

Applies to:

Azure SQL Database

Azure SQL Managed Instance

This function returns column or parameter information.

Transact-SQL syntax conventions

containing the identifier (ID) of the table or procedure.

An expression containing the name of the column or parameter.

argument, the

argument specifies the information type that the

function will return. The

argument can have any one of these values:

Description

Allows null values.

NULL: invalid input.

Column ID value corresponding to

When querying

multiple columns, gaps

may appear in the

sequence of Column

Expand table

Description

The TYPE COLUMN in the table holding the document

type information of the

ID of the full-text TYPE

COLUMN for the

column name

expression passed as

the second parameter

of this function.

Is column value system-generated. Corresponds to

: SQL Server

2016 (13.x) and later.

0: Not generated

1: Generated always at

2: Generated always at

Column is a column set. For more information, see

Column Sets

NULL: invalid input.

Column is a computed column.

NULL: invalid input.

Procedure parameter is of type CURSOR.

NULL: invalid input.

Column is deterministic. This property applies only to

computed columns and view columns.

NULL: invalid input.

Not a computed

column or view

Column is registered for full-text indexing.

Description

NULL: invalid input.

_(... and 20 more arguments)_

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each column found in that is a computed-column. Description The view returns all columns in the view. It also returns the additional columns described below. For a description of the columns that the view inherits from , see sys.columns (Transact-SQL) . The value of the column is always set to 1 in the view. SQL text that defines this computed-column. 1 = The column definition depends on the default collation of the database for correct evaluation; otherwise, 0. Such a dependency prevents changing the database default collation. Computed column is persisted. The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . Object Catalog Views (Transact-SQL) Catalog Views (Transact-SQL) Last updated on 11/18/2025 ﾉ Expand table See Also Object Catalog Views (Transact-SQL) Catalog Views (Transact-SQL) Querying the SQL Server System Catalog FAQ Last updated on 11/18/2025 See also Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) SQL database in Microsoft Fabric Contains a row for each column that is an identity column. The view inherits rows from the view. The view returns the columns in the view, plus the , , , and columns. For more information, see Catalog Views (Transact-SQL) . Description The view returns all columns in the view. It also returns the additional columns described below. For a description of the columns that the view inherits from , see sys.columns (Transact-SQL) . sql_variant Seed value for this identity column. The data type of the seed value is the same as the data type of the column itself. sql_variant Increment value for this identity column. The data type of the seed value is the same as the data type of the column itself. sql_variant Last value generated for this identity column. The data type of the seed value is the same as the data type of the column itself. Identity column is declared NOT FOR REPLICATION. Note: This column does not apply to Azure Synapse Analytics. ﾉ Expand table ７ Note To create an automatically incrementing number that can be used in multiple tables or that can be called from applications without referencing any table, see . Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric SQL database in Microsoft Fabric Contains a row for each column that is part of statistics. Description ID of the object of which this column is part. ID of the statistics of which this column is part. If statistics correspond to an index, the stats_id value is the same as the index_id value in the sys.indexes catalog view. 1-based ordinal within set of stats columns. ID of the column from . The visibility of the metadata in catalog views is limited to securables that a user either owns, or on which the user was granted some permission. For more information, see Metadata Visibility Configuration . Object Catalog Views (Transact-SQL) Catalog Views (Transact-SQL) Querying the SQL Server System Catalog FAQ Statistics sys.dm_db_stats_properties (Transact-SQL) sys.dm_db_stats_histogram (Transact-SQL) sys.stats (Transact-SQL) Statistics in Microsoft Fabric Last updated on 11/18/2025 ﾉ Expand table See Also System catalog views (Transact-SQL) Querying the SQL Server System Catalog FAQ sys.columns (Transact-SQL) sys.all_columns (Transact-SQL) sys.computed_columns (Transact-SQL) Last updated on 11/28/2025 Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance Azure Synapse Analytics Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric SQL database in Microsoft Fabric Many of the system tables from earlier releases of SQL Server are now implemented as a set of views. These views are known as compatibility views, and they are meant for backward compatibility only. The compatibility views expose the same metadata that was available in SQL Server 2000 (8.x). However, the compatibility views do not expose any of the metadata related to features that are introduced in SQL Server 2005 (9.x) and later. Therefore, when you use new features, such as Service Broker or partitioning, you must switch to using the catalog views. Another reason for upgrading to the catalog views is that compatibility view columns that store user IDs and type IDs may return NULL or trigger arithmetic overflows. This is because you can create more than 32,767 users, groups, and roles, and 32,767 data types. For example, if you were to create 32,768 users, and then run the following query: . If ARITHABORT is set to ON, the query fails with an arithmetic overflow error. If ARITHABORT is set to OFF, the column returns NULL. To avoid these problems, we recommend that you use the new catalog views that can handle the increased number of user IDs and type IDs. The following table lists the columns that are subject to this overflow. SQL Server 2005 view ﾉ Expand table Columnstore Index Architecture Querying the SQL Server System Catalog FAQ sys.columns sys.all_columns sys.computed_columns sys.column_store_dictionaries sys.column_store_segments Last updated on 11/18/2025 System Views (Transact-SQL) Information Schema Views (Transact-SQL) sys.columns (Transact-SQL) sys.objects (Transact-SQL) sys.types (Transact-SQL) sys.check_constraints (Transact-SQL) sys.key_constraints (Transact-SQL) sys.foreign_keys (Transact-SQL) Last updated on 11/18/2025 System Views (Transact-SQL) Information Schema Views (Transact-SQL) sys.columns (Transact-SQL) sys.indexes (Transact-SQL) sys.objects (Transact-SQL) sys.foreign_keys (Transact-SQL) sys.key_constraints (Transact-SQL) SQL SQL Permissions (Database Engine) Securables Permissions Hierarchy (Database Engine) sys.fn_builtin_permissions (Transact-SQL) Security Catalog Views (Transact-SQL) Last updated on 11/18/2025 See Also
