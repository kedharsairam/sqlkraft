---
title: "OLE automation objects in T-SQL"
topic: "spatial-data"
description: |
  Article

  •

  01/29/2024

  Applies to:

  SQL Server

  Transact-SQL includes several system stored procedures that allow OLE Automation objects to

  be referenced in Transact-SQL batches, stored procedures,
tags:
  - "spatial-data"
  - "ole-automation-objects-in-t-sql"
pubDate: 2025-12-01
---

Article

•

01/29/2024

SQL Server

Transact-SQL includes several system stored procedures that allow OLE Automation objects to

be referenced in Transact-SQL batches, stored procedures, and triggers. These system stored

procedures run as extended stored procedures, and the OLE Automation objects that are

executed through the stored procedures run in the address space of an instance of the SQL

Server Database Engine in the same way that an extended stored procedure runs.

The OLE Automation stored procedures enable Transact-SQL batches to reference SQL-DMO

objects and custom OLE Automation objects, such as objects that expose the

interface. A custom in-process OLE server that is created by using Microsoft Visual Basic must

have an error handler (specified with the

statement) for the

and

subroutines. Unhandled errors in the

and

subroutines can cause unpredictable errors, such as an access violation in an instance of the

Database Engine. Error handlers for other subroutines are also recommended.

The first step when using an OLE Automation object in Transact-SQL is to call the

system stored procedure to create an instance of the object in the address space of the

instance of the Database Engine.

After an instance of the object has been created, call the following stored procedures to work

with the properties, methods, and error information related to the object:

obtains the value of a property.

sets the value of a property.

calls a method.

obtains the most recent error information.

When there is no more need for the object, call

to deallocate the instance of the

object created by using.

OLE Automation objects return data through property values and methods. The

and

procedures return these data values in the form of a result

set.

The scope of an OLE Automation object is a batch. All references to the object must be

contained in a single batch, stored procedure, or trigger.

```sql
sp_OACreate sp_OAGetProperty sp_OASetProperty sp_OAMethod sp_OAGetErrorInfo sp_OADestroy sp_OACreate sp_OAGetProperty sp_OAMethod
```
