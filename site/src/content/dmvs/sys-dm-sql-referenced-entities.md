---
title: sys.dm_sql_referenced_entities
name: sys.dm_sql_referenced_entities
category: execution
description:
pubDate: 2026-05-29
---

Requires SELECT permission on sys.dm_sql_referenced_entities and VIEW DEFINITION

permission on the referencing entity. By default, SELECT permission is granted to public.

Requires VIEW DEFINITION permission on the database or ALTER DATABASE DDL TRIGGER

permission on the database when the referencing entity is a database-level DDL trigger.

Requires VIEW ANY DEFINITION permission on the server when the referencing entity is a

server-level DDL trigger.

The following example returns the entities (tables and columns) that are referenced by the

database-level DDL trigger

.

SQL

The following example returns the entities that are referenced by the user-defined function

.

SQL

```sql
ddlDatabaseTriggerLog
```

```sql
dbo.ufnGetContactInformation
```

```sql
USE
AdventureWorks2022;
GO
SELECT
referenced_schema_name,
referenced_entity_name,
referenced_minor_name,
referenced_minor_id,
referenced_class_desc
FROM
sys.dm_sql_referenced_entities (
'ddlDatabaseTriggerLog'
,
'DATABASE_DDL_TRIGGER'
)
;
GO
```

```sql
USE
AdventureWorks2022;
GO
SELECT
```
