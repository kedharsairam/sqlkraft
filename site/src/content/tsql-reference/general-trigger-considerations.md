---
name: "General trigger considerations"
title: "General trigger considerations"
category: "statements"
description: "The ability to return results from triggers will be removed in a future version of SQL Server."
tags: ["tsql", "statements"]
pubDate: 2026-05-29
---

## Return results

## Multiple triggers

## Recursive triggers

The ability to return results from triggers will be removed in a future version of SQL Server.

Triggers that return result sets might cause unexpected behavior in applications that aren't

designed to work with them. Avoid returning result sets from triggers in new development

work, and plan to modify applications that currently do. To prevent triggers from returning

result sets, set the

disallow results from triggers option

to 1.

Logon triggers always disallow the return of results sets and this behavior isn't configurable. If

a logon trigger generates a result set, the trigger fails to launch and the login attempt that

fired the trigger is denied.

SQL Server lets you create multiple triggers for each DML, DDL, or

event. For example, if

is run for a table that already has an

trigger, an additional

update trigger is created. In earlier versions of SQL Server, only one trigger for each

,

, or

data modification event is allowed for each table.

SQL Server also supports recursive invocation of triggers when the

setting

is enabled using

.

Recursive triggers enable the following types of recursion to occur:

: With indirect recursion, an application updates table

. This fires

trigger

, updating table

. Trigger

then fires and updates table

.

: In direct recursion, the application updates table

. This fires trigger

, updating table

. Because table

was updated, trigger

fires again, and so on.

The following example uses both indirect and direct trigger recursion Assume that two update

triggers,

and

, are defined on table

. Trigger

updates table

recursively. An

statement runs each

and

one time. Additionally, the launch of

triggers the

execution of

(recursively) and

. The inserted and deleted tables for a specific trigger

contain rows that correspond only to the

statement that invoked the trigger.

### nested triggers

### nested triggers

## Nested triggers

## Deferred name resolution

`LOGON`

```sql
CREATE TRIGGER FOR UPDATE
```

`UPDATE`

`INSERT`

`UPDATE`

`DELETE`

`RECURSIVE_TRIGGERS`

```sql
ALTER DATABASE
```

`T1`

`TR1`

`T2`

`T2`

`T1`

`T1`

`TR1`

`T1`

`T1`

`TR1`

`TR1`

`TR2`

`T1`

`TR1`

`T1`

`UPDATE`

`TR1`

`TR2`

`TR1`

`TR1`

`TR2`

`UPDATE`
