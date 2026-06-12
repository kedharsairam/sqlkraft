---
title: "LocalDBStartInstance"
topic: "clr-integration"
description: "07/14/2025 Starts the specified SQL Server Express LocalDB instance. C++ [Input] The name of the LocalDB instance to start. [Input] Reserved for future use."
tags: ["clr-integration","localdbstartinstance"]
pubDate: "2025-12-01"
---

Starts the specified SQL Server Express LocalDB instance.

C++

[Input] The name of the LocalDB instance to start.

[Input] Reserved for future use. Currently should be set to 0.

[Output] The buffer to store the connection string to the LocalDB instance.

[Input/Output] On input contains the size of the

wszSqlConnection

buffer in characters,

including any trailing nulls. On output, if the given buffer size is too small, contains the

required buffer size in characters, including any trailing nulls.

```sql
msoledbsql.h
HRESULT
LocalDBStartInstance (
PCWSTR pInstanceName ,
DWORD dwFlags ,
LPWSTR wszSqlConnection ,
LPDWORD lpcchSqlConnection
);
```
