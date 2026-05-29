---
name: 'sys.identity_columns'
title: 'sys.identity_columns'
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

Contains a row for each column that is an identity column.

The

view inherits rows from the

view. The

view returns the columns in the

view, plus the

,

,

, and

columns. For more information, see

Catalog Views (Transact-SQL)

.


## Description
The

view returns all columns in the

view. It also returns the additional columns

described below. For a description of the columns that the

view inherits from

, see

sys.columns (Transact-SQL)

.

sql_variant

Seed value for this identity column. The data type of the seed

value is the same as the data type of the column itself.

sql_variant

Increment value for this identity column. The data type of the

seed value is the same as the data type of the column itself.

sql_variant

Last value generated for this identity column. The data type of

the seed value is the same as the data type of the column itself.

Identity column is declared NOT FOR REPLICATION.

Note:

This

column does not apply to Azure Synapse Analytics.

ﾉ

Expand table

７

Note

To create an automatically incrementing number that can be used in multiple tables or

that can be called from applications without referencing any table, see

.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Object Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

Querying the SQL Server System Catalog FAQ

Last updated on 11/18/2025

See Also
