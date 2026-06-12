---
title: "Nonclustered index architecture"
topic: "index-architecture"
description: ""
tags: ["index-architecture","architecture"]
pubDate: "2026-05-29"
---

values are ordered in the nonclustered index, the query optimizer can quickly find all entries in

the index that match the specified

value. Each index entry points to the exact page

and row in the base table where the corresponding data from all other columns can be

retrieved. After the query optimizer finds all entries in the index, it can go directly to the exact

page and row to retrieve the data instead of scanning the entire base table.

Disk-based rowstore nonclustered indexes have the same B+ tree structure as clustered

indexes, except for the following differences:

A nonclustered index doesn't necessarily contain all columns and rows of the table.

The leaf level of a nonclustered index is made up of index pages instead of data pages.

The index pages on the leaf level of a nonclustered index contain key columns. Optionally,

they might also contain a subset of other columns in the table as

included columns

, to

avoid retrieving them from the base table.

The row locators in nonclustered index rows are either a pointer to a row or are a clustered

index key for a row, described as follows:

If the table has a clustered index, or the index is on an indexed view, the row locator is the

clustered index key for the row.

If the table is a heap, which means it doesn't have a clustered index, the row locator is a

pointer to the row. The pointer is built from the file identifier (ID), page number, and

number of the row on the page. The whole pointer is known as a Row ID (RID).

Row locators also ensure uniqueness for nonclustered index rows. The following table

describes how the Database Engine adds row locators to nonclustered indexes:

Nonunique

RID added to key columns

Unique

RID added to included columns

Nonunique

Clustered index keys added to key columns

ﾉ

Expand table

Unique

Clustered index keys added to included columns

Nonunique

Clustered index keys and uniqueifier (when present)

added to key columns

Unique

Clustered index keys and uniqueifier (when present)

added to included columns

The Database Engine never stores a given column more than once in a nonclustered index. The

index key order specified by the user when they create a nonclustered index is always honored:

any row locator columns that need to be added to the key of a nonclustered index are added

at the end of the key, following the columns specified in the index definition. Clustered index

key row locators in a nonclustered index can be used in query processing, regardless of

whether they are explicitly specified in the index definition or added implicitly.

The following examples show how row locators are implemented in nonclustered indexes:

Unique

clustered

index with key

columns (

,

,

)

Nonunique

nonclustered index

with key columns (

,

) and included

columns (

,

)

Key columns (

,

,

) and

included columns

(

,

)

The nonclustered index is nonunique, so

the row locator needs to be present in

the index keys. Columns

and

from

the row locator are already present, so

only column

is added. Column

is

added to the end of the key column list.

Unique

clustered

index with key

column (

)

Nonunique

nonclustered index

with key columns (

,

) and included

column (

)

Key columns (

,

,

)

The nonclustered index is nonunique, so

the row locator is added to the key.

Column

isn't already specified as a key

column, so it's added to the end of the

key column list. Column

is now in the

key, so there's no need to store it as an

included column.

Unique

clustered

index with key

column (

,

)

Unique nonclustered

index with key column

(

)

Key column (

)

and included

columns (

,

)

The nonclustered index is unique, so the

row locator is added to the included

columns.

ﾉ

Expand table

### nvarchar(max)

`ManagerID`

```sql
A
```

```sql
B
```

```sql
C
```

```sql
B
```

```sql
A
```

```sql
E
```

```sql
G
```

```sql
B
```

```sql
A
```

```sql
C
```

```sql
E
```

```sql
G
```

```sql
B
```

```sql
A
```

```sql
C
```

```sql
C
```

```sql
A
```

```sql
B
```

```sql
C
```

```sql
A
```

```sql
B
```

```sql
C
```

```sql
A
```

```sql
A
```

```sql
A
```

```sql
A
```

```sql
B
```

```sql
C
```

```sql
C
```

```sql
A
```

```sql
B
```
