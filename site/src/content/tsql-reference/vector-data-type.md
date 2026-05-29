---
name: 'Vector data type'
title: 'Vector data type'
category: 'data-types'
description: 'Summarize this article for me'
tags: ["tsql", "data-types"]
pubDate: 2026-05-29
---

### vector

### vector

### vector

### varchar

### nvarchar

### json

### Half-precision float support in vector data type

### Always-

### up-to-date

ﾃ

Summarize this article for me

Applies to:

SQL Server 2025 (17.x)

Azure SQL Database

Azure SQL Managed

Instance

SQL database in Microsoft Fabric

The

data type is designed to store vector data optimized for operations such as

similarity search and machine learning applications. Vectors are stored in an optimized binary

format but are exposed as JSON arrays for convenience. Each element of the vector is stored as

a single-precision (4-byte) floating-point value.

To provide a familiar experience for developers, the

data type is created and displayed

as a JSON array. For example, a vector with three dimensions can be represented as

. Implicit and explicit conversion from and to the

type can be done using

,

, and

types.

vector is currently available for preview. To test, enable the

database

scoped configuration option. For details, review

PREVIEW_FEATURES = { ON | OFF }

.

SQL

For limitations, review

Limitations

and

Known issues

.

For more information on working with vector data, see:

Vector search and vector indexes in the SQL Database Engine

Intelligent applications

７

Note

SQL Server 2025 (17.x) supports half-precision (

) vectors. For more information,

see

.

７

Note

Vector features are available in Azure SQL Managed Instance configured with the

policy.

### vector

#### syntaxsql

### half-precision

#### syntaxsql

### vector

### vector

```sql
'[0.1, 2,
30]'
```

```sql
float16
```

```sql
PREVIEW_FEATURES
```

```sql
float16
```

```sql
ALTER
DATABASE
SCOPED CONFIGURATION
SET
PREVIEW_FEATURES =
ON
;
GO
```
