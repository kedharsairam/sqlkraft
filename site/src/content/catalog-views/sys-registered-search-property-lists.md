---
name: "sys.registered_search_property_lists"
title: "sys.registered_search_property_lists"
category: "compatibility"
description: "Azure SQL Managed Instance Drops a property list from the current database if the search property list is currently not associated with any full-text index in the database. property_list_name Is the name of the search property list to be dropped. property_list_name is an identifier."
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  USE AdventureWorks2022;
  GO
  SELECT property_list_id, name FROM sys.registered_search_property_lists;
  GO
---

## Description

Azure SQL Managed Instance Drops a property list from the current database if the search property list is currently not associated with any full-text index in the database. property_list_name Is the name of the search property list to be dropped. property_list_name is an identifier. To view the names of the existing property lists, use the sys.registered_search_property_lists catalog view, as follows: You cannot drop a search property list from a database while the list is associated with any full- text index, and attempts to do so fail. To drop a search property list from a given full-text index, ALTER FULLTEXT INDEX statement, and specify the SET SEARCH PROPERTY LIST clause with either OFF or the name of another search property list. sys.registered_search_property_lists (Transact-SQL)

## Syntax

```sql
USE AdventureWorks2022;
GO
SELECT property_list_id, name FROM sys.registered_search_property_lists;
GO
```

## Arguments

Applies to:

Azure SQL Managed Instance

Adds a specified search property to, or drops it from the specified search property list.

Is the name of the property list being altered.

is an identifier.

To view the names of the existing property lists, use the

sys.registered_search_property_lists

catalog view, as follows:

Adds a specified search property to the property list specified by

. The property is

registered for the search property list . Before newly added properties can be used for property

searching, the associated full-text index or indexes must be repopulated. For more information,

ALTER FULLTEXT INDEX (Transact-SQL)

## Remarks

Applies to:

Azure SQL Managed Instance

Drops a property list from the current database if the search property list is currently not

associated with any full-text index in the database.

property_list_name

Is the name of the search property list to be dropped.

property_list_name

is an identifier.

To view the names of the existing property lists, use the

sys.registered_search_property_lists

catalog view, as follows:

You cannot drop a search property list from a database while the list is associated with any full-

text index, and attempts to do so fail. To drop a search property list from a given full-text index,

ALTER FULLTEXT INDEX

statement, and specify the SET SEARCH PROPERTY LIST clause

with either OFF or the name of another search property list.

sys.registered_search_property_lists (Transact-SQL)

## Examples

### Example 1

```sql
USE AdventureWorks2022;
GO
SELECT property_list_id, name FROM sys.registered_search_property_lists;
GO
```
