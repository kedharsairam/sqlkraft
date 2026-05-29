---
name: 'sys.sql_modules'
title: 'sys.sql_modules'
category: 'objects'
description: 'This information is also described in'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

This information is also described in

sys.dm_db_uncontained_entities

.

Renaming a stored procedure, function, view, or trigger doesn't change the name of the

corresponding object in the definition column of the

catalog view or the

definition returned by the

OBJECT_DEFINITION

built-in function. For this reason, we

recommend that you don't use

to rename these object types. Instead, drop and

recreate the object with its new name. Learn more in

sp_rename

.

The visibility of the metadata in catalog views is limited to securables that a user either owns,

or on which the user was granted some permission. For more information, see

Metadata

Visibility Configuration

.

The following example returns the object_id, schema name, object name, object type, and

definition of each module in the current database.

SQL

System catalog views (Transact-SQL)

Object catalog views (Transact-SQL)

Querying the SQL Server System Catalog FAQ

In-Memory OLTP overview and usage scenarios

Last updated on 11/18/2025

Related content

```sql
sys.sql_modules
```

```sql
sp_rename
```

```sql
SELECT
sm.object_id,
ss.[
name
]
AS
[
schema
],
o.[
name
]
AS
object_name,
o.[
type
],
o.[type_desc],
sm.[definition]
FROM
sys.sql_modules
AS
sm
INNER
JOIN
sys.objects
AS
o
ON
sm.object_id = o.object_id
INNER
JOIN
sys.schemas
AS
ss
ON
o.schema_id = ss.schema_id
ORDER
BY
o.[
type
], ss.[
name
], o.[
name
];
```
