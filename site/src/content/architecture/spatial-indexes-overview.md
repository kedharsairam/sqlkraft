---
title: "Spatial Indexes Overview"
topic: "spatial-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  SQL database in Microsoft Fabric

  SQL Server supports spatial data and spatial indexes. A

  spatial index

  is a type of extended
tags:
  - "spatial-data"
  - "spatial-indexes-overview"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

SQL Server supports spatial data and spatial indexes. A

spatial index

is a type of extended index

that allows you to index a spatial column. A spatial column is a table column that contains data

of a spatial data type, such as

or

.

In SQL Server, spatial indexes are built using B-trees, which means that the indexes must

represent the 2-dimensional spatial data in the linear order of B-trees. Therefore, before

reading data into a spatial index, SQL Server implements a hierarchical uniform decomposition

of space. The index-creation process

decomposes

the space into a four-level

grid hierarchy

.

These levels are referred to as

level 1

(the top level),

level 2

,

level 3

, and

level 4

.

Each successive level further decomposes the level above it, so each upper-level cell contains a

complete grid at the next level. On a given level, all the grids have the same number of cells

along both axes (for example, 4x4 or 8x8), and the cells are all one size.

The following illustration shows the decomposition for the upper-right cell at each level of the

grid hierarchy into a 4x4 grid. In reality, all the cells are decomposed in this way. Thus, for

example, decomposing a space into four levels of 4x4 grids actually produces a total of 65,536

level-four cells.



Tip

SQL Server spatial tools is a Microsoft sponsored open-source collection of tools for use

with the spatial types in SQL Server. This project provides a set of reusable functions which

applications can make use of. These functions may include data conversion routines, new

transformations, aggregates, etc. See

in GitHub for

more details.
