---
name: "the index"
title: "The index"
category: "hints"
description: "fragments containing multiple languages are supported."
tags: ["tsql","hints"]
pubDate: "2026-05-29"
---

fragments containing multiple languages are supported. For more information, see

Use Full-

Text Search with XML Columns.

We recommend that the index key column is an integer data type. This provides optimizations

at query execution time.

ALTER FULLTEXT INDEX can't be placed inside a user transaction. This statement must be run in

its own implicit transaction.

For more information about full-text indexes, see

Create and Manage Full-Text Indexes.

Whether the full-text index is populated depends on whether change-tracking is enabled and

whether WITH NO POPULATION is specified in the ALTER FULLTEXT INDEX statement. The

following table summarizes the result of their interaction.

Not enabled

Not specified

A full population is performed on the index.

Not enabled

Specified

No population of the index occurs until an ALTER FULLTEXT

INDEX.START POPULATION statement is issued.

Enabled

Specified

An error is raised, and the index isn't altered.

Enabled

Not specified

A full population is performed on the index.

For more information about populating full-text indexes, see

Populate Full-Text Indexes.

The first time that a full-text index is associated with a search property list, the index must be

repopulated to index property-specific search terms. The existing index data isn't truncated.

However, if you associate the full-text index with a different property list, the index is rebuilt.

Rebuilding immediately truncates the full-text index, removing all existing data, and the index

must be repopulated. While the population progresses, full-text queries on the base table

Expand table

### Search Document Properties with Search Property Lists

### Populate Full-Text Indexes

## Scenario A: Switch directly to a different search property list

search only on the table rows that have already been indexed by the population. The

repopulated index data includes metadata from the registered properties of the newly added

search property list.

Scenarios that cause rebuilding include:

Switch directly to a different search property list (see "Scenario A," later in this section).

Turn off the search property list, and later associate the index with any search property list

(see "Scenario B," later in this section).

1. A full-text index is created on

with a search property list

:

2. A full population is run on the full-text index:

3. The full-text index is later associated a different search property list,

, using the

following statement:

This statement causes a full population, the default behavior. However, before beginning

this population, the Full-Text Engine automatically truncates the index.

７

Note

For more information about how full-text search works with search property lists, see. For information about full

populations, see.

### sysadmin

### db_ddladmin

### db_owner

## Scenario B: Turn off the search property list and later associate

## the index with any search property list

`table_1`

`spl_1`

`spl_2`

```sql
CREATE
FULLTEXT
INDEX
ON table_1 (column_name)
KEY
INDEX unique_key_index
WITH
SEARCH
PROPERTY
LIST
=spl_1,
CHANGE_TRACKING
OFF
,
NO
POPULATION;
ALTER
FULLTEXT
INDEX
ON table_1
START
FULL
POPULATION;
ALTER
FULLTEXT
INDEX
ON table_1
SET
SEARCH
PROPERTY
LIST spl_2;
```
