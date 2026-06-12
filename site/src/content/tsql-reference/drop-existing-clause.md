---
name: "DROP_EXISTING clause"
title: "DROP_EXISTING clause"
category: "statements"
description: ""
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

2005 (9.x) introduced new index options and also modified the way in which

options are specified. In the backward compatible syntax,

is equivalent to. When you set index options, the following rules apply:

New index options can only be specified by using.

Options can't be specified by using both the backward compatible and new syntax in the

same statement. For example, specifying

causes the

statement to fail.

When you create an XML index, the options must be specified by using.

You can use the

clause to rebuild the index, add or drop columns, modify

options, modify column sort order, or change the partition scheme or filegroup.

If the index enforces a

or

constraint and the index definition isn't altered

in any way, the index is dropped and re-created preserving the existing constraint. However, if

the index definition is altered the statement fails. To change the definition of a

or

constraint, drop the constraint and add a constraint with the new definition.

enhances performance when you re-create a clustered index, with either the

same or different set of keys, on a table that also has nonclustered indexes.

replaces the execution of a

statement on the old clustered index followed by the

execution of a

statement for the new clustered index. The nonclustered indexes

are rebuilt once, and then only if the index definition has changed. The

clause

doesn't rebuild the nonclustered indexes when the index definition has the same index name,

key and partition columns, uniqueness attribute, and sort order as the original index.

Whether the nonclustered indexes are rebuilt or not, they always remain in their original

filegroups or partition schemes and use the original partition functions. If a clustered index is

rebuilt to a different filegroup or partition scheme, the nonclustered indexes are not moved to

coincide with the new location of the clustered index. Therefore, even if the nonclustered

indexes previously aligned with the clustered index, they might no longer be aligned with it.

For more information about partitioned index alignment, see

Partitioned tables and indexes.

The

clause doesn't sort the data again if the same index key columns are used

in the same order and with the same ascending or descending order, unless the index

statement specifies a nonclustered index and the

option is set to. If the clustered

## Applies to

## Deferred deallocation

```sql
WITH option_name
```

```sql
WITH (option_name = ON)
```

```sql
WITH (<option_name> = <ON | OFF>)
```

```sql
WITH (DROP_EXISTING, ONLINE = ON)
```

```sql
WITH (<option_name> = <ON | OFF>)
```

`DROP_EXISTING`

```sql
PRIMARY KEY
```

`UNIQUE`

```sql
PRIMARY KEY
```

`UNIQUE`

`DROP_EXISTING`

`DROP_EXISTING`

```sql
DROP INDEX
```

```sql
CREATE INDEX
```

`DROP_EXISTING`

`DROP_EXISTING`

`ONLINE`

`OFF`
