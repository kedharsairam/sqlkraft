---
name: "CREATE EXTERNAL FILE FORMAT (Transact-"
title: "CREATE EXTERNAL FILE FORMAT (Transact-"
category: "statements"
description: "SQL Server 2016 (13.x) and later versions"
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

### Delimited text

### Hive RCFile

### Hive ORC

### Parquet

### JSON

### Delta

SQL)

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft Fabric

Creates an external file format object defining external data stored in Hadoop, Azure Blob

Storage, Azure Data Lake Store, OneLake in Microsoft Fabric, or for the input and output

streams associated with external streams. Creating an external file format is a prerequisite for

creating an External Table. By creating an External File Format, you specify the actual layout of

the data referenced by an external table. To create an External Table, see

CREATE EXTERNAL

TABLE (Transact-SQL)

.

The following file formats are supported:

SQL database in Microsoft Fabric only supports CSV format of delimited text.

Doesn't apply to Azure Synapse Analytics, Azure SQL Managed Instance, Azure SQL

Database, SQL database in Microsoft Fabric, or SQL Server 2022 (16.x).

Doesn't apply to Azure Synapse Analytics, Azure SQL Managed Instance, Azure SQL

Database, SQL database in Microsoft Fabric, or SQL Server 2022 (16.x).

Applies to Azure SQL Edge

only

. For information on using

to import JSON

data in other platforms, see

Import JSON documents into SQL Server

or

Query JSON files

using serverless SQL pool in Azure Synapse Analytics

.

Applies

only

to

serverless SQL pools in Azure Synapse Analytics

, Azure SQL Database, SQL

Server 2022 (16.x) and later versions. You can query

Delta Lake version 1.0

. Changes

introduced since, in

Delta Lake 1.2

, like renaming columns are not supported. If you are

using the higher versions of Delta with delete vectors, v2 checkpoints, and other features,

```sql
OPENROWSET
```
