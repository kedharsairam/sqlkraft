---
name: 'sys.computed_columns'
title: 'sys.computed_columns'
category: 'objects'
description: 'Azure SQL Managed Instance'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

Applies to:

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

Contains a row for each column found in

that is a computed-column.


## Description
The

view returns all columns in the

view. It also returns the additional columns

described below. For a description of the columns that the

view inherits from

, see

sys.columns (Transact-SQL)

. The value of the

column is always set to 1 in the

view.

SQL text that defines this computed-column.

1 = The column definition depends on the default collation

of the database for correct evaluation; otherwise, 0. Such a

dependency prevents changing the database default

collation.

Computed column is persisted.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Object Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

Last updated on 11/18/2025

ﾉ

Expand table

See Also
