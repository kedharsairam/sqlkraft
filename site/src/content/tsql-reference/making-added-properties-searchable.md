---
name: "Making Added Properties Searchable"
title: "Making Added Properties Searchable"
category: "statements"
description: ""
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

Full-text search maps a search property to a full-text index by using its property set GUID and

property integer ID. For information about how to obtain these for properties that have been

defined by Microsoft, see

Find Property Set GUIDs and Property Integer IDs for Search

Properties

. For information about properties defined by an independent software vendor (ISV),

see the documentation of that vendor.

Adding a search property to a search property list registers the property. A newly added

property can be immediately specified in

CONTAINS

queries. However, property-scoped full-

text queries on a newly added property will not return documents until the associated full-text

index is repopulated. For example, the following property-scoped query on a newly added

property,

new_search_property

, will not return any documents until the full-text index

associated with the target table (

table_name

) is repopulated:

To start a full population, use the following

ALTER FULLTEXT INDEX (Transact-SQL)

statement:

７

Note

This example uses the property name,

, which is similar to the concept of

canonical property names introduced in Windows Vista (Windows canonical name).

７

Note

### To create a property list

### To drop a property list

### To add or remove a property list on a full-text index

### To run a population on a full-text index

`System.Author`

```sql
SELECT column_name
FROM table_name
WHERE
CONTAINS( PROPERTY( column_name,
'new_search_property'
),
'contains_search_condition'
);
GO
USE database_name;
GO
ALTER
FULLTEXT
INDEX
ON table_name
START
FULL
POPULATION;
GO
```
