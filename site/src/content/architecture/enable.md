---
title: "Enable"
topic: "filestream"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  This article describes how to enable a disabled index in SQL Server by using SQL Server
  
  Mana
tags:
  - "filestream"
  - "enable"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

This article describes how to enable a disabled index in SQL Server by using SQL Server

Management Studio or Transact-SQL. After an index is disabled, it remains in a disabled state

until it rebuilds or is dropped.

After the index rebuilds, any constraints that were disabled because of disabling the index must

be manually enabled.

and

constraints are enabled by rebuilding the

associated index. This index must be rebuilt (enabled) before you can enable

constraints that reference the

or

constraint.

constraints are

enabled by using the

statement.

Rebuilding a disabled clustered index can't be performed when the

option is set to

.

When the clustered index is disabled or enabled and the nonclustered index is disabled, the

clustered index action has the following results on the disabled nonclustered index.

Remains disabled

Rebuilt and enabled

Rebuilt and enabled

Remains disabled

Creating a new clustered index behaves the same as

.

Allowed actions on nonclustered indexes associated with a clustered index depend on the

state, whether disabled or enabled, of both index types. The following table summarizes the

allowed actions on nonclustered indexes.

ﾉ

Expand table

ﾉ

Expand table

```sql
PRIMARY KEY
UNIQUE
FOREIGN KEY
PRIMARY KEY
UNIQUE
FOREIGN KEY
ALTER TABLE CHECK CONSTRAINT
ONLINE
ON
ALTER INDEX REBUILD
ALTER INDEX ALL REBUILD
DROP INDEX
CREATE INDEX WITH DROP_EXISTING
ALTER INDEX ALL REBUILD
```