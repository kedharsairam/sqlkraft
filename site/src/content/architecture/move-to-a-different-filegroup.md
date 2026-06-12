---
title: "Move to a different filegroup"
topic: "filestream"
description: "This topic describes how to move an existing index from its current filegroup to a different filegroup in SQL Server by using SQL Server Managemen"
tags: ["filestream","move-to-a-different-filegroup"]
pubDate: "2025-12-01"
---

This topic describes how to move an existing index from its current filegroup to a different

filegroup in SQL Server by using SQL Server Management Studio or Transact-SQL.

For design considerations including why you might want to place a nonclustered index on a

different filegroup, see

Index Placement on Filegroups or Partitions Schemes.

If a table has a clustered index, moving the clustered index to a new filegroup moves the

table to that filegroup.

You cannot move indexes created using a UNIQUE or PRIMARY KEY constraint using

Management Studio. To move these indexes use the

CREATE INDEX

statement with the

(DROP_EXISTING=ON) option in Transact-SQL.

Requires ALTER permission on the table or view. User must be a member of the

fixed

server role or the

and

fixed database roles.

1. In Object Explorer, click the plus sign to expand the database that contains the table

containing the index that you want to move.

2. Click the plus sign to expand the

folder.

3. Right-click the table containing the index that you want to move and select.
