---
name: 'sys.foreign_key_columns'
title: 'sys.foreign_key_columns'
category: 'objects'
description: 'Azure SQL Managed Instance'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

Warehouse in Microsoft

Fabric

SQL database in Microsoft Fabric

Contains a row for each column, or set of columns, that comprise a foreign key.


## Description
ID of the FOREIGN KEY constraint.

ID of the column, or set of columns, that comprise the FOREIGN KEY

(

1..n

where n is the number of columns).

ID of the parent of the constraint, which is the referencing object.

ID of the parent column, which is the referencing column.

ID of the referenced object, which has the candidate key.

ID of the referenced column (candidate key column).

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

The following Transact-SQL query retrieves all foreign keys in the database, including their

related tables and columns.

SQL

ﾉ

Expand table

Object Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

Querying the SQL Server System Catalog FAQ

Last updated on 11/18/2025

See also

```sql
SELECT
fk.name
AS
ForeignKeyName
, t_parent.name
AS
ParentTableName
, c_parent.name
AS
ParentColumnName
, t_child.name
AS
ReferencedTableName
, c_child.name
AS
ReferencedColumnName
FROM
sys.foreign_keys fk
INNER
JOIN
sys.foreign_key_columns fkc
```

```sql
ON
fkc.constraint_object_id = fk.object_id
INNER
JOIN
sys.tables t_parent
ON
t_parent.object_id = fk.parent_object_id
INNER
JOIN
sys.columns c_parent
ON
fkc.parent_column_id = c_parent.column_id
AND
c_parent.object_id = t_parent.object_id
INNER
JOIN
sys.tables t_child
ON
t_child.object_id = fk.referenced_object_id
INNER
JOIN
sys.columns c_child
ON
c_child.object_id = t_child.object_id
AND
fkc.referenced_column_id = c_child.column_id
ORDER
BY
t_parent.name, c_parent.name;
```
