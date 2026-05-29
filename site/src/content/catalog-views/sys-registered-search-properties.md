---
name: 'sys.registered_search_properties'
title: 'sys.registered_search_properties'
category: 'compatibility'
description: 'To view the integer identifier of any property that exists in a search property list of the current database, use the sys.registered_search_properties catalog view, as follows: PROPERTY_DESCRIPTION ='' property_description Specifies a user-defined description of the property. property_description is a string of up to 512 characters. This option is optional. Drops the specified property from the pro'
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: |
  USE AdventureWorks2022;
  GO
  SELECT * FROM sys.registered_search_properties;
  GO
---

## Description

To view the integer identifier of any property that exists in a search property list of the current database, use the sys.registered_search_properties catalog view, as follows: PROPERTY_DESCRIPTION =' property_description Specifies a user-defined description of the property. property_description is a string of up to 512 characters. This option is optional. Drops the specified property from the property list specified by . Dropping a property unregisters it, so it is no longer searchable. Each full-text index can have only one search property list. To enable querying on a given search property, you must add it to the search property list of the full-text index and then repopulate the index. When specifying a property you can arrange the PROPERTY_SET_GUID, PROPERTY_INT_ID, and PROPERTY_DESCRIPTION clauses in any order, as a comma-separated list within parentheses,

## Syntax

```sql
USE AdventureWorks2022;
GO
SELECT * FROM sys.registered_search_properties;
GO
```

## Remarks

To view the integer identifier of any property that exists in a search property list of the current

database, use the

sys.registered_search_properties

catalog view, as follows:

PROPERTY_DESCRIPTION ='

property_description

Specifies a user-defined description of the property.

property_description

is a string of up to

512 characters. This option is optional.

Drops the specified property from the property list specified by

. Dropping a property

unregisters it, so it is no longer searchable.

Each full-text index can have only one search property list.

To enable querying on a given search property, you must add it to the search property list of

the full-text index and then repopulate the index.

When specifying a property you can arrange the PROPERTY_SET_GUID, PROPERTY_INT_ID, and

PROPERTY_DESCRIPTION clauses in any order, as a comma-separated list within parentheses,

for example:

A given combination of

property_set_guid

property_int_id

must be unique in a search

property list. If you try to add an existing combination, the ALTER SEARCH PROPERTY LIST

operation fails and issues an error. This means that you can define only one name for a

given property.

## Examples

### Example 1

```sql
USE AdventureWorks2022;
GO
SELECT * FROM sys.registered_search_properties;
GO
```
