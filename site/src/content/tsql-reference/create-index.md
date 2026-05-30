---
name: "CREATE INDEX"
title: "CREATE INDEX"
category: "statements"
description: "Azure SQL Managed Instance"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

### Examples:

### Server and Azure SQL index architecture and design guide

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

Creates a relational index on a table or view. Also called a rowstore index because it is either a

clustered or nonclustered B-tree index. You can create a rowstore index before there is data in

the table. Use a rowstore index to improve query performance, especially when the queries

select from specific columns or require values to be sorted in a particular order.

Azure Synapse Analytics and Analytics Platform System (PDW) currently don't support unique

constraints. Any examples referencing unique constraints are only applicable to SQL Server,

Azure SQL Database, SQL database in Microsoft Fabric, and Azure SQL Managed Instance.

For information on index design guidelines, refer to the

SQL Server index design guide

.

1. Create a nonclustered index on a table or view

2. Create a clustered index on a table and use a 3-part name for the table

3. Create a nonclustered index with a unique constraint and specify the sort order

７

Note

Documentation uses the term B-tree generally in reference to indexes. In rowstore

indexes, the Database Engine implements a B+ tree. This does not apply to columnstore

indexes or indexes on memory-optimized tables. For more information, see the

.

### Key scenario:

```sql
CREATE
INDEX index1
ON schema1.table1 (column1);
CREATE
CLUSTERED
INDEX index1
ON database1.schema1.table1 (column1);
CREATE
UNIQUE
INDEX index1
ON schema1.table1 (column1
DESC
, column2
ASC
,
column3
DESC
);
```
