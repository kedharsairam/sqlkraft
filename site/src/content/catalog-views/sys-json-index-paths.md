---
name: 'sys.json_index_paths'
title: 'sys.json_index_paths'
category: 'indexes'
description: '## A. JSON index with no paths'
tags: ["catalog-view", "indexes"]
pubDate: 2026-05-29
---

## A. JSON index with no paths

Applies to:

SQL Server 2025 (17.x) Preview

Contains the SQL/JSON paths for a JSON index. If the

statement doesn't

define a

, this catalog view contains one row with a root SQL/JSON path

for

that index.


## Description
ID of table with JSON column.

ID of JSON index.

SQL/JSON path. Collation of the path column is fixed to

.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

visibility configuration

.

The following example returns JSON indexes for the table

. The JSON index is

created without specifying any SQL/JSON path.

SQL

ﾉ

Expand table

## B. JSON index for a specific path

## C. JSON index for multiple paths

The following example returns JSON indexes for the table

. The JSON index is

created for a specific SQL/JSON path

.

SQL

The following example returns JSON indexes for the table

. The JSON index is

created for multiple SQL/JSON paths

and

.

SQL

Object catalog views (Transact-SQL)

System catalog views (Transact-SQL)

sys.indexes (Transact-SQL)

sys.json_indexes (Transact-SQL)

CREATE JSON INDEX (Transact-SQL)

Last updated on 10/28/2025

Related content

```sql
CREATE JSON INDEX
```

```sql
sql_json_path
```

```sql
S
```

```sql
Latin1_General_100_BIN2_UTF8
```

```sql
dbo.Customers
```

```sql
DROP
TABLE
IF
EXISTS
dbo.Customers;
CREATE
TABLE
dbo.Customers
(
customer_id
INT
IDENTITY
PRIMARY
KEY
,
customer_info
JSON
NOT
NULL
);
CREATE
JSON
INDEX
CustomersJsonIndex
```

```sql
dbo.Customers
```

```sql
$.phone
```

```sql
dbo.Customers
```

```sql
$.name
```

```sql
$.email
```

```sql
ON
dbo.Customers (customer_info);
INSERT
INTO
dbo.Customers (customer_info)
VALUES
(
'{"name":"customer1", "email": "customer1@example.com", "phone":["123-456-
7890", "234-567-8901"]}'
);
SELECT
object_id,
index_id,
path
FROM
sys.json_index_paths
WHERE
object_id = OBJECT_ID(
'dbo.Customers'
);
```

```sql
DROP
TABLE
IF
EXISTS
dbo.Customers;
CREATE
TABLE
dbo.Customers
(
customer_id
INT
IDENTITY
PRIMARY
KEY
,
customer_info
JSON
NOT
NULL
);
CREATE
JSON
INDEX
CustomersJsonIndex
ON
dbo.Customers (customer_info)
FOR
(
'$.phone'
)
WITH
(OPTIMIZE_FOR_ARRAY_SEARCH =
ON
);
INSERT
INTO
dbo.Customers (customer_info)
VALUES
(
'{"name":"customer1", "email": "customer1@example.com", "phone":["123-456-
7890", "234-567-8901"]}'
);
SELECT
object_id,
index_id,
path
FROM
sys.json_index_paths
WHERE
object_id = OBJECT_ID(
'dbo.Customers'
);
```

```sql
DROP
TABLE
IF
EXISTS
dbo.Customers;
```

```sql
CREATE
TABLE
dbo.Customers
(
customer_id
INT
IDENTITY
PRIMARY
KEY
,
customer_info
JSON
NOT
NULL
);
CREATE
JSON
INDEX
CustomersJsonIndex
ON
dbo.Customers (customer_info)
FOR
(
'$.name'
,
'$.email'
);
INSERT
INTO
dbo.Customers (customer_info)
VALUES
(
'{"name":"customer1", "email": "customer1@example.com", "phone":["123-456-
7890", "234-567-8901"]}'
);
SELECT
object_id,
index_id,
path
FROM
sys.json_index_paths
WHERE
object_id = OBJECT_ID(
'dbo.Customers'
);
```
