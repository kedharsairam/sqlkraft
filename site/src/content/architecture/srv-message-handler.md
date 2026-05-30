---
title: "srv_message_handler"
topic: "clr-integration"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  Calls the installed Extended Stored Procedure API message handler. This function is usually

  used to call Microsoft SQL Server from an extended stored
tags:
  - "clr-integration"
  - "srv-message-handler"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

Calls the installed Extended Stored Procedure API message handler. This function is usually

used to call Microsoft SQL Server from an extended stored procedure to log an error (defined

by the extended stored procedure) in the SQL Server error log file or the Microsoft Windows

application log.

）

Important

This feature will be removed in a future version of SQL Server. Avoid using this feature in

new development work, and plan to modify applications that currently use this feature.

Use CLR integration instead.

```sql
int srv_message_handler (
SRV_PROC *
srvproc
,
int errornum
,
BYTE severity
,
BYTE state
,
int oserrnum
,
char *
errtext
,
int errtextlen
,
char *
oserrtext
```
