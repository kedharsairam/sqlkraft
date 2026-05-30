---
title: "LocalDBStopInstance"
topic: "clr-integration"
description: |
  07/14/2025

  Applies to:

  SQL Server

  Stops the specified SQL Server Express LocalDB instance from running.

  C++

  [Input] The name of the LocalDB instance to stop.

  [Input] One or a combination of the
tags:
  - "clr-integration"
  - "localdbstopinstance"
pubDate: 2025-12-01
---

07/14/2025

Applies to:

SQL Server

Stops the specified SQL Server Express LocalDB instance from running.

C++

[Input] The name of the LocalDB instance to stop.

[Input] One or a combination of the flag values specifying the way to stop the instance.

Available flags:

Shut down immediately using the terminate process operating system command.

Shut down using the

option Transact-SQL command.

```sql
msoledbsql.h
WITH NOWAIT
HRESULT
LocalDBStopInstance (
PCWSTR pInstanceName ,
DWORD dwFlags ,
ULONG ulTimeout
);
```
