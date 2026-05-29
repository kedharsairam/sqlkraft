---
name: 'sys.types'
title: 'sys.types'
category: 'objects'
description: '## Get column details for a table'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## Get column details for a table


## Description
= SQL Server system data type.

= Implementation of the type is defined in a CLR assembly.

= Type is based on a SQL Server system data type.

ID of the stand-alone default that is bound to the type by using

sp_bindefault

.

= No default exists.

ID of the stand-alone rule that is bound to the type by using

sp_bindrule

.

= No rule exists.

Indicates the type is a table.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

To get metadata for columns in a table you can use the following code:

SQL

System catalog views (Transact-SQL)

Scalar Types Catalog Views (Transact-SQL)

ALTER AUTHORIZATION (Transact-SQL)

OBJECTPROPERTY (Transact-SQL)

Querying the SQL Server System Catalog FAQ

sys.columns (Transact-SQL)

Last updated on 11/18/2025

Related content

```sql
0
```

```sql
is_assembly_type
```

```sql
1
```

```sql
0
```

```sql
default_object_id
```

```sql
0
```

```sql
rule_object_id
```

```sql
0
```

```sql
is_table_type
```

```sql
CREATE
TABLE
dbo.[
sample
] (
id
INT
NOT
NULL
,col1 VARBINARY(10)
NULL
)
GO
SELECT
c.[
name
]
AS
column_name
,t.[
name
]
AS
[type_name]
,c.[max_length]
,c.[
precision
]
,c.[scale]
FROM
sys.columns c
```

```sql
INNER
JOIN
sys.types t
ON
c.user_type_id = t.user_type_id
WHERE
object_id = object_id(
'dbo.sample'
);
```
