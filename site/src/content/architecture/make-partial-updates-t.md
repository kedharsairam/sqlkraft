---
title: "Make Partial Updates t"
topic: "filestream"
description: "An application uses FSCTL_SQL_FILESTREAM_FETCH_OLD_CONTENT to make partial updates to FILESTREAM BLOB data."
tags: ["filestream","make-partial-updates-t"]
pubDate: "2025-12-01"
---

An application uses FSCTL_SQL_FILESTREAM_FETCH_OLD_CONTENT to make partial updates to

FILESTREAM BLOB data. The

DeviceIoControl

function passes this value and the handle that is

returned from

OpenSqlFilestream

to the FILESTREAM driver. The driver then forces a server-

side copy of the current FILESTREAM data into the file that is referenced by the handle. If the

application issues the FSCTL_SQL_FILESTREAM_FETCH_OLD_CONTENT value after the handle

has been written to, the last write operation persists and previous write operations that were

made to the handle are lost.

The following example shows you how to use the

value to perform a partial update of an inserted FILESTREAM BLOB.

C++

７

Note

FILESTREAM relies on the

for remote access.

７

Note

This example requires the FILESTREAM-enabled database and table that are created in

and.

```sql
FSCTL_SQL_FILESTREAM_FETCH_OLD_CONTENT
#include <windows.h>
#include<sqlext.h>
#include <stdio.h>
#include <msodbcsql.h>
#include <tchar.h>
#include <strsafe.h>
/// <summary>
///This class iterates though the ODBC error queue and prints all of the
///accumulated error messages to the console.
/// </summary>
class
ODBCErrors
```
