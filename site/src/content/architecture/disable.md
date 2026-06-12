---
title: "Disable"
topic: "filestream"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  This article describes how to disable an index or constraints in SQL Server by using SQL Serv
tags:
  - "filestream"
  - "disable"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

This article describes how to disable an index or constraints in SQL Server by using SQL Server

Management Studio or Transact-SQL. Disabling an index prevents user access to the index, and

for clustered indexes to the underlying table data. The index definition remains in metadata,

and index statistics are kept on nonclustered indexes. Disabling a clustered index on a view or a

nonclustered index physically deletes the index data.

Disabling a clustered index on a table prevents access to the data. The data still remains in the

table, but is unavailable for data manipulation language (DML) operations until the index is

dropped or rebuilt.

The index isn't maintained while it's disabled.

The query optimizer doesn't consider the disabled index when creating query execution plans.

Also, queries that reference the disabled index with a table hint fail.

You can't create an index that uses the same name as an existing disabled index.

A disabled index can be dropped.

When you disable a unique index, the

or

constraint and all

constraints that reference the indexed columns from other tables are also disabled. When you

disable a clustered index, all incoming and outgoing

constraints on the underlying

table are also disabled. The constraint names are listed in a warning message when the index is

disabled. After you rebuild the index, all constraints must be manually enabled by using the

statement.

Nonclustered indexes are automatically disabled when the associated clustered index is

disabled. They can't be enabled until either the clustered index on the table or view is enabled

or the clustered index on the table is dropped. Nonclustered indexes must be explicitly

enabled, unless the clustered index was enabled by using the

statement.

The

statement rebuilds and enables all disabled indexes on the table,

except for disabled indexes on views. Indexes on views must be enabled in a separate

statement.

```sql
PRIMARY KEY
UNIQUE
FOREIGN KEY
FOREIGN KEY
ALTER TABLE CHECK CONSTRAINT
ALTER INDEX ALL REBUILD
ALTER INDEX ALL REBUILD
ALTER
INDEX ALL REBUILD
```
