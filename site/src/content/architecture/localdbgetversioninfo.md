---
title: "LocalDBGetVersionInfo"
topic: "clr-integration"
description: ""
tags: ["clr-integration","localdbgetversioninfo"]
pubDate: 2025-12-01
---

Returns information for the specified SQL Server Express LocalDB version, such as whether it

exists and the full LocalDB version number (including build and release numbers).

The information is returned in the form of a

named

, which has the

following definition.

C++

C++

```sql
struct
LocalDBVersionInfo msoledbsql.h typedef struct
_
LocalDBVersionInfo
{
// Contains the size of the LocalDBVersionInfo struct
DWORD cbLocalDBVersionInfoSize;
// Holds the version name
TLocalDBVersionwszVersion;
// TRUE if the instance files exist on disk, FALSE otherwise
BOOL bExists;
// Holds the LocalDB version for the instance in the format:
major.minor.build.revision
DWORD dwMajor;
DWORD dwMinor;
DWORD dwBuild;
DWORD dwRevision;
} LocalDBVersionInfo;
HRESULT
LocalDBGetVersionInfo (
PCWSTR wszVersionName ,
PLocalDBVersionInfo pVersionInfo ,
DWORD dwVersionInfoSize);
```
