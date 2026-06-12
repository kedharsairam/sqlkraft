---
title: "srv_senddone"
topic: "clr-integration"
description: "Sends a result completion message to the client. srvproc Is a pointer to the SRV_PROC structure that is the handle for a particular client connection"
tags: ["clr-integration","srv-senddone"]
pubDate: 2025-12-01
---

Sends a result completion message to the client.

srvproc

Is a pointer to the SRV_PROC structure that is the handle for a particular client connection (in

this case, the handle that received the language request). The structure contains information

that the Extended Stored Procedure API library uses to manage communication and data

between the application and the client.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

```sql
int srv_senddone (
SRV_PROC *
srvproc
,
DBUSMALLINT status
,
DBUSMALLINT info
,
DBINT count
);
```
