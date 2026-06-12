---
title: "Execute"
topic: "spatial-data"
description: ""
tags: ["spatial-data","execute"]
pubDate: 2025-12-01
---

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

This article describes how to execute a stored procedure in SQL Server by using SQL Server

Management Studio or Transact-SQL.

There are different ways to execute a stored procedure. The first and most common approach

is for an application or user to call the procedure. Another approach is to set the stored

procedure to run automatically when an instance of SQL Server starts.

When a procedure is called by an application or user, the Transact-SQL EXECUTE or EXEC

keyword is explicitly stated in the call. The procedure can be called and executed without the

EXEC keyword if the procedure is the first statement in a Transact-SQL batch.

The calling database collation is used when matching system procedure names. For this reason,

always use the exact case of system procedure names in procedure calls. For example, this

code fails if executed in the context of a database that has a case-sensitive collation:

To display the exact system procedure names, query the

sys.system_objects

and

sys.system_parameters

catalog views.

If a user-defined procedure has the same name as a system procedure, the user-defined

procedure might not ever execute.

Use the following recommendations for executing stored procedures.

System procedures begin with the prefix. Because they logically appear in all user- and

system- defined databases, system procedures can be executed from any database without

having to fully qualify the procedure name. However, it's best to schema-qualify all system

```sql
sp_
EXEC SP_heLP;
-- Fails to resolve because SP_heLP doesn't equal sp_help
```
