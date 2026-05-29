---
title: "srv_rpcparams"
topic: "clr-integration"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Returns the number of parameters for the current remote stored procedure.

  srvproc

  Is a pointer to the SRV_PROC structure that is the handle for a par
tags:
  - "clr-integration"
  - "srv-rpcparams"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Returns the number of parameters for the current remote stored procedure.

srvproc

Is a pointer to the SRV_PROC structure that is the handle for a particular client connection (in

this case, the handle that received the remote stored procedure). The structure contains

information that the Extended Stored Procedure API library uses to manage communication

and data between the application and the client.

The number of parameters in the remote stored procedure. If there are no parameters in the

remote stored procedure or if there is not a current remote stored procedure, -1 is returned

and an information error occurs.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

```sql
int srv_rpcparams ( SRV_PROC *
srvproc
);
```
