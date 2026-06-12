---
title: "LocalDBGetInstanceInfo"
topic: "clr-integration"
description: ""
tags: ["clr-integration","localdbgetinstanceinfo"]
pubDate: 2025-12-01
---

Returns information for the specified SQL Server Express LocalDB instance, such as whether it

exists, the LocalDB version it uses, whether it's running, and so on.

The information is returned in a

named

, which has the following

definition.

C++

```sql
struct
LocalDBInstanceInfo typedef struct
_
LocalDBInstanceInfo
{
// Contains the size of the LocalDBInstanceInfo struct
DWORD cbLocalDBInstanceInfoSize;
// Holds the instance name
TLocalDBInstanceNamewszInstanceName;
// TRUE if the instance files exist on disk, FALSE otherwise
BOOL bExists;
// TRUE if the instance configuration registry is corrupted, FALSE otherwise
BOOLbConfigurationCorrupted;
// TRUE if the instance is running at the moment, FALSE otherwise
BOOL bIsRunning;
// Holds the LocalDB version for the instance in the format:
major.minor.build.revision
DWORD dwMajor;
DWORD dwMinor;
DWORD dwBuild;
DWORD dwRevision;
// Holds the date and time when the instance was started for the last time
FILETIME ftLastStartUTC;
// Holds the name of the TDS named pipe to connect to the instance
WCHARwszConnection;
// TRUE if the instance is shared, FALSE otherwise
BOOLbIsShared;
// Holds the shared name for the instance (if the instance is shared)
TLocalDBInstanceNamewszSharedInstanceName;
// Holds the SID of the instance owner (if the instance is shared)
WCHARwszOwnerSID;
```
