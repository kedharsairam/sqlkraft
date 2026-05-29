---
title: "Of a clustered index"
topic: "collation"
description: |
  Applies to:
  
  SQL Server
  
  Azure SQL Database
  
  Azure SQL Managed Instance
  
  SQL database in Microsoft Fabric
  
  You can use the following steps to estimate the amount of space that is required to store dat
tags:
  - "collation"
  - "of-a-clustered-index"
pubDate: 2025-12-01
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

You can use the following steps to estimate the amount of space that is required to store data

in a clustered index:

1. Calculate the space used to store data in the leaf level of the clustered index.

2. Calculate the space used to store index information for the clustered index.

3. Total the calculated values.

1. Specify the number of rows that are present in the table:

= number of rows in the table

2. Specify the number of fixed-length and variable-length columns and calculate the space

that is required for their storage:

Calculate the space that each of these groups of columns occupies within the data row.

The size of a column depends on the data type and length specification.

= total number of columns (fixed-length and variable-length)

= total byte size of all fixed-length columns

= number of variable-length columns

= maximum byte size of all variable-length columns

3. If the clustered index is nonunique, account for the

uniqueifier

column:

The uniqueifier is a nullable, variable-length column. It's non-null and 4 bytes in size in

rows that have nonunique key values. This value is part of the index key and is required to

make sure that every row has a unique key value.

=

+ 1

=

+ 1

=

+ 4

These modifications assume that all values are nonunique.

4. Part of the row, known as the null bitmap, is reserved to manage column nullability.

Calculate its size: