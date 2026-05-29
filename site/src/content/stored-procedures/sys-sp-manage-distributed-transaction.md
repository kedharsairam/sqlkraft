---
name: 'sys.sp_manage_distributed_transaction'
title: 'sys.sp_manage_distributed_transaction'
category: 'general'
description: 'SQL Server 2022 (16.x)'
tags: ["stored-procedure"]
pubDate: 2026-05-29
---

## Description
Help context ID in the Help source file.

Each call to an OLE Automation stored procedure (except

) resets the error

information; therefore,

obtains error information only for the most recent

OLE Automation stored procedure call. Because

doesn't reset the error

information, it can be called multiple times to get the same error information.

The following table lists OLE Automation errors and their common causes.

Data type of a Transact-SQL value passed as a method parameter didn't

match the Microsoft Visual Basic data type of the method parameter, or a

value was passed as a method parameter.

Specified property or method name wasn't found for the specified object.

Specified ProgID or CLSID isn't registered as an OLE object on an instance

of SQL Server. Custom OLE automation servers must be registered before

they can be instantiated using

. You can register servers using

the

utility for in-process (

) servers, or the

command-line switch for local (

) servers.

Specified OLE object is registered as a local OLE server (

file) but the

.exe file couldn't be found or started.

Specified OLE object is registered as an in-process OLE server (

file),

but the .dll file couldn't be found or loaded.

Data type of a Transact-SQL local variable that is used to store a returned

property value or a method return value didn't match the Visual Basic data

type of the property or method return value. Or, the return value of a

property or a method was requested, but it doesn't return a value.

The value of the context parameter should be one of: 1, 4, or 5.

ﾉ

Expand table

```sql
HelpID
```

```sql
sp_OAGetErrorInfo
```

```sql
sp_OAGetErrorInfo
```

```sql
sp_OAGetErrorInfo
```

```sql
NULL
```

```sql
sp_OACreate
```

```sql
Regsvr32.exe
```

```sql
.dll
```

```sql
/REGSERVER
```

```sql
.exe
```

```sql
.exe
```

```sql
.dll
```

```sql
sp_OACreate
```
