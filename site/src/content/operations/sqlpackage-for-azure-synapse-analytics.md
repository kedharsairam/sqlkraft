---
title: "SqlPackage for Azure Synapse Analytics"
topic: "sqlpackage"
description: |
  SqlPackage for Azure Synapse Analytics
  
  Article
  
  •
  
  03/06/2024
  
  This article covers SqlPackage support for
  
  Azure Synapse Analytics
  
  . It includes information on
  
  the following topics:
  
  integration wi
tags:
  - "sqlpackage"
  - "sqlpackage-for-azure-synapse-analytics"
pubDate: 2025-12-01
---

SqlPackage for Azure Synapse Analytics

Article

•

03/06/2024

This article covers SqlPackage support for

Azure Synapse Analytics

. It includes information on

the following topics:

integration with Azure Blob Storage for accessing data in parquet files

support for serverless SQL pools

Both dedicated and serverless SQL pools do not support the import/export actions in

SqlPackage or

files. SqlPackage supports Azure Synapse Analytics with

files

and can read and write data in parquet format files in Azure Blog Storage. To import or export

data from a dedicated SQL pool, you must use the publish or extract actions with data as

detailed below.

To export data from an Azure Synapse Analytics database to Azure Blob Storage, the

SqlPackage

extract

action is used with following properties:

/p:AzureStorageBlobEndpoint

/p:AzureStorageContainer

/p:AzureStorageKey

Access for the database to access the blob storage container is authorized via a storage

account key. The database schema (.dacpac file) is written to the local client running

SqlPackage and the data is written to Azure Blob Storage in parquet format.

An additional parameter is optional, which sets the storage root path within the container:

/p:AzureStorageRootPath

Without this property, the path defaults to

. Data is stored

in individual folders named with 2-part table names.

The following example extracts a database named

from a server named

to a local file named

in the current

directory. The data is written to a container named

in a storage account named

using a storage account key named

. The data is written to

the default path of

in the container.

```cmd
.bacpac
.dacpac
servername/databasename/timestamp/
databasename
yourserver.sql.azuresynapse.net
```