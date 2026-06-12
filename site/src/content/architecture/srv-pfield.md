---
title: "srv_pfield"
topic: "clr-integration"
description: "Returns information about a database connection. srvproc Pointer identifying a database connection."
tags: ["clr-integration","srv-pfield"]
pubDate: "2025-12-01"
---

Returns information about a database connection.

srvproc

Pointer identifying a database connection.

field

Specifies data on the connection to return.

SRV_APPLNAME

The application name provided by the client when it established the

connection.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

ﾉ

Expand table

```sql
DBCHAR * srv_pfield (
SRV_PROC *
srvproc
,
int field
,
int *
len
);
```
