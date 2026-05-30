---
title: "Sample"
topic: "sql-graph"
description: |
  Applies to:

  SQL Server 2017 (14.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  SQL database in Microsoft Fabric

  This sample provides a Transact-SQL script to create a graph
tags:
  - "sql-graph"
  - "sample"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2017 (14.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

This sample provides a Transact-SQL script to create a graph database with nodes and edges

and then use the new MATCH clause to match some patterns and traverse through the graph.

This sample script works on both Azure SQL Database and SQL Server 2017 (14.x) and later

versions.

This sample creates a graph schema for a hypothetical social network that has

,

, and

nodes. These nodes are connected to each other using

,

,

, and

edges. The following diagram shows a sample schema with

,

,

nodes, and

,

,

edges.

The following sample script uses the new T-SQL syntax to create node and edge tables. Learn

how to insert data into node and edge tables using

statement and also shows how to

use

clause for pattern matching and navigation.

This script performs the following steps:

```sql
People
Restaurant
City
Friends
Likes
LivesIn
LocatedIn
restaurant
city
person
LivesIn
LocatedIn
Likes
INSERT
MATCH
```
