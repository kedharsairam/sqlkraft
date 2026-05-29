---
title: "View states"
topic: "high-availability"
description: |
  Article

  •

  02/01/2024

  Applies to:

  SQL Server

  During a database mirroring session, you can view the status on the

  page of the

  dialog box.

  1. After connecting to the principal server instance, in
tags:
  - "high-availability"
  - "view-states"
pubDate: 2025-12-01
---

Article

•

02/01/2024

Applies to:

SQL Server

During a database mirroring session, you can view the status on the

page of the

dialog box.

1. After connecting to the principal server instance, in Object Explorer, click the server name

to expand the server tree.

2. Expand

, and select the database to be mirrored.

3. Right-click the database, select

, and then click

. This opens the

page of the

dialog box.

4. After mirroring begins, the

panel displays the status of the database mirroring

session as of when you selected the

page or clicked the

button. The

possible states are as follows:

<blank>

No database mirroring session exists and there is no activity to report on the

page.

Paused

The principal database is running but is not sending any logs to the mirror server.

The mirror copy of the database is not available.

No

connection

The principal server instance cannot connect to its partner or to the witness server

instance (if any)

Synchronizing

The contents of the mirror database are lagging behind the contents of the

principal database. The principal server instance is sending log records to the

mirror server instance, which is applying the changes to the mirror database to roll

it forward.

At the start of a database mirroring session, the mirror and principal databases are

in the synchronizing state.

Failover

On the principal server instance, a manual failover (role swap) has begun but has

not yet accepted by the mirror.

ﾉ

Expand table
