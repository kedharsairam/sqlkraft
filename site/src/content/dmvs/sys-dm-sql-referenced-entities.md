---
name: "sys.dm_sql_referenced_entities"
title: "sys.dm_sql_referenced_entities"
category: "execution"
description: "Returns one row for each user-defined entity that is referenced by name in the definition of the specified referencing entity in SQL Server."
tags: ["execution","dmv"]
pubDate: "2026-05-29"
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

Returns one row for each user-defined entity that is referenced by name in the definition of the specified referencing entity in SQL Server.

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
