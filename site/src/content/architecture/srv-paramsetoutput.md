---
title: "srv_paramsetoutput"
topic: "clr-integration"
description: |
  Article
  
  •
  
  03/03/2023
  
  Applies to:
  
  SQL Server
  
  Sets the value of a return parameter. This function supersedes the
  
  function.
  
  srvproc
  
  Is a handle for a client connection.
  
  n
  
  Is the ordinal number 
tags:
  - "clr-integration"
  - "srv-paramsetoutput"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

Sets the value of a return parameter. This function supersedes the

function.

srvproc

Is a handle for a client connection.

n

Is the ordinal number of the parameter to be set. The first parameter is 1.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

```sql
int srv_paramsetoutput (
SRV_PROC *
srvproc
,
int
n
,
BYTE *
pbData
,
ULONG
cbLen
,
BOOL
fNull
);
```