---
title: "LocalDBGetInstances"
topic: "clr-integration"
description: |
  07/14/2025

  Applies to:

  SQL Server

  Returns all SQL Server Express LocalDB instances with the given version.

  C++

  [Output] When this function returns, contains the names of both named and default Lo
tags:
  - "clr-integration"
  - "localdbgetinstances"
pubDate: 2025-12-01
---

07/14/2025

SQL Server

Returns all SQL Server Express LocalDB instances with the given version.

C++

[Output] When this function returns, contains the names of both named and default LocalDB

instances on the user's workstation.

[Input/Output] On input, this option contains the number of slots for instance names in the

pInstanceNames

buffer. On output, this option contains the number of LocalDB instances found

on the user's workstation.

: The function succeeded.

ﾉ

Expand table

```sql
msoledbsql.h
S_OK
#define MAX_LOCALDB_INSTANCE_NAME_LENGTH 128typedef WCHAR TLocalDBInstanceName [
MAX_LOCALDB_INSTANCE_NAME_LENGTH + 1 ] ;
typedef
TLocalDBInstanceName* PTLocalDBInstanceName;
HRESULT
LocalDBGetInstances (
PTLocalDBInstanceName pInstanceNames ,
LPDWORD lpdwNumberOfInstances
);
```
