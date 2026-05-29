---
name: 'sys.external_data_sources'
title: 'sys.external_data_sources'
category: 'external'
description: 'SQL Server 2016 (13.x) and later versions'
tags: ["catalog-view", "external"]
pubDate: 2026-05-29
---

Applies to:

SQL Server 2016 (13.x) and later versions

Azure SQL Database

Azure

SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft Fabric

Contains a row for each external data source in the current database for SQL Server, Azure SQL

Database, and Azure Synapse Analytics.

Contains a row for each external data source on the server for Analytics Platform System

(PDW).


## Description
Object ID for the external data

source.

Name of the external data

source.

The connection string, which

includes the protocol, IP

address, and port for the

external data source.

Data source type displayed as a

string.

,

,

,

,

,

Data source type displayed as a

number.

-

-

-

-

-

internal use only

-

-

ﾉ

Expand table


## Description
For type

, the IP and port

location of the Hadoop

Resource Manager. The

is

used for submitting a job on a

Hadoop data source.

for other types of external

data sources.

The

of the database

scoped credential used to

connect to the external data

source.

For type

, the name of the

remote database. For type

, the name of

the shard map manager

database.

for other types

of external data sources.

For type

, the

name of the shard map.

for other types of external data

sources.

Applies to:

SQL Server 2019

(15.x) and later. The

will contain

the same string from your

CONNECTION_OPTIONS

parameter from

CREATE

EXTERNAL DATA SOURCE

CONNECTION_OPTIONS

.

In SQL Server 2019 (15.x), this is

a semicolon-separated string.

In SQL Server 2022 (16.x), this

can also be a JSON-formatted

string.

Applies to:

SQL Server 2019

(15.x) and later.

NOT NULL. Whether pushdown

is enabled. For more

ON, OFF

```sql
data_source_id
```

```sql
name
```

```sql
location
```

```sql
type_desc
```

```sql
HADOOP
```

```sql
RDBMS
```

```sql
SHARD_MAP_MANAGER
```

```sql
REMOTE_DATA_ARCHIVE
```

```sql
BLOB_STORAGE
```

```sql
NONE
type
```

```sql
0
```

```sql
HADOOP
1
```

```sql
RDBMS
2
```

```sql
SHARD_MAP_MANAGER
3
```

```sql
REMOTE_DATA_ARCHIVE
4
```

```sql
5
```

```sql
BLOB_STORAGE
6
```

```sql
NONE
```

```sql
resource_manager_location
```

```sql
HADOOP
```

```sql
resource_manager_location
```

```sql
NULL
```

```sql
credential_id
```

```sql
object_id
```

```sql
database_name
```

```sql
RDBMS
```

```sql
SHARD_MAP_MANAGER
```

```sql
NULL
```

```sql
shard_map_name
```

```sql
SHARD_MAP_MANAGER
```

```sql
NULL
```

```sql
connection_options
```

```sql
connection_options
```

```sql
pushdown
```
