---
title: "Architecture"
topic: "sql-graph"
description: |
  SQL Graph Architecture

  Applies to:

  SQL Server 2017 (14.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  SQL database in Microsoft Fabric

  Learn about the architecture of SQL G
tags:
  - "sql-graph"
  - "architecture"
pubDate: 2025-12-01
---

SQL Graph Architecture

Applies to:

SQL Server 2017 (14.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

Learn about the architecture of SQL Graph. Knowing the basics make it easier to understand

other SQL Graph articles.

Users can create one graph per database. A graph is a collection of node and edge tables.

Node or edge tables can be created under any schema in the database, but they all belong to

one logical graph. A node table is collection of similar type of nodes. For example, a

node table holds all the

nodes belonging to a graph. Similarly, an edge table is a

collection of similar type of edges. For example, a

edge table holds all the edges that

connect a

to another

. Since nodes and edges are stored in tables, most of the

operations supported on regular tables are supported on node or edge tables.

The following diagram shows the SQL Graph database architecture.

SQL Graph database

```sql
Person
Person
Friends
Person
Person
```
