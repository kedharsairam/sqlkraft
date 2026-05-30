---
name: "sys.dm_sql_referenced_entities"
title: "sys.dm_sql_referenced_entities"
category: "execution"
description: "SQL database in Microsoft Fabric Returns one row for each user-defined entity that is referenced by name in the definition of the specified referencing entity in SQL Server. A dependency between two entities is created when one user-defined entity, called the , appears by name in a persisted SQL expression of another user-defined entity, called the procedure is the specified referencing entity, th"
tags: ["execution", "dmv"]
pubDate: 2026-05-29
syntax: |
  sys.dm_sql_referenced_entities (
  ' [ schema_name. ] referencing_entity_name ' ,
  ' <referencing_class> ' )
  <referencing_class> ::=
  {
  OBJECT
  | DATABASE_DDL_TRIGGER
  | SERVER_DDL_TRIGGER
  }
---

## Description

SQL database in Microsoft Fabric Returns one row for each user-defined entity that is referenced by name in the definition of the specified referencing entity in SQL Server. A dependency between two entities is created when one user-defined entity, called the , appears by name in a persisted SQL expression of another user-defined entity, called the procedure is the specified referencing entity, this function returns all user-defined entities that

## Syntax

```sql
sys.dm_sql_referenced_entities (
' [ schema_name. ] referencing_entity_name ' ,
' <referencing_class> ' )
<referencing_class> ::=
{
OBJECT
| DATABASE_DDL_TRIGGER
| SERVER_DDL_TRIGGER
}
```
