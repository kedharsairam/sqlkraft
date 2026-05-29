---
name: 'sys.external_tables'
title: 'sys.external_tables'
category: 'objects'
description: 'number of rows to load, either successfully or'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
For

, this is the

number of rows to load, either successfully or

unsuccessfully, before calculating the

percentage of rejected rows.

if

=

.

For external tables over a

SHARD_MAP_MANAGER external data

source, this is the data distribution of the

rows across the underlying base tables.

- Sharded

- Replicated

- Round

robin

For external tables over a

SHARD_MAP_MANAGER external data

source, this is the distribution type displayed

as a string.

For external tables over a

SHARD_MAP_MANAGER external data source

and a sharded distribution, this is the column

ID of the column that contains the sharding

key values.

For external tables over a

SHARD_MAP_MANAGER external data

source, this is the schema where the base

table is located on the remote databases (if

different from the schema where the external

table is defined).

For external tables over a

SHARD_MAP_MANAGER external data

source, this is the name of the base table on

the remote databases (if different from the

name of the external table).

The visibility of the metadata in catalog views is limited to securables that a user either owns or

on which the user has been granted some permission. For more information, see

Metadata

Visibility Configuration

.

sys.external_file_formats (Transact-SQL)

Related content

sys.external_data_sources (Transact-SQL)

CREATE EXTERNAL TABLE (Transact-SQL)

Last updated on 11/18/2025

```sql
reject_sample_value
```

```sql
reject_type = PERCENTAGE
```

```sql
NULL
```

```sql
reject_type
```

```sql
VALUE
```

```sql
distribution_type
```

```sql
0
```

```sql
1
```

```sql
2
```

```sql
distribution_desc
```

```sql
sharding_column_id
```

```sql
remote_schema_name
```

```sql
remote_object_name
```
