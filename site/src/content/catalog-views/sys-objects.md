---
name: 'sys.objects'
title: 'sys.objects'
category: 'objects'
description: '## A. Return all the objects that were modified in the last N days'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## A. Return all the objects that were modified in the last N days

## B. Return the parameters for a specified stored procedure or

## function

Visibility Configuration

.

Before you run the following query, replace

and

with valid values.

SQL

Before you run the following query, replace

and

with valid names.

SQL

## C. Return all the user-defined functions in a database

## D. Return the owner of each object in a schema

Before you run the following query, replace

with a valid database name.

SQL

Before you run the following query, replace all occurrences of

and

with valid names.

SQL

System catalog views (Transact-SQL)

sys.all_objects (Transact-SQL)

sys.system_objects (Transact-SQL)

sys.triggers (Transact-SQL)

Object Catalog Views (Transact-SQL)

Querying the SQL Server System Catalog FAQ

sys.internal_tables (Transact-SQL)

Related content

```sql
<database_name>
```

```sql
<n_days>
```

```sql
<database_name>
```

```sql
<schema_name.object_name>
```

```sql
USE
<database_name>;
GO
SELECT
name
AS
object_name,
SCHEMA_NAME(schema_id)
AS
schema_name,
type_desc,
create_date,
modify_date
FROM
sys.objects
WHERE
modify_date >
GETDATE
() - <n_days>
ORDER
BY
modify_date;
GO
```

```sql
USE
<database_name>;
GO
SELECT
SCHEMA_NAME(schema_id)
AS
schema_name,
o.name
AS
object_name,
o.type_desc,
p.parameter_id,
p.name
AS
parameter_name,
TYPE_NAME(p.user_type_id)
AS
parameter_type,
p.max_length,
p.precision,
p.scale,
p.is_output
FROM
sys.objects
AS
o
INNER
JOIN
sys.parameters
AS
p
ON
o.object_id = p.object_id
```

```sql
<database_name>
```

```sql
<database_name>
```

```sql
<schema_name>
```

```sql
WHERE
o.object_id = OBJECT_ID(
'<schema_name.object_name>'
)
ORDER
BY
schema_name,
object_name,
p.parameter_id;
GO
```

```sql
USE
<database_name>;
GO
SELECT
name
AS
function_name,
SCHEMA_NAME(schema_id)
AS
schema_name,
type_desc,
create_date,
modify_date
FROM
sys.objects
WHERE
type_desc
LIKE
'%FUNCTION%'
;
GO
```

```sql
USE
<database_name>;
GO
SELECT
'OBJECT'
AS
entity_type,
USER_NAME(OBJECTPROPERTY(object_id,
'OwnerId'
))
AS
owner_name,
name
FROM
sys.objects
WHERE
SCHEMA_NAME(schema_id) =
'<schema_name>'
UNION
SELECT
'TYPE'
AS
entity_type,
USER_NAME(TYPEPROPERTY(SCHEMA_NAME(schema_id) +
'.'
+
name
,
'OwnerId'
))
AS
owner_name,
name
FROM
sys.types
WHERE
SCHEMA_NAME(schema_id) =
'<schema_name>'
```

```sql
UNION
SELECT
'XML SCHEMA COLLECTION'
AS
entity_type,
COALESCE
(USER_NAME(xsc.principal_id), USER_NAME(s.principal_id))
AS
owner_name,
xsc.name
FROM
sys.xml_schema_collections
AS
xsc
INNER
JOIN
sys.schemas
AS
s
ON
s.schema_id = xsc.schema_id
WHERE
s.name =
'<schema_name>'
;
GO
```
