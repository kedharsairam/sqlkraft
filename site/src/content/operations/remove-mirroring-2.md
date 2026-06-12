---
title: "Remove Mirroring"
topic: "high-availability"
description: |
  Article

  •

  02/01/2024

  Applies to:

  SQL Server

  The database owner can manually stop a database mirroring session at any time, at either

  partner.

  When mirroring is removed, the following occurs:

  T
tags:
  - "high-availability"
  - "remove-mirroring-2"
pubDate: 2025-12-01
---

Article

•

02/01/2024

SQL Server

The database owner can manually stop a database mirroring session at any time, at either

partner.

When mirroring is removed, the following occurs:

The relationship between the partners and between each partner and the witness breaks

permanently, if any relationship exists.

If the partners are communicating with each other when the session is stopped, their

relationship is immediately broken on both computers. If the partners are not

communicating (the database is in a DISCONNECTED state at the time of stopping), the

relationship is broken immediately on the partner from which mirroring is stopped; when

the other partner tries to reconnect, it discovers that the database mirroring session has

ended.

Information about the mirroring session is dropped, unlike when pausing a session.

Mirroring is removed on both the principal database and the mirror database. In

, the

column and all other mirroring columns are set to

NULL. For more information, see

sys.database_mirroring (Transact-SQL).

Each partner server instance is left with a separate copy of the database.

The mirror database is left in the RESTORING state (see the

column of

), because the mirror database was created by using RESTORE WITH

NORECOVERY. At this point, you can drop the former mirror database or restore it using

WITH RECOVERY. When you recover the database, it will have diverged from the former

principal database because the recovery starts a new recovery fork.

７

Note

To continue mirroring after stopping a session, you must establish a new database

mirroring session. If you create a log backup after stopping mirroring, you must apply it to

the mirror database before restarting mirroring.
