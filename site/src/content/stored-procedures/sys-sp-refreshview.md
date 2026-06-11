---
name: "sys.sp_refreshview"
title: "sp_refreshview"
category: "general"
description: "SQL database in Microsoft Fabric Updates the metadata for the specified non-schema-bound view. Persistent metadata for a view can become outdated because of changes to the underlying objects upon which the view Transact-SQL syntax conventions identifier, but can only refer to views in the current database. (success) or a nonzero number (failure). should be run when changes are made to the objects"
tags: ["stored-procedure"]
pubDate: 2026-05-29
syntax: |
  sp_refreshview [ @viewname = ]
  'viewname'
  [ ; ]
---

## Description

SQL database in Microsoft Fabric Updates the metadata for the specified non-schema-bound view. Persistent metadata for a view can become outdated because of changes to the underlying objects upon which the view Transact-SQL syntax conventions identifier, but can only refer to views in the current database. (success) or a nonzero number (failure). should be run when changes are made to the objects underlying the view, which affects the definition of the view. Otherwise,

## Syntax

```sql
sp_refreshview [ @viewname = ]
'viewname'
[ ; ]
```

## Permissions

Applies to: SQL Server Azure SQL Database Azure SQL Managed Instance SQL database in Microsoft Fabric Updates the metadata for the specified non-schema-bound view. Persistent metadata for a view can become outdated because of changes to the underlying objects upon which the view depends. Transact-SQL syntax conventions syntaxsql The name of the view. @viewname is , with no default. @viewname can be a multipart identifier, but can only refer to views in the current database. (success) or a nonzero number (failure). If a view isn't created with , should be run when changes are made to the objects underlying the view, which affects the definition of the view. Otherwise, the view could produce unexpected results when you query it. Requires permission on the view, and permission on common language runtime (CLR) user-defined types and XML schema collections that the view columns reference. The following example refreshes a server-level DDL trigger. SQL sp_refreshview (Transact-SQL) Database Engine stored procedures (Transact-SQL) Last updated on 11/18/2025 Related content
