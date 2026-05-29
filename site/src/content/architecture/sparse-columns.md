---
title: "Sparse Columns"
topic: "tables"
description: |
  Applies to:
  
  SQL Server 2016 (13.x) and later versions
  
  Azure SQL Database
  
  Azure
  
  SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  Sparse columns are ordinary columns that have an optimized st
tags:
  - "tables"
  - "sparse-columns"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

Sparse columns are ordinary columns that have an optimized storage for null values. Sparse

columns reduce the space requirements for null values at the cost of more overhead to retrieve

non-NULL values. Consider using sparse columns when the space saved is at least 20 percent

to 40 percent. Sparse columns and column sets are defined by using the

CREATE TABLE

or

ALTER TABLE

statements.

Sparse columns can be used with column sets and filtered indexes:

Column sets

INSERT, UPDATE, and DELETE statements can reference the sparse columns by name.

However, you can also view and work with all the sparse columns of a table that are

combined into a single XML column. This column is called a column set. For more

information about column sets, see

Use Column Sets

.

Filtered indexes

Because sparse columns have many null-valued rows, they are especially appropriate for

filtered indexes. A filtered index on a sparse column can index only the rows that have

populated values. This creates a smaller and more efficient index. For more information,

see

Create Filtered Indexes

.

Sparse columns and filtered indexes enable applications, such as Windows SharePoint Services,

to efficiently store and access a large number of user-defined properties by using SQL Server.

Sparse columns have the following characteristics:

The SQL Server Database Engine uses the SPARSE keyword in a column definition to

optimize the storage of values in that column. Therefore, when the column value is NULL

for any row in the table, the values require no storage.

Catalog views for a table that has sparse columns are the same as for a typical table. The

catalog view contains a row for each column in the table and includes a

column set if one is defined.

Sparse columns are a property of the storage layer, rather than the logical table.

Therefore a

statement does not copy over the sparse column property

```sql
sys.columns
SELECT ... INTO
```