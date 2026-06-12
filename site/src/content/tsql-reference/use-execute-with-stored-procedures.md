---
name: "Use EXECUTE with stored procedures"
title: "Use EXECUTE with stored procedures"
category: "statements"
description: "Nesting occurs when one module calls another or executes managed code by referencing a"
tags: ["tsql","statements"]
pubDate: "2026-05-29"
---

Nesting occurs when one module calls another or executes managed code by referencing a

common language runtime (CLR) module, user-defined type, or aggregate. The nesting level

increments when the called module or managed code reference starts execution, and

decrements when the called module or managed code reference finishes. Exceeding the

maximum of 32 nesting levels causes the complete calling chain to fail. The current nesting

level is stored in the

system function.

Because remote stored procedures and extended stored procedures aren't within the scope of

a transaction (unless issued within a

statement or when used

with various configuration options), commands executed through calls to them can't be rolled

back. For more information, see

System stored procedures

and

BEGIN DISTRIBUTED

TRANSACTION.

When you use cursor variables, if you execute a procedure that passes in a cursor variable with

a cursor allocated to it, an error occurs.

You don't have to specify the

keyword when executing modules if the statement is the

first one in a batch.

For more information specific to CLR stored procedures, see

CLR Stored Procedures.

You don't have to specify the

keyword when you execute stored procedures when the

statement is the first one in a batch.

system stored procedures start with the characters. They are physically stored

in the

Resource Database

, but logically appear in the sys schema of every system and user-

defined database. When you execute a system stored procedure, either in a batch or inside a

module such as a user-defined stored procedure or function, we recommend that you qualify

the stored procedure name with the sys schema name.

system extended stored procedures start with the characters

, and these are

contained in the dbo schema of the

database. When you execute a system extended

stored procedure, either in a batch or inside a module such as a user-defined stored procedure

or function, we recommend that you qualify the stored procedure name with.

When you execute a user-defined stored procedure, either in a batch or inside a module such

as a user-defined stored procedure or function, we recommend that you qualify the stored

procedure name with a schema name. We don't recommend that you name a user-defined

stored procedure with the same name as a system stored procedure. For more information

about executing stored procedures, see

Execute a stored procedure.

### varchar(max)

### nvarchar(max)

### sysadmin

```sql
@@NESTLEVEL
```

```sql
BEGIN DISTRIBUTED TRANSACTION
```

`EXECUTE`

`EXECUTE`

`sp_`

`xp_`

`master`

`master.dbo`
