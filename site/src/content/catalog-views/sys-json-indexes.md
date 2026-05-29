---
name: 'sys.json_indexes'
title: 'sys.json_indexes'
category: 'indexes'
description: '## A. JSON index without array search optimization'
tags: ["catalog-view", "indexes"]
pubDate: 2026-05-29
---

## A. JSON index without array search optimization

Applies to:

SQL Server 2025 (17.x) Preview

Contains a row per json index.


## Description
Inherits columns from

sys.indexes

.

Indicates that array search optimization is enabled for JSON index.

1 = Array search optimization is enabled for JSON index.

0 = Array search optimization isn't enabled for JSON indexes.

Default is 0.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

visibility configuration

.

The following example returns JSON indexes for the table

. The JSON index is

created without the array search optimization option enabled.

SQL

ﾉ

Expand table

## B. JSON index with array search optimization

The following example returns JSON indexes for the table

. The JSON index is

created with the array search optimization option enabled.

SQL

Object catalog views (Transact-SQL)

System catalog views (Transact-SQL)

sys.indexes (Transact-SQL)

sys.json_index_paths (Transact-SQL)

CREATE JSON INDEX (Transact-SQL)

Last updated on 10/28/2025

Related content

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
ON
dbo.Customers (customer_info);
INSERT
INTO
dbo.Customers (customer_info)
```

```sql
dbo.Customers
```

```sql
VALUES
(
'{"name":"customer1", "email": "customer1@example.com", "phone":["123-456-
7890", "234-567-8901"]}'
);
SELECT
object_id,
index_id,
optimize_for_array_search
FROM
sys.json_indexes
AS
ji
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
optimize_for_array_search
FROM
sys.json_indexes
AS
ji
WHERE
object_id = OBJECT_ID(
'dbo.Customers'
);
```
