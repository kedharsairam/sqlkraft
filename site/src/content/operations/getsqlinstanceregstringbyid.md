---
title: "GetSQLInstanceRegStringByID"
topic: "event-classes"
description: |
  Article
  
  •
  
  02/07/2024
  
  Retrieves a registry string from an instance specific registry tree by the given instance ID, the
  
  subtree, and the name of the value.
  
  This article describes a native code API
tags:
  - "event-classes"
  - "getsqlinstanceregstringbyid"
pubDate: 2025-12-01
---

Article

•

02/07/2024

Retrieves a registry string from an instance specific registry tree by the given instance ID, the

subtree, and the name of the value.

This article describes a native code API that is used by SQL Server and may also be called by

other Microsoft products. For a managed code method, see

InstAPI.GetSvcInstanceRegStringByName Method

.

C

pInstanceID

[in]

A pointer to the instance ID of the relevant instance.

sRegPath

[in]

A pointer to registry path of the string to retrieve.

sValueName

[in]

A pointer to a string that contains the value name to retrieve.

sString

[out]

A pointer to a buffer to receive the string that will be retrieved.

pdwSize

[out]

A pointer to a

value to supply the length of the buffer. Returns the required length if the

supplied buffer is too small.

```cmd
DWORD
GetSQLInstanceRegStringByID(
PINST_ID  pInstanceID,
LPCWSTR   sRegPath,
LPCWSTR   sValueName,
LPWSTR    sString,
PDWORD    pdwSize
);
```