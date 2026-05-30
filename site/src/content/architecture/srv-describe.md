---
title: "srv_describe"
topic: "clr-integration"
description: |
  Article

  •

  04/15/2024

  Applies to:

  SQL Server

  Defines the column name and source and destination data types for a specific column in a row.

  ）

  Important

  This feature will be removed in a future v
tags:
  - "clr-integration"
  - "srv-describe"
pubDate: 2025-12-01
---

Article

•

04/15/2024

Applies to:

SQL Server

Defines the column name and source and destination data types for a specific column in a row.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

```sql
int srv_describe (
SRV_PROC *
srvproc
,
int colnumber
,
DBCHAR *
column_name
,
int namelen
,
DBINT desttype
,
DBINT destlen
,
DBINT srctype
,
DBINT srclen
,
void *
```
