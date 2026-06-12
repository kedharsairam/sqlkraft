---
title: "SqlPackage with data in Parquet files"
topic: "sqlpackage"
description: |
  SqlPackage with data in Parquet files

  07/30/2025

  This article covers SqlPackage support for interacting with data stored in Azure Blob Storage

  that is in Parquet format.

  With

  extract

  , the datab
tags:
  - "sqlpackage"
  - "sqlpackage-with-data-in-parquet-files"
pubDate: 2025-12-01
---

SqlPackage with data in Parquet files

07/30/2025

This article covers SqlPackage support for interacting with data stored in Azure Blob Storage

that is in Parquet format.

With

extract

, the database schema (

file) is written to the local client running

SqlPackage and the data is written to Azure Blob Storage in Parquet format. The data is stored

in individual folders named with two-part table names.

CREATE EXTERNAL TABLE AS SELECT

(CETAS)

is used to write the files in Azure Blob Storage.

With

publish

, the database schema (

file) is read from the local client running

SqlPackage and the data is read from or written to Azure Blob Storage in Parquet format.

For SQL Server 2022 and Azure SQL Managed Instance, preview support for

extract

and

publish

with data in Parquet files in Azure Blob Storage is available in SqlPackage 162.1.176 and higher.

For Azure SQL Database, preview support for

publish

is available in SqlPackage 170.1.61 and

higher. SQL Server 2019 and earlier isn't supported. The

import

and

export

actions continue to

be available for SQL Server, Azure SQL Managed Instance, and Azure SQL Database. Support

for Parquet files in Azure Blob Storage continues to be generally available for

Azure Synapse

Analytics.

In SQL databases hosted in Azure, the extract/publish operations with Parquet files offer

improved performance over import/export operations with

files in many scenarios.

To export data from a database to Azure Blob Storage, the SqlPackage

extract

action is used

with following properties:

or

(not supported for use with

SQL Server)

```cmd.dacpac.dacpac.bacpac
/p:AzureStorageBlobEndpoint
/p:AzureStorageContainer
/p:AzureSharedAccessSignatureToken
/p:AzureStorageKey
```
