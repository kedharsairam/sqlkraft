---
name: "sys.triggers"
title: "sys.triggers"
category: "compatibility"
description: "Contains a row for each object that is a trigger, with a type of TR or TA. DML trigger names are schema-scoped and, therefore, are visible in . DDL trigger names are scoped by the parent entity and are only visible in this view. columns uniquely identify the trigger in the database. Trigger name. DML trigger names are schema-scoped."
tags: ["compatibility","catalog-view"]
pubDate: "2026-05-29"
syntax: |
  SELECT OBJECT_ID
      FROM sys.triggers WHERE name = 'DatabaseTriggerLog'
---

## Description

Contains a row for each object that is a trigger, with a type of TR or TA. DML trigger names are schema-scoped and, therefore, are visible in. DDL trigger names are scoped by the parent entity and are only visible in this view. columns uniquely identify the trigger in the database. Trigger name. DML trigger names are schema-scoped. DDL trigger names are scoped with respect to the parent entity.

## Syntax

```sql
SELECT OBJECT_ID
FROM sys.triggers WHERE name = 'DatabaseTriggerLog'
```

## Permissions

DATABASE Indicates the scope of the DDL trigger applies to the current database. DATABASE must be specified if it was also specified when the trigger was created or modified. ALL SERVER : SQL Server 2008 (10.0.x) and later. Indicates the scope of the DDL trigger applies to the current server. ALL SERVER must be specified if it was also specified when the trigger was created or modified. ALL SERVER also applies to logon triggers. You can remove a DML trigger by dropping it or by dropping the trigger table. When a table is dropped, all associated triggers are also dropped. When a trigger is dropped, information about the trigger is removed from the , and catalog views. Multiple DDL triggers can be dropped per DROP TRIGGER statement only if all triggers were created using identical ON clauses. To rename a trigger, use DROP TRIGGER and CREATE TRIGGER. To change the definition of a trigger, use ALTER TRIGGER. For more information about determining dependencies for a specific trigger, see sys.sql_expression_dependencies , sys.dm_sql_referenced_entities (Transact-SQL) , and sys.dm_sql_referencing_entities (Transact-SQL). For more information about viewing the text of the trigger, see sp_helptext (Transact-SQL) and sys.sql_modules (Transact-SQL). For more information about viewing a list of existing triggers, see sys.triggers (Transact-SQL) and sys.server_triggers (Transact-SQL). ７ Note This option is not available in a contained database.
