---
title: "LocalDBStopTracing"
topic: "clr-integration"
description: |
  07/14/2025
  
  Applies to:
  
  SQL Server
  
  Disables tracing of API calls for all the SQL Server Express LocalDB instances owned by the
  
  current Windows user.
  
  C++
  
  : The function succeeded.
  
  Description
  
  LO
tags:
  - "clr-integration"
  - "localdbstoptracing"
pubDate: 2025-12-01
---

07/14/2025

Applies to:

SQL Server

Disables tracing of API calls for all the SQL Server Express LocalDB instances owned by the

current Windows user.

C++

: The function succeeded.

Description

LOCALDB_ERROR_INTERNAL_ERROR

An unexpected error occurred. See the event log for details.

For a code sample that uses LocalDB API, see

SQL Server Express LocalDB reference

.

SQL Server Express LocalDB header and version information

ﾉ

Expand table

```sql
msoledbsql.h
S_OK
HRESULT
LocalDBStopTracing
();
```