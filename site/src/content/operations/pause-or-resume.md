---
title: "Pause or resume"
topic: "high-availability"
description: |
  Article

  •

  02/01/2024

  Applies to:

  SQL Server

  This topic describes how to pause or resume database mirroring in SQL Server by using SQL

  Server Management Studio or Transact-SQL.

  Security

  SQL Ser
tags:
  - "high-availability"
  - "pause-or-resume"
pubDate: 2025-12-01
---

Article

•

02/01/2024

Applies to:

SQL Server

This topic describes how to pause or resume database mirroring in SQL Server by using SQL

Server Management Studio or Transact-SQL.

Security

SQL Server Management Studio

Transact-SQL

After Pausing or Resuming Database Mirroring

At any time, you can suspend a database mirroring session, which might improve performance

during bottlenecks, and you can resume a suspended session at any time.

Requires ALTER permission on the database.

Ｕ

Caution

After a forced service, when the original principal server reconnects, mirroring is

suspended. Resuming mirroring in this situation could possibly cause data loss on the

original principal server. For information about managing the potential data loss, see

.
