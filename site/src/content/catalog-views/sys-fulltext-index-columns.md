---
name: 'sys.fulltext_index_columns'
title: 'sys.fulltext_index_columns'
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

Azure SQL Database

Azure SQL Managed Instance

Contains a row for each column that is part of a full-text index.


## Description
ID of the object of which this is part.

ID of the column that is part of the full-text index.

ID of the type column that stores the user-supplied document file

extension-".doc", ".xls", and so forth-of the document in a given row. The

type column is specified only for columns whose data requires filtering

during full-text indexing. NULL if not applicable. For more information,

see

Configure and Manage Filters for Search

.

LCID of language whose word breaker is used to index this full-text

column.

0 = Neutral.

For more information, see

sys.fulltext_languages (Transact-SQL)

.

1 = This column has statistical semantics enabled in addition to full-text

indexing.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission.

Object Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

ﾉ

Expand table

See Also
