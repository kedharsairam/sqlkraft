---
name: 'sys.system_parameters'
title: 'sys.system_parameters'
category: 'objects'
description: ': SQL Server 2016 (13.x) and later, SQL'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
supported.

: SQL Server 2016 (13.x) and later, SQL

Database.

ID of the CEK.

: SQL Server 2016 (13.x) and later, SQL

Database.

The name of the database where the column

encryption key exists if different than the

database of the column.

if the key exists in

the same database as the column.

: SQL Server 2016 (13.x) and later, SQL

Database.

Indicates how many dimensions the vector has.

: SQL Server 2025 (17.x) and later

versions, and SQL Database

Indicates the data type used to store vector

dimensions values.

= 32-bit (single-precision) float

= 16-bit (half-precision) float

: SQL Server 2025 (17.x) and later

versions, and SQL Database

Contains the textual description of the data type

used to store vector dimensions values.

: SQL Server 2025 (17.x) and later

versions, and SQL Database

For more information, see

Half-precision floating-point format

.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

visibility configuration

.

1

1

Object catalog views (Transact-SQL)

System catalog views (Transact-SQL)

Querying the SQL Server System Catalog FAQ

sys.parameters (Transact-SQL)

sys.all_parameters (Transact-SQL)

Last updated on 11/28/2025

Related content

```sql
column_encryption_key_id
```

```sql
column_encryption_key_database_name
```

```sql
NULL
```

```sql
vector_dimensions
```

```sql
vector_base_type
```

```sql
0
```

```sql
1
```

```sql
vector_base_type_desc
```
