---
name: 'sys.sql_dependencies'
title: 'sys.sql_dependencies'
category: 'objects'
description: 'ID of the referenced entity, interpreted by value of class, according'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
ID of the referenced entity, interpreted by value of class, according

to:

0, 1 = Object ID of object or column.

2 = Type ID.

3 = XML Schema collection ID.

Minor-ID of the referenced entity, interpreted by value of class, as

shown in the following.

When class =:

0,

is a column ID; or if not a column, it is 0.

1,

is a column ID; or if not a column, it is 0.

Otherwise,

= 0.

Object or column is selected.

Object or column is updated.

Object is used in SELECT * clause (object-level only).

Requires membership in the

role. For more information, see

Metadata Visibility

Configuration

.

Catalog Views (Transact-SQL)

Object Catalog Views (Transact-SQL)

Querying the SQL Server System Catalog FAQ

See Also
