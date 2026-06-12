---
title: "srv_rpcnumber"
topic: "clr-integration"
description: "Returns the number component for the current remote stored procedure call."
tags: ["clr-integration","srv-rpcnumber"]
pubDate: "2025-12-01"
---

Returns the number component for the current remote stored procedure call.

srvproc

Is a pointer to the SRV_PROC structure that is the handle for a particular client connection (in

this case, the handle that received the remote stored procedure). The structure contains

information that the Extended Stored Procedure API library uses to manage communication

and data between the application and the client.

The number component for the current remote stored procedure. If the client does not use a

number component when running the remote stored procedure or if there is no current

remote stored procedure, it returns - 1.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

```sql
int srv_rpcnumber ( SRV_PROC *
srvproc
)
```
