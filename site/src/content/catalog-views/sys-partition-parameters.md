---
name: 'sys.partition_parameters'
title: 'sys.partition_parameters'
category: 'partitions'
description: 'Azure SQL Managed Instance'
tags: ["catalog-view", "partitions"]
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

Contains a row for each parameter of a partition function.


## Description
ID of the partition function to which this parameter belongs.

ID of the parameter. Is unique within the partition function, beginning with

1.

ID of the system type of the parameter. Corresponds to the

column of the

catalog view.

Maximum length of the parameter in bytes.

Precision of the parameter if numeric-based; otherwise, 0.

Scale of the parameter if numeric-based; otherwise, 0.

Name of the collation of the parameter if character-based; otherwise,

NULL.

ID of the type. Is unique within the database. For system data types,

=

.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

Partition Function Catalog Views (Transact-SQL)

Catalog Views (Transact-SQL)

sys.partition_functions (Transact-SQL)

sys.partition_range_values (Transact-SQL)

ﾉ

Expand table

See Also

Last updated on 11/18/2025
