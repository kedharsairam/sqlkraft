---
title: "Manually fail over (SSMS)"
topic: "high-availability"
description: |
  Article

  •

  02/01/2024

  Applies to:

  SQL Server

  When the mirrored database is synchronized (that is, when the database is in the

  SYNCHRONIZED state), the database owner can initiate manual failover
tags:
  - "high-availability"
  - "manually-fail-over-ssms"
pubDate: 2025-12-01
---

Article

•

02/01/2024

SQL Server

When the mirrored database is synchronized (that is, when the database is in the

SYNCHRONIZED state), the database owner can initiate manual failover to the mirror server.

During a manual failover, the principal and mirror server roles are swapped for the database on

which the failover occurs. The mirror database becomes the principal database and the

principal database becomes the mirror. For example, the following table shows the how a

manual failover swaps the roles of two mirroring partners:

and.

PRINCIPAL

MIRROR

MIRROR

PRINCIPAL

Note that the server roles for other database mirroring sessions are not affected. For more

information, see

Role Switching During a Database Mirroring Session (SQL Server).

1. Connect to the principal server instance and, in the

pane, click the server

name to expand the server tree.

2. Expand

, and select the database to be failed over.

3. Right-click the database, select

, and then click. This opens the

page of the

dialog box.

4. Click.

A confirmation box appears. The principal server begins by trying to connect to the mirror

server by using Windows Authentication. If Windows Authentication does not work, the

principal server displays the

dialog box. If the mirror server uses SQL

Server Authentication, select

Authentication

in the

box. In the

text box, specify the login account to connect with on the mirror server, and in the

text box, specify the password for that account.

ﾉ

Expand table

```cmd
SQLDBENGINE0_1
SQLDBENGINE0_2
SQLDBENGINE0_1
SQLDBENGINE0_2
```
