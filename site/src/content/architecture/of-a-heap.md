---
title: "Of a heap"
topic: "collation"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  Azure Synapse Analytics

  Analytics Platform System (PDW)

  SQL database in Microsoft

  Fabric

  You can use the following steps to
tags:
  - "collation"
  - "of-a-heap"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

You can use the following steps to estimate the amount of space that is required to store data

in a heap:

1. Specify the number of rows that will be present in the table:

= number of rows in the table

2. Specify the number of fixed-length and variable-length columns and calculate the space

that is required for their storage:

Calculate the space that each of these groups of columns occupies within the data row.

The size of a column depends on the data type and length specification.

= total number of columns (fixed-length and variable-length)

= total byte size of all fixed-length columns

= number of variable-length columns

= maximum total byte size of all variable-length columns

3. Part of the row, known as the null bitmap, is reserved to manage column nullability.

Calculate its size:

= 2 + ((

- 7. / 8)

Only the integer part of this expression should be used. Discard any remainder.

4. Calculate the variable-length data size:

If there are variable-length columns in the table, determine how much space is used to

store the columns within the row:

= 2 + (

x 2) +

The bytes added to

are for tracking each variable-length column. This

formula assumes that all variable-length columns are 100 percent full. If you anticipate

that a smaller percentage of the variable-length column storage space will be used, you

can adjust the

value by that percentage to yield a more accurate estimate

of the overall table size.

７

Note
