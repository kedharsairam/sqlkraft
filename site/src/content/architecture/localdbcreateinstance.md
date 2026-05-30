---
title: "LocalDBCreateInstance"
topic: "clr-integration"
description: |
  07/14/2025

  Applies to:

  SQL Server

  Creates a new SQL Server Express LocalDB instance.

  C++

  [Input] The LocalDB version, for example 11.0 or 11.0.1094.2.

  [Input] The name for the LocalDB instance t
tags:
  - "clr-integration"
  - "localdbcreateinstance"
pubDate: 2025-12-01
---

07/14/2025

Applies to:

SQL Server

Creates a new SQL Server Express LocalDB instance.

C++

[Input] The LocalDB version, for example 11.0 or 11.0.1094.2.

[Input] The name for the LocalDB instance to create.

[Input] Reserved for future use. Currently should be set to 0.

: The function succeeded.

ﾉ

Expand table

```sql
msoledbsql.h
S_OK
HRESULT
LocalDBCreateInstance
(
PCWSTR wszVersion ,
PCWSTR pInstanceName ,
DWORD dwFlags
);
```
