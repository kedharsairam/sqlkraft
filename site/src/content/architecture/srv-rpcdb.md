---
title: "srv_rpcdb"
topic: "clr-integration"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Returns the database name component for the current remote stored procedure.

  srvproc

  Is a pointer to the SRV_PROC structure that is the handle for a
tags:
  - "clr-integration"
  - "srv-rpcdb"
pubDate: 2025-12-01
---

Article

•

02/28/2023

SQL Server

Returns the database name component for the current remote stored procedure.

srvproc

Is a pointer to the SRV_PROC structure that is the handle for a particular client connection. The

structure contains information the Extended Stored Procedure API library uses to manage

communication and data between the application and the client.

len

Is a pointer to an

variable that receives the length of the database name. If

len

is NULL, the

length of the database name is not returned.

A DBCHAR pointer to the null-terminated string for the database name part of the current

remote stored procedure. If there is no current remote stored procedure, NULL is returned and

the

len

parameter is set to - 1.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

```sql
DBCHAR * srv_rpcdb (
SRV_PROC * srvproc,int *len );
```
