---
title: "srv_wsendmsg"
topic: "clr-integration"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Sends a Unicode message to the client.

  srvproc

  Is a pointer to the SRV_PROC structure that is the handle for a particular client connection. The

  str
tags:
  - "clr-integration"
  - "srv-wsendmsg"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Sends a Unicode message to the client.

srvproc

Is a pointer to the SRV_PROC structure that is the handle for a particular client connection. The

structure contains information the Extended Stored Procedure API library uses to manage

communication and data between the application and the client.

Msgnum

Is a 4-byte message number.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

```sql
int srv_wsendmsg(SRV_PROC *
srvproc
, int msgnum
, int severity
, WCHAR *
message
, int msglen
);
```
