---
name: 'sys.filegroups'
title: 'sys.filegroups'
category: 'databases-files'
description: 'Azure SQL Managed Instance'
tags: ["catalog-view", "databases-files"]
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

Contains a row for each data space that is a filegroup.


## Description
--

For a list of columns that this view inherits, see

sys.data_spaces

(Transact-SQL)

.

GUID for the filegroup.

NULL = PRIMARY filegroup

Identified for informational purposes only. Not supported.

Future compatibility is not guaranteed. In SQL Server, the value

is NULL.

1 = Filegroup is read-only.

0 = Filegroup is read/write.

Applies to:

SQL Server 2016 (13.x) and later versions.

1 = When a file in the filegroup meets the autogrow threshold,

all files in the filegroup grow.

0 = When a file in the filegroup meets the autogrow threshold,

only that file grows. This is the default.

Requires membership in the

role. For more information, see

Metadata Visibility

Configuration

.

Catalog Views (Transact-SQL)

Data Spaces (Transact-SQL)

ﾉ

Expand table

See Also

Last updated on 11/18/2025
