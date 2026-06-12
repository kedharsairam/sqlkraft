---
title: "How it works"
topic: "filestream"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  This article defines the structures that exist during an online index operation and shows the
tags:
  - "filestream"
  - "how-it-works"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

This article defines the structures that exist during an online index operation and shows the

activities associated with these structures.

To allow for concurrent user activity during an index data definition language (DDL) operation,

the following structures are used during the online index operation: source and preexisting

indexes, target, and for rebuilding a heap or dropping a clustered index online, a temporary

mapping index.

The source is the original table or clustered index data. Preexisting indexes are any

nonclustered indexes that are associated with the source structure. For example, if the

online index operation is rebuilding a clustered index that has four associated

nonclustered indexes, the source is the existing clustered index and the preexisting

indexes are the nonclustered indexes.

The preexisting indexes are available to concurrent users for select, insert, update, and

delete operations. This includes bulk inserts (supported but not recommended during an

online index operation) and implicit updates by triggers and referential integrity

constraints. All preexisting indexes are available for queries. This means they might be

selected by the query optimizer and, if necessary, specified in index hints.

The target or targets is the new index (or heap) or a set of new indexes that is being

created or rebuilt. User insert, update, and delete operations to the source are applied by

the Database Engine to the target during the index operation. For example, if the online

index operation is rebuilding a clustered index, the target is the rebuilt clustered index;

the Database Engine doesn't rebuild nonclustered indexes when a clustered index is

rebuilt.

The target index isn't used until the index operation is committed. Internally, the index is

marked as write-only.
