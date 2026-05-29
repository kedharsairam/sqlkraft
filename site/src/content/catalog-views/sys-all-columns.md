---
name: 'sys.all_columns'
title: 'sys.all_columns'
category: 'objects'
description: ', contains a textual description of the type of a'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Description
If not

, contains a textual description of the type of a

column in a ledger view:

: SQL Server 2022 (16.x) and later versions, and

SQL Database.

Indicates a ledger table column that was dropped.

: SQL Server 2022 (16.x) and later versions, and

SQL Database

Indicates how many dimensions the vector has.

: SQL Server 2025 (17.x) and later versions, and

SQL Database

Indicates the data type used to store vector dimensions

values.

= 32-bit (single-precision) float

= 16-bit (half-precision) float

: SQL Server 2025 (17.x) and later versions, and

SQL Database

Contains the textual description of the data type used to

store vector dimensions values.

: SQL Server 2025 (17.x) and later versions, and

SQL Database

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

sys.columns (Transact-SQL)

sys.system_columns (Transact-SQL)

sys.computed_columns (Transact-SQL)

Last updated on 11/28/2025

Related content

```sql
ledger_view_column_type_desc
```

```sql
NULL
```

```sql
TRANSACTION_ID
SEQUENCE_NUMBER
OPERATION_TYPE
OPERATION_TYPE_DESC
```

```sql
is_dropped_ledger_column
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
