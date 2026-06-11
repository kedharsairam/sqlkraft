---
name: "sys.dm_sql_referencing_entities"
title: "sys.dm_sql_referencing_entities"
category: "execution"
description: "SQL database in Microsoft Fabric Returns one row for each entity in the current database that references another user-defined entity by name. A dependency between two entities is created when one entity, called the , appears by name in a persisted SQL expression of another entity, called the ."
tags: ["execution", "dmv"]
pubDate: 2026-05-29
syntax: |
  sys.dm_sql_referencing_entities (
  ' schema_name.referenced_entity_name ' , ' <referenced_class> ' )
  <referenced_class> ::=
  {
  OBJECT
  | TYPE
  | XML_SCHEMA_COLLECTION
  | PARTITION_FUNCTION
  }
---

## Description

SQL database in Microsoft Fabric Returns one row for each entity in the current database that references another user-defined entity by name. A dependency between two entities is created when one entity, called the , appears by name in a persisted SQL expression of another entity, called the . For example, if a user-defined type (UDT) is specified as the referenced entity, this function returns each user-defined entity that reference that type by name in its

## Syntax

```sql
sys.dm_sql_referencing_entities (
' schema_name.referenced_entity_name ' , ' <referenced_class> ' )
<referenced_class> ::=
{
OBJECT
| TYPE
| XML_SCHEMA_COLLECTION
| PARTITION_FUNCTION
}
```

## Arguments

Azure SQL Database

Azure SQL Managed Instance

SQL database in Microsoft Fabric

Returns one row for each entity in the current database that references another user-defined

entity by name. A dependency between two entities is created when one entity, called the

referenced entity

, appears by name in a persisted SQL expression of another entity, called the

referencing entity

. For example, if a user-defined type (UDT) is specified as the referenced

entity, this function returns each user-defined entity that reference that type by name in its

definition. The function does not return entities in other databases that may reference the

specified entity. This function must be executed in the context of the master database to return

a server-level DDL trigger as a referencing entity.

You can use this dynamic management function to report on the following types of entities in

the current database that reference the specified entity:

Schema-bound or non-schema-bound entities

Database-level DDL triggers

Server-level DDL triggers

: SQL Server ( SQL Server 2008 (10.0.x) and later), SQL Database.

Transact-SQL syntax conventions

sys.dm_sql_referenced_entities (Transact-SQL)

sys.dm_sql_referencing_entities (Transact-SQL)

Related content
