---
title: "srv_paraminfo"
topic: "clr-integration"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  Returns information about a parameter. This function supersedes the following functions:

  srv_paramtype

  ,

  srv_paramlen

  ,

  srv_parammaxlen

  , and

  sr
tags:
  - "clr-integration"
  - "srv-paraminfo"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Returns information about a parameter. This function supersedes the following functions:

srv_paramtype

,

srv_paramlen

,

srv_parammaxlen

, and

srv_paramdata

.

supports

the data types in

Data Types

and zero-length data.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

```sql
int srv_paraminfo (
SRV_PROC *
srvproc
,
int n
,
BYTE *
pbType
,
ULONG *
pcbMaxLen
,
ULONG *
pcbActualLen
,
BYTE *
pbData
,
BOOL *
pfNull
);
```
