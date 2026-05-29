---
title: "Edge constraints"
topic: "sql-graph"
description: |
  Applies to:

  SQL Server 2019 (15.x) and later versions

  Azure SQL Database

  Azure

  SQL Managed Instance

  SQL database in Microsoft Fabric

  Edge constraints can be used to enforce data integrity and sp
tags:
  - "sql-graph"
  - "edge-constraints"
pubDate: 2025-12-01
---

Applies to:

SQL Server 2019 (15.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

SQL database in Microsoft Fabric

Edge constraints can be used to enforce data integrity and specific semantics on the edge

tables in SQL Server graph database.

By default, edge tables don't enforce anything for the endpoints of the edge. That is, an edge

in a graph database could connect any node to any other node, regardless of the type.

SQL Graph supports edge constraints, which enable users to add constraints to their edge

tables, thereby enforcing specific semantics and also maintaining data integrity. When a new

edge is added to an edge table with edge constraints, the Database Engine enforces that the

nodes that the edge is trying to connect, exist in the proper node tables. It's also ensured that

a node can't be dropped, if any edge is referencing that node.

A single edge constraint consists of one or more edge constraint clause(s).

syntaxsql

An edge constraint clause is a pair of node table names, separated by the

keyword.

The first table name in the edge constraint clause is the name of the FROM node table for

the edge relationship.

The second table name in the edge constraint clause is the name of the TO node table for

the edge relationship.

The pair of table names therefore indicates the

direction

of the edge relationship.

As stated previously, an edge constraint can contain one or more edge constraint clauses.

Multiple edge constraints, defined for the same edge table, are enforced with an

operator.

Multiple edge constraint

clauses

, defined within the same edge constraint, are enforced

with an

operator.

```sql
TO
AND
OR
CONSTRAINT
constraint_name
CONNECTION
(cause1[, clause2...])
```
