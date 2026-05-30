---
title: "LocalDBGetVersions"
topic: "clr-integration"
description: |
  07/14/2025

  Applies to:

  SQL Server

  Returns all SQL Server Express LocalDB versions available on the computer.

  C++

  [Output] Contains names of the LocalDB versions that are available on the user's w
tags:
  - "clr-integration"
  - "localdbgetversions"
pubDate: 2025-12-01
---

07/14/2025

Applies to:

SQL Server

Returns all SQL Server Express LocalDB versions available on the computer.

C++

[Output] Contains names of the LocalDB versions that are available on the user's workstation.

[Input/Output] On input holds the number of slots for versions in the

pVersionNames

buffer.

On output, holds the number of existing LocalDB versions.

: The function succeeded.

Description

LOCALDB_ERROR_NOT_INSTALLED

SQL Server Express LocalDB isn't installed on the computer.

ﾉ

Expand table

```sql
msoledbsql.h
S_OK
#define MAX_LOCALDB_VERSION_LENGTH 43typedef WCHAR TLocalDBVersion [
MAX_LOCALDB_VERSION_LENGTH + 1 ] ;
typedef
TLocalDBVersion* PTLocalDBVersion;
HRESULT
LocalDBGetVersions (
PTLocalDBVersion pVersion ,
LPDWORD lpdwNumberOfVersions);
```
