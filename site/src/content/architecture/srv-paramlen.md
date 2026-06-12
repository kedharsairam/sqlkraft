---
title: "srv_paramlen"
topic: "clr-integration"
description: "Returns the data length of a remote stored procedure call parameter. This function has been superseded by the function."
tags: ["clr-integration","srv-paramlen"]
pubDate: 2025-12-01
---

Returns the data length of a remote stored procedure call parameter. This function has been

superseded by the

function.

srvproc

Is a pointer to the SRV_PROC structure that is the handle for a particular client connection (in

this case, the handle that received the remote stored procedure call). The structure contains

information that the Extended Stored Procedure API library uses to manage communication

and data between the application and the client.

n

Indicates the number of the parameter. The first parameter is 1.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

```sql
int srv_paramlen (
SRV_PROC *
srvproc
,
int n
);
```
