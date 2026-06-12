---
title: "srv_convert"
topic: "clr-integration"
description: "Changes data from one data type to another. ） Important This feature will be removed in a future version of SQL Server."
tags: ["clr-integration","srv-convert"]
pubDate: 2025-12-01
---

Changes data from one data type to another.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

```sql
int srv_convert (
SRV_PROC *
srvproc
,
int srctype
,
void *
src
,
DBINT srclen
,
int desttype
,
void *
dest
,
DBINT destlen
);
```
