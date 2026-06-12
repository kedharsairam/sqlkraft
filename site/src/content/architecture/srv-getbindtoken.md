---
title: "srv_getbindtoken"
topic: "clr-integration"
description: "Obtains a bind token of the transaction in the current client session that invokes the extended stored procedure. The extended stored procedure can t"
tags: ["clr-integration","srv-getbindtoken"]
pubDate: "2025-12-01"
---

Obtains a bind token of the transaction in the current client session that invokes the extended

stored procedure.

The extended stored procedure can then use

to bind any new session it creates

against the same server to the existing transaction so that the new session can share the same

transaction lock space with the client session that invoked the extended stored procedure.

srvproc

Is a pointer to the SRV_PROC structure that is the handle for a particular client connection. The

structure contains all the information that the Extended Stored Procedure API library uses to

manage communications and data between the application and the client.

bindtoken

Is a pointer to a buffer where the bind token will be copied. The bind token is represented as a

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

```sql
int srv_getbindtoken (
SRV_PROC*
srvproc
,
char*
bindtoken
);
```
