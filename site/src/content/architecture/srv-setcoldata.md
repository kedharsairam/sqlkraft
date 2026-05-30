---
title: "srv_setcoldata"
topic: "clr-integration"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Specifies the current address for a column's data.

  srvproc

  Is a pointer to the SRV_PROC structure that is the handle for a particular client connecti
tags:
  - "clr-integration"
  - "srv-setcoldata"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Specifies the current address for a column's data.

srvproc

Is a pointer to the SRV_PROC structure that is the handle for a particular client connection. The

structure contains information the Extended Stored Procedure API library uses to manage

communication and data between the application and the client.

column

Indicates the number of the column the address is being specified for. Columns are numbered

beginning with 1.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

```sql
int srv_setcoldata (
SRV_PROC *
srvproc
,
int
column
,
void *
data
);
```
