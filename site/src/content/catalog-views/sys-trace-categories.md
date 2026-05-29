---
name: 'sys.trace_categories'
title: 'sys.trace_categories'
category: 'objects'
description: 'Similar event classes are grouped by a category. Each row in the'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Article

•

02/28/2023

Applies to:

SQL Server

Similar event classes are grouped by a category. Each row in the

catalog

view identifies a category that is unique across the server. These categories do not change for a

given version of the SQL Server Database Engine.

For a complete list of supported trace events, see

SQL Server Event Class Reference

.


## Description
Unique ID of this category. This column is also in the

catalog view.

Unique name of this category. This parameter is not localized.

Category type:

0 = Normal

1 = Connection

2 = Error

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use Extended Event catalog views instead.

ﾉ

Expand table

See Also

Object Catalog Views (Transact-SQL)

sys.traces (Transact-SQL)

sys.trace_columns (Transact-SQL)

sys.trace_events (Transact-SQL)

sys.trace_event_bindings (Transact-SQL)

sys.trace_subclass_values (Transact-SQL)
