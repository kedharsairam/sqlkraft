---
title: "srv_pfieldex"
topic: "clr-integration"
description: "Returns a pointer to data containing the requested SRV_PROC field. srvproc Is a pointer to the SRV_PROC structure that is the handle for a particular"
tags: ["clr-integration","srv-pfieldex"]
pubDate: "2025-12-01"
---

Returns a pointer to data containing the requested SRV_PROC field.

srvproc

Is a pointer to the SRV_PROC structure that is the handle for a particular client connection. The

structure contains information the Extended Stored Procedure API library uses to manage

communication and data between the application and the client.

field

Specifies the

srvproc

field to return.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

ﾉ

Expand table

```sql
void *srv_pfieldex(SRV_PROC *
srvproc
, int field
, int *
len
);
```
