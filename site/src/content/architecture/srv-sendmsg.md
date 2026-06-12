---
title: "srv_sendmsg"
topic: "clr-integration"
description: "Sends a message to the client. ） Important This feature will be removed in a future version of SQL Server. Avoid using this feature in new developm"
tags: ["clr-integration","srv-sendmsg"]
pubDate: "2025-12-01"
---

Sends a message to the client.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

```sql
int srv_sendmsg (
SRV_PROC *
srvproc
,
int msgtype
,
DBINT msgnum
,
DBTINYINT class
,
DBTINYINT state
,
DBCHAR *
rpcname
,
int rpcnamelen
,
DBUSMALLINT linenum
,
DBCHAR *
message
,
```
