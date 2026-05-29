---
title: "Remove the witness"
topic: "high-availability"
description: |
  Article

  •

  04/15/2024

  Applies to:

  SQL Server

  This topic describes how to remove a witness from a database mirroring session in SQL Server

  by using SQL Server Management Studio or Transact-SQL. At
tags:
  - "high-availability"
  - "remove-the-witness"
pubDate: 2025-12-01
---

Article

•

04/15/2024

Applies to:

SQL Server

This topic describes how to remove a witness from a database mirroring session in SQL Server

by using SQL Server Management Studio or Transact-SQL. At any time during a database

mirroring session, the database owner can turn off the witness for a database mirroring

session.

Security

SQL Server Management Studio

Transact-SQL

After Removing the Witness

Requires ALTER permission on the database.

1. Connect to the principal server instance and, in the

pane, click the server

name to expand the server tree.

2. Expand

, and select the database whose witness you want to remove.
