---
name: "Structure of a recursive CTE"
title: "Structure of a recursive CTE"
category: "statements"
description: ""
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

A common table expression (CTE) provides the significant advantage of being able to reference

itself, thus creating a recursive CTE. A recursive CTE is one in which an initial CTE is repeatedly

executed to return subsets of data until the complete result set is obtained.

A query is referred to as a recursive query when it references a recursive CTE. Returning

hierarchical data is a common use of recursive queries. For example, displaying employees in

an organizational chart, or data in a bill of materials scenario in which a parent product has one

or more components and those components might have subcomponents, or might be

components, of other parents.

A recursive CTE can greatly simplify the code required to run a recursive query within a

,

,

,

, or

statement. In earlier versions of SQL Server, a recursive

query usually requires using temporary tables, cursors, and logic to control the flow of the

recursive steps. For more information about common table expressions, see

WITH

common_table_expression.

In Microsoft Fabric, Fabric Data Warehouse and the SQL analytics endpoint both support

standard, sequential, and

nested CTEs

, but not recursive CTEs.

The structure of the recursive CTE in Transact-SQL is similar to recursive routines in other

programming languages. Although a recursive routine in other languages returns a scalar

value, a recursive CTE can return multiple rows.

A recursive CTE consists of three elements:

1. Invocation of the routine.

The first invocation of the recursive CTE consists of one or more CTE query definitions

joined by

,

,

, or

operators. Because these query

definitions form the base result set of the CTE structure, they're referred to as anchor

members.

`SELECT`

`INSERT`

`UPDATE`

`DELETE`

```sql
CREATE VIEW
```

```sql
UNION ALL
```

`UNION`

`EXCEPT`

`INTERSECT`
