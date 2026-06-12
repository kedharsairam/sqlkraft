---
title: "Of a nonclustered index"
topic: "collation"
description: "Follow these steps to estimate the amount of space that is required to store a nonclustered"
tags: ["collation","of-a-nonclustered-index"]
pubDate: "2025-12-01"
---

Follow these steps to estimate the amount of space that is required to store a nonclustered

index:

1. Calculate variables for use in steps 2 and 3.

2. Calculate the space used to store index information in the leaf level of the nonclustered

index.

3. Calculate the space used to store index information in the non-leaf levels of the

nonclustered index.

4. Total the calculated values.

You can use the following steps to calculate variables that are used to estimate the amount of

space that is required to store the upper levels of the index.

1. Specify the number of rows that will be present in the table:

= number of rows in the table

2. Specify the number of fixed-length and variable-length columns in the index key and

calculate the space that is required for their storage:

The key columns of an index can include fixed-length and variable-length columns. To

estimate the interior level index row size, calculate the space that each of these groups of

columns occupies within the index row. The size of a column depends on the data type

and length specification.

= total number of key columns (fixed-length and variable-length)

= total byte size of all fixed-length key columns

= number of variable-length key columns

= maximum byte size of all variable-length key columns

3. Account for the data row locator that is required if the index is nonunique:

If the nonclustered index is nonunique, the data row locator is combined with the

nonclustered index key to produce a unique key value for every row.
