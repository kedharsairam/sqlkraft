---
name: 'sys.stats_columns'
title: 'sys.stats_columns'
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

SQL analytics endpoint in

Microsoft Fabric

Warehouse in Microsoft Fabric

SQL database in Microsoft Fabric

Contains a row for each column that is part of

statistics.


## Description
ID of the object of which this column is part.

ID of the statistics of which this column is part.

If statistics correspond to an index, the

stats_id

value is the same as the

index_id

value in the

sys.indexes

catalog view.

1-based ordinal within set of stats columns.

ID of the column from

.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Object Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

Querying the SQL Server System Catalog FAQ

Statistics

sys.dm_db_stats_properties (Transact-SQL)

sys.dm_db_stats_histogram (Transact-SQL)

sys.stats (Transact-SQL)

Statistics in Microsoft Fabric

Last updated on 11/18/2025

ﾉ

Expand table

See Also
