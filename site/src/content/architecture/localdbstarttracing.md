---
title: "LocalDBStartTracing"
topic: "clr-integration"
description: |
  07/14/2025

  Applies to:

  SQL Server

  Enables tracing of API calls for all the SQL Server Express LocalDB instances owned by the

  current Windows user.

  C++

  : The function succeeded.

  Description

  LOC
tags:
  - "clr-integration"
  - "localdbstarttracing"
pubDate: 2025-12-01
---

07/14/2025

Applies to:

SQL Server

Enables tracing of API calls for all the SQL Server Express LocalDB instances owned by the

current Windows user.

C++

: The function succeeded.

Description

LOCALDB_ERROR_XEVENT_FAILED

Failed to start XEvent engine within the LocalDB Instance API.

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
LocalDBStartTracing ();
```
