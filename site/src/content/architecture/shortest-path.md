---
title: "SHORTEST_PATH"
topic: "sql-graph"
description: |
  Applies to:

  SQL Server 2019 (15.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  SQL database in Microsoft Fabric

  Specifies a search condition for a graph, which is searched r
tags:
  - "sql-graph"
  - "shortest-path"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2019 (15.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

Specifies a search condition for a graph, which is searched recursively or repetitively.

SHORTEST_PATH can be used inside MATCH with graph node and edge tables, in the SELECT

statement.

Transact-SQL syntax conventions

The SHORTEST_PATH function lets you find:

A shortest path between two given nodes/entities

Single source shortest path(s).

Shortest path from multiple source nodes to multiple target nodes.

It takes an arbitrary length pattern as input and returns a shortest path that exists between two

nodes. This function can only be used inside MATCH. The function returns only one shortest

path between any two given nodes. If there exist, two or more shortest paths of the same

length between any pair of source and destination node(s), the function returns only one path

that was found first during traversal. An arbitrary length pattern can only be specified inside a

SHORTEST_PATH function.

For complete syntax, refer to

MATCH (SQL Graph)

.

FOR PATH must be used with any node or edge table name in the FROM clause, which

participates in an arbitrary length pattern. FOR PATH tells the engine that the node or edge

table returns an ordered collection representing the list of nodes or edges found along the

path traversed. The attributes from these tables can't be projected directly in the SELECT

clause. To project attributes from these tables, graph path aggregate functions must be used.

This pattern includes the nodes and edges that must be traversed repeatedly until either:

The desired node is reached.

The maximum number of iterations as specified in the pattern is met.
