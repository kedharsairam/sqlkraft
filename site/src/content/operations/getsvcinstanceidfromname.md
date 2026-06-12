---
title: "GetSvcInstanceIDFromName"
topic: "event-classes"
description: "Retrieves the instance ID of an instance when given the friendly name, conditioned to search only the instance maps for the given service."
tags: ["event-classes","getsvcinstanceidfromname"]
pubDate: "2025-12-01"
---

Retrieves the instance ID of an instance when given the friendly name, conditioned to search

only the instance maps for the given service.

This article describes a native code API that is used by SQL Server and may also be called by

other Microsoft products. For a managed code method, see

InstAPI.GetSvcInstanceIDFromName Method.

C

sInstanceName

[in]

A pointer to the instance ID of the relevant instance.

Service

[in]

The service type of the server whose instance ID is being looked for.

pInstanceID

[out]

A pointer to a buffer to receive the instance ID.

Boolean

if the call succeeded; otherwise,.

```cmd
true false
GetSvcInstanceIDFromName(
LPCWSTR sInstanceName,
SQL_SVCS Service,
PINST_ID pInstanceID
);
```
