---
name: "sys.sql_modules"
title: "sys.sql_modules"
category: "compatibility"
description: "The one-part or two-part name of a schema-scoped securable to be moved into the schema. Users and schemas are completely separate. Schemas aren't equivalent to database users. Use System catalog views to identify any differences between database users and schemas. ALTER SCHEMA can only be used to move securables between schemas in the same database. To change or drop a securable within a schema, u"
tags: ["compatibility", "catalog-view"]
pubDate: 2026-05-29
syntax: "uses_quoted_identifier"
---

## Description

The one-part or two-part name of a schema-scoped securable to be moved into the schema. Users and schemas are completely separate. Schemas aren't equivalent to database users. Use System catalog views to identify any differences between database users and schemas. ALTER SCHEMA can only be used to move securables between schemas in the same database. To change or drop a securable within a schema, use the ALTER or DROP statement specific to that securable. If a one-part name is used for , the name-resolution rules currently in effect will be used to locate the securable. All permissions associated with the securable are dropped when the securable is moved to the new schema. If the owner of the securable has been explicitly set, the owner remains unchanged. If the owner of the securable has been set to SCHEMA OWNER, the owner will

## Syntax

`uses_quoted_identifier`

## Permissions

The following table lists the catalog views and dynamic management views that you can use to return information about stored procedures. Description sys.sql_modules Returns the definition of a Transact-SQL procedure. The text of a procedure created with the ENCRYPTION option can't be viewed by using the catalog view. sys.assembly_modules Returns information about a CLR procedure. sys.parameters Returns information about the parameters that are defined in a procedure sys.sql_expression_dependencies sys.dm_sql_referenced_entities sys.dm_sql_referencing_entities Returns the objects that are referenced by a procedure. To estimate the size of a compiled procedure, use the following Performance Monitor Counters. SQLServer: Plan Cache Object Cache Hit Ratio Cache Pages Cache Object Counts These counters are available for various categories of cache objects including ad hoc Transact-SQL, prepared Transact-SQL, procedures, triggers, and so on. For more information, see SQL Server, Plan Cache Object . Requires permission in the database and permission on the schema in which the procedure is being created, or requires membership in the fixed database role. ﾉ Expand table ﾉ Expand table 1 1 DATABASE Indicates the scope of the DDL trigger applies to the current database. DATABASE must be specified if it was also specified when the trigger was created or modified. ALL SERVER : SQL Server 2008 (10.0.x) and later. Indicates the scope of the DDL trigger applies to the current server. ALL SERVER must be specified if it was also specified when the trigger was created or modified. ALL SERVER also applies to logon triggers. You can remove a DML trigger by dropping it or by dropping the trigger table. When a table is dropped, all associated triggers are also dropped. When a trigger is dropped, information about the trigger is removed from the , and catalog views. Multiple DDL triggers can be dropped per DROP TRIGGER statement only if all triggers were created using identical ON clauses. To rename a trigger, use DROP TRIGGER and CREATE TRIGGER. To change the definition of a trigger, use ALTER TRIGGER. For more information about determining dependencies for a specific trigger, see sys.sql_expression_dependencies , sys.dm_sql_referenced_entities (Transact-SQL) , and sys.dm_sql_referencing_entities (Transact-SQL) . For more information about viewing the text of the trigger, see sp_helptext (Transact-SQL) and sys.sql_modules (Transact-SQL) . For more information about viewing a list of existing triggers, see sys.triggers (Transact-SQL) and sys.server_triggers (Transact-SQL) . ７ Note This option is not available in a contained database.

## Remarks

The one-part or two-part name of a schema-scoped securable to be moved into the schema.

Users and schemas are completely separate. Schemas aren't equivalent to database users. Use

System catalog views

to identify any differences between database users and schemas.

ALTER SCHEMA can only be used to move securables between schemas in the same database.

To change or drop a securable within a schema, use the ALTER or DROP statement specific to

that securable.

If a one-part name is used for

securable_name

, the name-resolution rules currently in effect will

be used to locate the securable.

All permissions associated with the securable are dropped when the securable is moved to the

new schema. If the owner of the securable has been explicitly set, the owner remains

unchanged. If the owner of the securable has been set to SCHEMA OWNER, the owner will

remain SCHEMA OWNER; however, after the move SCHEMA OWNER will resolve to the owner

of the new schema. The

of the new owner will be

Moving an object such as a table or synonym will not automatically update references to that

object. You must modify any objects that reference the transferred object manually. For

example, if you move a table and that table is referenced in a trigger, you must modify the

trigger to reflect the new schema name. Use

sys.sql_expression_dependencies

dependencies on the object before moving it.

To change the schema of a table by using SQL Server Management Studio, in Object Explorer,

right-click on the table and then select

to open the Properties window. In the

box, select a new schema.

ALTER SCHEMA uses a schema level lock.

to transfer a stored procedure, function, view, or trigger to

another schema, it will not change the schema name, if present, of the object in the

column of the

catalog view, or in the result of the

built-in function. Therefore,

should not be used to

move these object types. Instead, drop and re-create the object in its new schema.

## Examples

### Example 1

`sys.sql_modules`

### Example 2

`sp_rename`

### Example 3

```sql
SELECT sm.object_id,
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
AS object_name,
o.[
type
],
o.[type_desc],
sm.[definition]
FROM sys.sql_modules
AS sm
INNER
JOIN sys.objects
AS o
ON sm.object_id = o.object_id
INNER
JOIN sys.schemas
AS ss
ON o.schema_id = ss.schema_id
ORDER
BY o.[
type
], ss.[
name
], o.[
name
];
```

### Example 4

`sys.objects`

### Example 5

`sys.sql_modules`

### Example 6

`CONTROL`

### Example 7

`ALTER`

### Example 8

`dbo.uspMyProc`

### Example 9

`dbo.uspMyProc`

### Example 10

```sql
DROP
PROCEDURE dbo.uspMyProc;
GO
DROP
PROCEDURE dbo.uspGetSalesbyMonth,
dbo.uspUpdateSalesQuotes,
dbo.uspGetSalesByYear;
```
