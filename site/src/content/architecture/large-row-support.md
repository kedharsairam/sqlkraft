---
title: "Large row support"
topic: "query-processing"
description: ""
tags: ["query-processing", "architecture"]
pubDate: 2026-05-29
---

Slot array

As rows on a page are deleted or updated over time, free space might appear among

remaining rows. When a new row is added, it might be stored in this free space, if the space is

sufficient. This means that rows on a page might not be physically stored in any particular

order. However, the Database Engine maintains the slot array entries in a logical order. As a

result, rows on a page are also accessed in a logical order, for example the order defined by

the key of the BTree index that owns the page.

To support large rows that don't fit on a single page, the part of the row that doesn't fit can be

stored on other pages. The maximum size of data and overhead that can be contained in a

single row on a page is 8,060 bytes.

The 8,060-byte restriction doesn't apply to the data in the columns using the LOB data types.

By default for such columns, the data is stored in row if there's sufficient space. Otherwise, the

row contains a 16-byte pointer to a separate tree of text/LOB pages storing the LOB data in a

allocation unit. The

table option

controls this

behavior.

### varchar(7000)

### varchar(2000)

### varchar(7000)

### varchar(max)

### nvarchar(max)

### varbinary(max)

The 8,060-byte restriction is relaxed for tables and indexes that contain variable length

columns using the

,

,

,

sql_variant

, or CLR user-defined data types.

When the total row size of all fixed and variable length columns in a heap or index exceeds the

8,060-byte limitation, the Database Engine dynamically moves one or more variable length

columns to pages in a

allocation unit, starting with the widest column.

This is done whenever an insert or update operation increases the total size of the row beyond

the 8,060-byte limit. When a column is moved to a page in a

allocation unit,

a 24-byte pointer on the original page in a

allocation unit is maintained. If a

subsequent operation reduces the row size, the Database Engine dynamically moves the

columns back to the original data page.

For example, a table can be created with two columns: one

and another

. Individually, neither column exceeds 8,060 bytes, but combined they would do

so if the entire width of each column is filled. If this happens, the Database Engine dynamically

moves the

variable length column from the original page to the pages in a

allocation unit.

When a table or an index has

,

,

,

sql_variant

, or CLR user-defined

type columns that can exceed 8,060 bytes per row, consider the following:

Moving large rows to another page occurs dynamically as rows are lengthened based on

update operations. Update operations that shorten rows can cause them to be moved

back to the original page in a

allocation unit.

This data movement results in extra disk I/O. Query processing operations such as sorts

or joins on large records that contain row-overflow data might be slower.

Therefore, when you design a table with multiple

,

,

,

sql_variant

, or CLR user-defined type columns, consider the percentage of rows that are

likely to flow over and the frequency with which this overflow data is likely to be queried.

To avoid slower performance, normalize the table to move some of these columns to

another table to reduce or eliminate the likelihood of using row-overflow storage.

The length of individual columns must still fall within the limit of 8,000 bytes for

,

,

,

sql_variant

, and CLR user-defined type columns. Only their

combined lengths can exceed the 8,060-byte row limit of a table.

The sum of the lengths of other data type columns, for example

,

, and

data,

must still be within the 8,060-byte row limit. However, columns using the LOB data types

such as

,

, and

are exempt from the 8,060-

byte row limit.

### Uniform

### Mixed

`LOB_DATA`

```sql
large value types out of row
```

`ROW_OVERFLOW_DATA`

`ROW_OVERFLOW_DATA`

`IN_ROW_DATA`

`ROW_OVERFLOW_DATA`

`IN_ROW_DATA`
