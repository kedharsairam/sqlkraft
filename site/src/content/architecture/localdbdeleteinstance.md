---
title: "LocalDBDeleteInstance"
topic: "clr-integration"
description: |
  07/14/2025

  Applies to:

  SQL Server

  Removes the specified SQL Server Express LocalDB instance.

  C++

  [Input] The name of the LocalDB instance to remove.

  [Input] Reserved for future use. Currently sh
tags:
  - "clr-integration"
  - "localdbdeleteinstance"
pubDate: 2025-12-01
---

07/14/2025

Applies to:

SQL Server

Removes the specified SQL Server Express LocalDB instance.

C++

[Input] The name of the LocalDB instance to remove.

[Input] Reserved for future use. Currently should be set to 0.

: The function succeeded.

Description

LOCALDB_ERROR_NOT_INSTALLED

SQL Server Express LocalDB isn't installed on

the computer.

LOCALDB_ERROR_INVALID_PARAMETER

One or more specified input parameters are

invalid.

ﾉ

Expand table

```sql
msoledbsql.h
S_OK
HRESULT
LocalDBDeleteInstance (
PCWSTR pInstanceName ,
DWORD dwFlags
);
```
