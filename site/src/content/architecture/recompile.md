---
title: "Recompile"
topic: "spatial-data"
description: "This article describes how to recompile a stored procedure i"
tags: ["spatial-data","recompile"]
pubDate: "2025-12-01"
---

Analytics Platform System (PDW)

This article describes how to recompile a stored procedure in SQL Server by using Transact-

SQL. There are three ways to do this:

option in the procedure definition or

when the procedure is called, the RECOMPILE query hint on individual statements, or by using

the

system stored procedure.

When a procedure is compiled for the first time or recompiled, the procedure's query

plan is optimized for the current state of the database and its objects. If a database

undergoes significant changes to its data or structure, recompiling a procedure updates

and optimizes the procedure's query plan for those changes. This can improve the

procedure's processing performance.

There are times when procedure recompilation must be forced and other times when it

occurs automatically. Automatic recompiling occurs whenever SQL Server is restarted. It

also occurs if an underlying table referenced by the procedure has undergone physical

design changes.

Another reason to force a procedure to recompile is to counteract the "parameter

sniffing" behavior of procedure compilation. When SQL Server executes procedures, any

parameter values that are used by the procedure when it compiles are included as part of

generating the query plan. If these values represent the typical ones with which the

procedure is subsequently called, then the procedure benefits from the query plan every

time that it compiles and executes. If parameter values on the procedure are frequently

atypical, forcing a recompile of the procedure and a new plan based on different

parameter values can improve performance.

features statement-level recompilation of procedures. When SQL Server

recompiles stored procedures, only the statement that caused the recompilation is

compiled, instead of the complete procedure.

If certain queries in a procedure regularly use atypical or temporary values, procedure

performance can be improved by using the RECOMPILE query hint inside those queries.

Since only the queries using the query hint will be recompiled instead of the complete

```sql
WITH RECOMPILE sp_recompile
```
