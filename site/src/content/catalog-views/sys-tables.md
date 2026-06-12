---
name: "sys.tables"
title: "sys.tables"
category: "objects"
description: "SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric SQL database in Microsoft Fabric Catalog views return information that is used by the SQL Server Database Engine."
tags: ["objects", "catalog-view"]
pubDate: 2026-05-29
syntax: "filestream_data_space_id"
---

## Description

Analytics Platform System (PDW) SQL analytics endpoint in Microsoft Fabric Warehouse in Microsoft Fabric SQL database in Microsoft Fabric Catalog views return information that is used by the SQL Server Database Engine. We recommend that you use catalog views because they are the most general interface to the catalog metadata, and provide the most efficient way to obtain, transform, and present customized forms of this information. All user-available catalog metadata is exposed through Some catalog views inherit rows from other catalog views. For example, the view inherits from the catalog view. The catalog view is referred to as the base view, and the view is called the derived view.

## Syntax

`filestream_data_space_id`

## Remarks

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in Microsoft Fabric

Catalog views return information that is used by the SQL Server Database Engine. We

recommend that you use catalog views because they are the most general interface to the

catalog metadata, and provide the most efficient way to obtain, transform, and present

customized forms of this information. All user-available catalog metadata is exposed through

catalog views.

Some catalog views inherit rows from other catalog views. For example, the

view inherits from the

sys.objects

catalog view. The

catalog view is referred to as

the base view, and the

view is called the derived view. The

catalog view

returns the columns that are specific to tables and also all the columns that the

catalog view returns. The

catalog view returns rows for objects other than tables,

such as stored procedures and views. After a table is created, the metadata for the table is

returned in both views. Although the two catalog views return different levels of information

about the table, there is only one entry in metadata for this table with one name and one. This can be summarized as follows:

The base view contains a subset of columns and a superset of rows.

The derived view contains a superset of columns and a subset of rows.

The catalog views in SQL Server have been organized into the following categories:

Catalog views do not contain information about replication, backup, database

maintenance plan, or SQL Server Agent catalog data.

In future releases of SQL Server, Microsoft may augment the definition of any system

catalog view by adding columns to the end of the column list. We recommend against

using the syntax

in production code because the

number of columns returned might change and break your application.

## Examples

### Example 1

```sql
SELECT tbl.name as table_name, c.name AS column_name, c.is_masked,
c.masking_function
FROM sys.masked_columns AS c
JOIN sys.tables AS tbl
ON c.object_id = tbl.object_id
WHERE is_masked = 1;
```

### Example 2

```sql
ON fkc.constraint_object_id = fk.object_id
INNER
JOIN sys.tables t_parent
ON t_parent.object_id = fk.parent_object_id
INNER
JOIN sys.columns c_parent
ON fkc.parent_column_id = c_parent.column_id
AND c_parent.object_id = t_parent.object_id
INNER
JOIN sys.tables t_child
ON t_child.object_id = fk.referenced_object_id
INNER
JOIN sys.columns c_child
ON c_child.object_id = t_child.object_id
AND fkc.referenced_column_id = c_child.column_id
ORDER
BY t_parent.name, c_parent.name;
```
