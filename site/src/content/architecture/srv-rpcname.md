---
title: "srv_rpcname"
topic: "clr-integration"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Returns the procedure name component for the current remote stored procedure.

  srvproc

  Is a pointer to the SRV_PROC structure that is the handle for a
tags:
  - "clr-integration"
  - "srv-rpcname"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Returns the procedure name component for the current remote stored procedure.

srvproc

Is a pointer to the SRV_PROC structure that is the handle for a particular client connection (in

this case, the handle that received the remote stored procedure). The structure contains

information that the Extended Stored Procedure API library uses to manage communication

and data between the application and the client.

len

Is a pointer to an integer variable that receives the length of the database name. If

len

is NULL,

the length of the remote stored procedure name is not returned.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

```sql
DBCHAR * srv_rpcname (
SRV_PROC *
srvproc
,
int *
len
);
```
