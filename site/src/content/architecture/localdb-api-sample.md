---
title: "LocalDB API sample"
topic: "clr-integration"
description: "Express LocalDB reference 07/14/2025 This section contains information about the SQL Server Express LocalDB: SQL Server Express LocalDB error messages SQL Serve"
tags: ["clr-integration","localdb-api-sample"]
pubDate: "2025-12-01"
---

Express LocalDB reference

This section contains information about the SQL Server Express LocalDB:

Express LocalDB error messages

Express LocalDB instance APIs

The following sample demonstrates the LocalDB API. Make sure that LocalDB is installed on the

computer before running this sample. You can install LocalDB from setup in SQL Server Express.

C++

```sql
// compile with: Advapi32.lib
#include <SDKDDKVer.h>
#include <stdio.h>
// To use LocalDB API, you must define LOCALDB_DEFINE_PROXY_FUNCTIONS before you include msoledbsql.h in one (and only one) of the
// source files in your program. LOCALDB_DEFINE_PROXY_FUNCTIONS causes code to be generated that binds to the LocalDB API at runtime.
#define LOCALDB_DEFINE_PROXY_FUNCTIONS
#include "msoledbsql.h"
HRESULT
CreateAndStartLocalDBInstance (PWCHAR wszVersion, PWCHAR wszInstanceName) {
HRESULT hr;
if (SUCCEEDED(hr = LocalDBCreateInstance(wszVersion, wszInstanceName, 0))) hr = LocalDBStartInstance(wszInstanceName, 0,
NULL
,
NULL
);
return hr;
}
HRESULT
StopAndDeleteLocalDBInstance (PWCHAR wszInstanceName) {
HRESULT hr;
if (SUCCEEDED(hr = LocalDBStopInstance(wszInstanceName, 0, 30)))
// 30 seconds timeout hr = LocalDBDeleteInstance(wszInstanceName, 0);
return hr;
}
void
PrintLocalDBError (HRESULT hr) {
```
