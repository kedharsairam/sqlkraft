---
title: "srv_rpcoptions"
topic: "clr-integration"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Returns run-time options for the current remote stored procedure.

  srvproc

  Is a pointer to the SRV_PROC structure that is the handle for a particular
tags:
  - "clr-integration"
  - "srv-rpcoptions"
pubDate: 2025-12-01
---

Article

•

02/28/2023

SQL Server

Returns run-time options for the current remote stored procedure.

srvproc

Is a pointer to the SRV_PROC structure that is the handle for a particular client connection (in

this case, the handle that received the remote stored procedure). The structure contains

information the Extended Stored Procedure API library uses to manage communication and

data between the application and the client.

A bitmap that contains the run-time flags joined in a logical OR for the current remote stored

procedure. If there is not a current remote stored procedure, 0 is returned and a message is

generated.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

```sql
DBUSMALLINT srv_rpcoptions ( SRV_PROC *
srvproc
);
```
