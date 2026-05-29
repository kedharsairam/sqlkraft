---
name: 'sys.registered_search_properties'
title: 'sys.registered_search_properties (Transact-'
category: 'objects'
description: 'For more information about search property lists, see'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

For more information about search property lists, see

Search Document Properties with Search

Property Lists

.

Visibility of the metadata for search properties is limited to those that are in search property

lists that you either own or on which you have been granted some REFERENCE permission.

The following example lists all of the metadata for registered search properties.

ALTER FULLTEXT INDEX (Transact-SQL)

sys.fulltext_indexes (Transact-SQL)

Search Document Properties with Search Property Lists

Last updated on 11/18/2025

７

Note

The search property list owner can grant REFERENCE or CONTROL permissions on the list.

Users with CONTROL permission can also grant REFERENCE permission to other users.

See Also

```sql
USE AdventureWorks2022;
GO
SELECT * FROM sys.registered_search_properties;
GO
```
