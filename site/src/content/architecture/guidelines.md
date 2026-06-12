---
title: "Guidelines"
topic: "filestream"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  When you perform online index operations, the following guidelines apply:

  Clustered indexes
tags:
  - "filestream"
  - "guidelines"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

When you perform online index operations, the following guidelines apply:

Clustered indexes must be created, rebuilt, or dropped offline when the underlying table

contains the following large object (LOB) data types:

,

, and.

Nonunique nonclustered indexes can be created online when the table has columns using

the LOB data types but none of these columns are used in the index definition as either

key or included columns.

Indexes on local temp tables can't be created, rebuilt, or dropped online. This restriction

doesn't apply to indexes on global temp tables.

You can start an online index operation as a resumable operation by using the

clause of

CREATE INDEX

or

ALTER INDEX. A resumable index operation can restart after an

unexpected failure, database failover, or an

command and continue

from where it was interrupted.

The following table shows the index operations that can be performed online, the indexes that

are excluded from these online operations, and resumable index restrictions. Additional

restrictions are also included.

Disabled clustered

index or disabled

indexed view

XML index

Index on a local temp

table

Specifying the keyword

can cause the

operation to fail when the table contains an

excluded index.

Additional restrictions on rebuilding disabled

indexes apply. For more information, see

Disable

indexes and constraints.

７

Note

Online index operations aren't available in every edition of Microsoft SQL Server. For a list

of features that are supported by the editions of SQL Server, see.

ﾉ

Expand table

```sql
RESUMABLE
ALTER INDEX PAUSE
ALTER INDEX REBUILD
ALL
```
