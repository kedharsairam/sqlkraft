---
name: 'sys.sql_expression_dependencies'
title: 'sys.sql_expression_dependencies (Transact-'
category: 'objects'
description: '## A. Return entities that are referenced by another entity'
tags: ["catalog-view", "objects"]
pubDate: 2026-05-29
---

## A. Return entities that are referenced by another entity

## B. Return entities that reference another entity

Numbered stored procedures with an integer value greater than 1 aren't tracked as either a

referencing or referenced entity.

Requires VIEW DEFINITION permission on the database and SELECT permission on

for the database. By default, SELECT permission is granted

only to members of the

fixed database role. When SELECT and VIEW DEFINITION


## permissions are granted to another user, the grantee can view all dependencies in the
database.

The following example returns the tables and columns referenced in the view

. The view depends on the entities (tables and columns)

returned in the

and

columns.

SQL

3

## C. Return cross-database dependencies

The following example returns the entities that reference the table

. The

entities returned in the

column depend on the

table.

SQL

The following example returns all cross-database dependencies. The example first creates the

database

and two stored procedures that reference tables in the databases

and

.

The

table is then queried to report the cross-database

dependencies between the procedures and the tables.

is returned in the

column for the referenced entity

because a schema name isn't

specified for that entity in the definition of the procedure.

SQL

sys.dm_sql_referenced_entities (Transact-SQL)

sys.dm_sql_referencing_entities (Transact-SQL)

Related content

```sql
sys.sql_expression_dependencies
```

```sql
Production.vProductAndDescription
```

```sql
referenced_entity_name
```

```sql
referenced_column_name
```

```sql
USE
AdventureWorks2022;
GO
SELECT
OBJECT_NAME(referencing_id)
AS
referencing_entity_name,
o.type_desc
AS
referencing_description,
COALESCE
(COL_NAME(referencing_id, referencing_minor_id),
'(n/a)'
)
AS
referencing_minor_id,
referencing_class_desc,
referenced_server_name,
referenced_database_name,
referenced_schema_name,
referenced_entity_name,
COALESCE
(COL_NAME(referenced_id, referenced_minor_id),
'(n/a)'
)
AS
referenced_column_name,
is_caller_dependent,
is_ambiguous
FROM
sys.sql_expression_dependencies
AS
sed
INNER
JOIN
sys.objects
AS
o
ON
sed.referencing_id = o.object_id
WHERE
referencing_id = OBJECT_ID(N
'Production.vProductAndDescription'
);
```

```sql
Production.Product
```

```sql
referencing_entity_name
```

```sql
Product
```

```sql
db1
```

```sql
db2
```

```sql
db3
```

```sql
sys.sql_expression_dependencies
```

```sql
NULL
```

```sql
referenced_schema_name
```

```sql
t3
```

```sql
USE
AdventureWorks2022;
GO
SELECT
OBJECT_SCHEMA_NAME(referencing_id)
AS
referencing_schema_name,
OBJECT_NAME(referencing_id)
AS
referencing_entity_name,
o.type_desc
AS
referencing_description,
COALESCE
(COL_NAME(referencing_id, referencing_minor_id),
'(n/a)'
)
AS
referencing_minor_id,
referencing_class_desc,
referenced_class_desc,
referenced_server_name,
referenced_database_name,
referenced_schema_name,
referenced_entity_name,
COALESCE
(COL_NAME(referenced_id, referenced_minor_id),
'(n/a)'
)
AS
referenced_column_name,
is_caller_dependent,
is_ambiguous
FROM
sys.sql_expression_dependencies
AS
sed
INNER
JOIN
sys.objects
AS
o
ON
sed.referencing_id = o.object_id
WHERE
referenced_id = OBJECT_ID(N
'Production.Product'
);
```

```sql
CREATE
DATABASE
db1;
GO
USE
db1;
GO
CREATE
PROCEDURE
p1
AS
SELECT
*
FROM
db2.s1.t1;
```

```sql
GO
CREATE
PROCEDURE
p2
AS
UPDATE
db3..t3
SET
c1 = c1 + 1;
GO
SELECT
OBJECT_NAME(referencing_id),
referenced_database_name,
referenced_schema_name,
referenced_entity_name
FROM
sys.sql_expression_dependencies
WHERE
referenced_database_name
IS
NOT
NULL
;
GO
USE
master
;
GO
DROP
DATABASE
db1;
```
