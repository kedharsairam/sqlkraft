---
title: "srv_setutype"
topic: "clr-integration"
description: "Sets the user-defined data type for a column in a row."
tags: ["clr-integration","srv-setutype"]
pubDate: 2025-12-01
---

Sets the user-defined data type for a column in a row.

srvproc

Is a pointer to the SRV_PROC structure that is the handle for a particular client connection. The

structure contains information the Extended Stored Procedure API library uses to manage

communication and data between the application and the client.

column

Indicates which column to set. Columns are numbered beginning with 1.

user_type

Specifies the user-defined data type code.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

```sql
int srv_setutype (
SRV_PROC *
srvproc
,
int column
,
DBINT user_type
);
```
