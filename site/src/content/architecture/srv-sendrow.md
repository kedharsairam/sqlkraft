---
title: "srv_sendrow"
topic: "clr-integration"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Transmits a row of data to the client.

  srvproc

  Is a pointer to the SRV_PROC structure that is the handle for a particular client connection (in

  this
tags:
  - "clr-integration"
  - "srv-sendrow"
pubDate: 2025-12-01
---

Article

•

02/28/2023

SQL Server

Transmits a row of data to the client.

srvproc

Is a pointer to the SRV_PROC structure that is the handle for a particular client connection (in

this case, the handle that received the language request). The structure contains information

that the Extended Stored Procedure API library uses to manage communication and data

between the application and the client.

SUCCEED or FAIL.

The

function is called once for each row sent to the client. All rows must be sent

to the client before any messages, status values, or completion statuses are sent with

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

```sql
int srv_sendrow ( SRV_PROC *
srvproc
);
```
