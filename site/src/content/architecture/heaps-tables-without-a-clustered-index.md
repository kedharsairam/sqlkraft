---
title: "Heaps (tables without a clustered index)"
topic: "filestream"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  A heap is a table without a clustered index. One or more nonclustered indexes can be created
  
tags:
  - "filestream"
  - "heaps-tables-without-a-clustered-index"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

A heap is a table without a clustered index. One or more nonclustered indexes can be created

on tables stored as a heap. Data is stored in the heap without specifying an order. Usually data

is initially stored in the order in which the rows are inserted. However, the Database Engine can

move data around in the heap to store the rows efficiently. In query results, data order cannot

be predicted. To guarantee the order of rows returned from a heap, use the

clause. To

specify a permanent logical order for storing the rows, create a clustered index on the table, so

that the table is not a heap.

A heap is ideal for tables that are frequently truncated and reloaded. The database engine

optimizes space in a heap by filling the earliest available space.

Consider the following:

Locating free space in a heap can be costly, especially if there have been many deletes or

updates.

Clustered indexes offer steady performance for tables that are not frequently truncated.

For tables that are regularly truncated or recreated, such as temporary or staging tables, using

a heap is often more efficient.

The choice between using a heap and a clustered index can significantly affect your database's

performance and efficiency.

When a table is stored as a heap, individual rows are identified by reference to an 8-byte row

identifier (RID) consisting of the file number, data page number, and slot on the page

(FileID:PageID:SlotID). The row ID is a small and efficient structure.

７

Note

There are sometimes good reasons to leave a table as a heap instead of creating a

clustered index, but using heaps effectively is an advanced skill. Most tables should have a

carefully chosen clustered index unless a good reason exists for leaving the table as a

heap.

```sql
ORDER BY
```