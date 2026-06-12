---
name: "sys.sp_addtype"
title: "sp_addtype"
category: "general"
description: "The name of the alias data type. Alias data type names must follow the rules for must be unique in each database. The physical, or SQL Server supplied, data type on which the alias data type is based. , with no default, and can be one of these values: This feature will be removed in a future version of SQL Server."
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_addtype
              [ @typename = ]
              N
              'typename'
              , [ @phystype = ]
              N
              'phystype'
              [ , [ @nulltype = ]
              'nulltype'
              ]
              [ , [ @owner = ]
              N
              'owner'
              ]
              [ ; ]
---

## Description

## Syntax

```sql
sp_addtype
[ @typename = ]
N
'typename'
, [ @phystype = ]
N
'phystype'
[ , [ @nulltype = ]
'nulltype'
]
[ , [ @owner = ]
N
'owner'
]
[ ; ]
```

## Permissions

To modify a user-defined type, you must drop the type by using a statement and then re-create it. Unlike user-defined types that are created by using , the database role isn't automatically granted permission on types that are created by using. This permission must be granted separately. In user-defined table types, structured user-defined types that are used in column_name <data type> are part of the database schema scope in which the table type is defined. To access structured user-defined types in a different scope within the database, use two-part names. In user-defined table types, the primary key on computed columns must be and. In Fabric SQL database , user defined types can be created but are not mirrored to Fabric OneLake, and columns of user defined types are skipped in mirroring. Beginning in SQL Server 2014 (12.x), processing data in a table type can be done in primary memory, and not on disk. For more information, see In-Memory OLTP overview and usage scenarios. For code samples showing how to create memory-optimized table types, see Creating a Memory-Optimized Table and a Natively Compiled Stored Procedure. Requires permission in the current database and permission on schema_name. If schema_name isn't specified, the default name resolution rules for determining the schema for the current user apply. If assembly_name is specified, a user must either own the assembly or have permission on it. If any columns in the statement are defined to be of a user-defined type, permission on the user-defined type is required. A user creating a table with a column that uses a user-defined type needs the permission on the user-defined type. If this table must be created in , then either the permission needs to be granted explicitly each time before the table is created, or this data type and permission need to be added to the database. For example: SQL
