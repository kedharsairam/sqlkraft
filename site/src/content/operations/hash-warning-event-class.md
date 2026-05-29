---
title: "Hash Warning Event Class"
topic: "event-classes"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  The Hash Warning event class can be used to monitor when a hash recursion or cessation of
  
  ha
tags:
  - "event-classes"
  - "hash-warning-event-class"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

The Hash Warning event class can be used to monitor when a hash recursion or cessation of

hashing (hash bailout) has occurred during a hashing operation.

Hash recursion occurs when the build input does not fit into available memory, resulting in the

split of input into multiple partitions that are processed separately. If any of these partitions

still do not fit into available memory, it is split into subpartitions, which are also processed

separately. This splitting process continues until each partition fits into available memory or

until the maximum recursion level is reached (displayed in the IntegerData data column).

Hash bailout occurs when a hashing operation reaches its maximum recursion level and shifts

to an alternate plan to process the remaining partitioned data. Hash bailout usually occurs

because of skewed data.

Hash recursion and hash bailout cause reduced performance in your server. To eliminate or

reduce the frequency of hash recursion and bailouts, do one of the following:

Make sure that statistics exist on the columns that are being joined or grouped.

If statistics exist on the columns, update them.

Use a different type of join. For example, use a MERGE or LOOP join instead, if

appropriate.

Increase available memory on the computer. Hash recursion or bailout occurs when there

is not enough memory to process queries in place and they need to spill to disk.

Creating or updating the statistics on the column involved in the join is the most effective way

to reduce the number of hash recursion or bailouts that occur.

７

Note

The terms

grace hash join

and

recursive hash join

are also used to describe hash bailout.

）

Important

To determine where the Hash Warning event is occurring when the query optimizer

generates an execution plan, you should also collect a Showplan event class in the trace.

You can choose any of the Showplan event classes except the Showplan Text and