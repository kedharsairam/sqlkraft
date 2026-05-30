---
title: "LocalDBFormatMessage"
topic: "clr-integration"
description: |
  07/14/2025

  Applies to:

  SQL Server

  Returns the localized textual description for the specified SQL Server Express LocalDB error.

  C++

  [Input] The LocalDB error code.

  [Input] The flags specifying t
tags:
  - "clr-integration"
  - "localdbformatmessage"
pubDate: 2025-12-01
---

07/14/2025

Applies to:

SQL Server

Returns the localized textual description for the specified SQL Server Express LocalDB error.

C++

[Input] The LocalDB error code.

[Input] The flags specifying the behavior of this function.

Available flags:

If the input buffer is too short, the error message is truncated to fit the buffer.

[Input] The language desired (LANGID) or 0, in which case the Win32 FormatMessage language

order is used.

```sql
msoledbsql.h
HRESULT
LocalDBFormatMessage (
HRESULT hrLocalDB ,
DWORD dwFlags ,
DWORD dwLanguageId ,
LPWSTR wszMessage ,
LPDWORD lpcchMessage
);
```
