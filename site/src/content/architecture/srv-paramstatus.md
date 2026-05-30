---
title: "srv_paramstatus"
topic: "clr-integration"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Returns the status of a particular remote stored procedure call parameter.

  srvproc

  Is a pointer to the SRV_PROC structure that is the handle for a pa
tags:
  - "clr-integration"
  - "srv-paramstatus"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Returns the status of a particular remote stored procedure call parameter.

srvproc

Is a pointer to the SRV_PROC structure that is the handle for a particular client connection (in

this case, the handle that received the remote stored procedure call). The structure contains

information the Extended Stored Procedure API library uses to manage communication and

data between the application and the client.

n

Indicates the number of the parameter. The first parameter is number 1.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

```sql
int srv_paramstatus (
SRV_PROC *
srvproc
,
int n
);
```
