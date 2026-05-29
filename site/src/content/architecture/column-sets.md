---
title: "Column Sets"
topic: "tables"
description: |
  Applies to:
  
  SQL Server 2016 (13.x) and later versions
  
  Azure SQL Database
  
  Azure SQL Managed
  
  Instance
  
  SQL database in Microsoft Fabric
  
  Tables that use sparse columns can designate a column set to 
tags:
  - "tables"
  - "column-sets"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure SQL Managed

Instance

SQL database in Microsoft Fabric

Tables that use sparse columns can designate a column set to return all sparse columns in the table. A column

set is an untyped XML representation that combines all the sparse columns of a table into a structured output.

A column set is like a calculated column in that the column set is not physically stored in the table. A column

set differs from a calculated column in that the column set is directly updatable.

You should consider using column sets when the number of columns in a table is large, and operating on them

individually is cumbersome. Applications might see some performance improvement when they select and

insert data by using column sets on tables that have lots of columns. However, the performance of column sets

can be reduced when many indexes are defined on the columns in the table. This is because the amount of

memory that is required for an execution plan increases.

To define a column set, use the

keywords in the

CREATE TABLE

or

ALTER TABLE

statements.

When you use column sets, consider the following guidelines:

Sparse columns and a column set can be added as part of the same statement.

A column set cannot be added to a table if that table already contains sparse columns.

The column set column cannot be changed or renamed. To change a column set, you must delete and re-

create the sparse columns and the column set. Columns with the SPARSE keyword can be added and

dropped from the table.

A column set can be added to a table that does not include any sparse columns. If sparse columns are

later added to the table, they will appear in the column set.

Only one column set is allowed per table.

A column set is optional and is not required to use sparse columns.

Constraints or default values cannot be defined on a column set.

Computed columns cannot contain column set columns.

Distributed queries are not supported on tables that contain column sets.

Replication does not support column sets.

Change data capture does not support column sets.

A column set cannot be part of any kind of index. This includes XML indexes, full-text indexes, and

indexed views. A column set cannot be added as an included column in any index.

A column set cannot be used in the filter expression of a filtered index or filtered statistics.

```sql
*<column_set_name>* FOR ALL_SPARSE_COLUMNS
```