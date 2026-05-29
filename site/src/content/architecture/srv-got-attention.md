---
title: "srv_got_attention"
topic: "clr-integration"
description: |
  Article
  
  •
  
  02/28/2023
  
  Applies to:
  
  SQL Server
  
  Checks whether the current connection or task needs to be aborted and returns TRUE if the
  
  connection is killed or the batch is aborted
  
  srvproc
  
  Point
tags:
  - "clr-integration"
  - "srv-got-attention"
pubDate: 2025-12-01
---

Article

•

02/28/2023

Applies to:

SQL Server

Checks whether the current connection or task needs to be aborted and returns TRUE if the

connection is killed or the batch is aborted

srvproc

Pointer identifying a database connection.

TRUE if the connection is killed or the batch is aborted. FALSE if the connection or batch is

active.

A long-running extended stored procedure should check the server attention by calling

periodically so that the procedure may terminate itself when the connection

is killed or the batch is aborted.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

```sql
BOOL srv_got_attention (SRV_PROC *
srvproc
);
```