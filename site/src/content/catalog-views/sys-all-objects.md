---
name: 'sys.all_objects'
title: 'sys.all_objects'
category: 'objects'
description: 'SQL_TABLE_VALUED_FUNCTION'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
SQL_TABLE_VALUED_FUNCTION

SQL_TRIGGER

TABLE_TYPE

USER_TABLE

UNIQUE_CONSTRAINT

VIEW

EXTENDED_STORED_PROCEDURE

create_date

Date the object was created.

modify_date

Date the object was last modified by using an ALTER statement. If

the object is a table or a view, modify_date also changes when an

index on the table or view is created or modified.

is_ms_shipped

Object created by an internal SQL Server component.

is_published

Object is published.

is_schema_published

Only the schema of the object is published.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Object Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

sys.objects (Transact-SQL)

sys.system_objects (Transact-SQL)

Last updated on 11/18/2025

See Also
