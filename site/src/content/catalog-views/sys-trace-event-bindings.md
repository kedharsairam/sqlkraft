---
name: 'sys.trace_event_bindings'
title: 'sys.trace_event_bindings'
category: 'objects'
description: 'Azure SQL Managed Instance'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Article

•

02/28/2023

Applies to:

SQL Server

Azure SQL Managed Instance

The

catalog view contains a list of all possible usage combinations of

events and columns. For each event listed in the

column, all available columns

are listed in the

column. Not all available columns are populated each time a

given event occurs. These values do not change for a given version of the SQL Server Database

Engine.

For a complete list of supported trace events, see

SQL Server Event Class Reference

.


## Description
ID of the trace event. This column is also in the

catalog

view.

ID of the trace column. This column is also in the

catalog view.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Object Catalog Views (Transact-SQL)

sys.traces (Transact-SQL)

sys.trace_categories (Transact-SQL)

sys.trace_columns (Transact-SQL)

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use Extended Event catalog views instead.

ﾉ

Expand table

See Also

sys.trace_events (Transact-SQL)

sys.trace_subclass_values (Transact-SQL)
