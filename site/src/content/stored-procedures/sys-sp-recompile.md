---
name: "sys.sp_recompile"
title: "sp_recompile"
category: "general"
description: "Causes stored procedures, triggers, and user-defined functions to be recompiled the next time that they're run. It does this by dropping the existing plan from the procedure cache, forcing a new plan to be created the next time that the procedure or trigger is run."
tags: ["stored-procedure"]
pubDate: "2026-05-29"
syntax: |
  sp_recompile [ @objname = ]
      N
      'object'
      [ ; ]
---

## Description

Causes stored procedures, triggers, and user-defined functions to be recompiled the next time that they're run. It does this by dropping the existing plan from the procedure cache, forcing a new plan to be created the next time that the procedure or trigger is run. In a SQL Server Profiler collection, the event is logged instead of the event The qualified or unqualified name of a stored procedure, trigger, table, view, or user-defined function in the current database. , with no default. is the name of a stored procedure, trigger, or user-defined function, the stored procedure, trigger, or function will be recompiled the next time that it's run. is the name of a table or view, all the stored procedures, triggers, or user-

## Syntax

```sql
sp_recompile [ @objname = ]
N
'object'
[ ; ]
```

## Remarks

Causes stored procedures, triggers, and user-defined functions to be recompiled the next time

that they're run. It does this by dropping the existing plan from the procedure cache, forcing a

new plan to be created the next time that the procedure or trigger is run. In a SQL Server

Profiler collection, the event

is logged instead of the event

The qualified or unqualified name of a stored procedure, trigger, table, view, or user-defined

function in the current database.

, with no default.

is the name of a stored procedure, trigger, or user-defined function, the

stored procedure, trigger, or function will be recompiled the next time that it's run.

is the name of a table or view, all the stored procedures, triggers, or user-

defined functions that reference the table or view will be recompiled the next time that

they're run.

(success) or a nonzero number (failure).

looks for an object in the current database only.

## Examples

### Example 1

`sp_recompile`

### Example 2

```sql
WITH RECOMPILE
```

### Example 3

```sql
WITH RECOMPILE
```

### Example 4

`Sales.Customer`

### Example 5

```sql
USE
AdventureWorks2022;
GO
EXECUTE sp_recompile N
'Sales.Customer'
;
GO
```
