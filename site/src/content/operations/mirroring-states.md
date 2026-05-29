---
title: "Mirroring States"
topic: "high-availability"
description: |
  Article
  
  •
  
  02/01/2024
  
  Applies to:
  
  SQL Server
  
  During a database mirroring session, the mirrored database is always in a specific state (the
  
  mirroring state
  
  ). The state of the database reflects t
tags:
  - "high-availability"
  - "mirroring-states"
pubDate: 2025-12-01
---

Article

•

02/01/2024

Applies to:

SQL Server

During a database mirroring session, the mirrored database is always in a specific state (the

mirroring state

). The state of the database reflects the communication status, data flow, and the

difference in data between the partners. The database mirroring session adopts the same state

as the principal database.

Throughout a database mirroring session, the server instances monitor each other. The

partners use the mirroring state to monitor the database. With the exception of the

PENDING_FAILOVER state, the principal and mirror database are always in the same state. If a

witness is set for the session, each of the partners monitors the witness using its connection

state (CONNECTED or DISCONNECTED).

The possible mirroring states of the database are as follows:

Description

SYNCHRONIZING

The contents of the mirror database are lagging behind the contents of the

principal database. The principal server is sending log records to the mirror server,

which is applying the changes to the mirror database to roll it forward.

At the start of a database mirroring session, the database is in the

SYNCHRONIZING state. The principal server is serving the database, and the mirror

is trying to catch up.

SYNCHRONIZED

When the mirror server becomes sufficiently caught up to the principal server, the

mirroring state changes to SYNCHRONIZED. The database remains in this state as

long as the principal server continues to send changes to the mirror server and the

mirror server continues to apply changes to the mirror database.

If transaction safety is set to FULLautomatic failover and manual failover are both

supported in the SYNCHRONIZED state, there is no data loss after a failover.

If transaction safety is off, some data loss is always possible, even in the

SYNCHRONIZED state.

In SQL Server Management Studio the status of the database will show as

Restoring. For actual status, query

column in the

sys.database_mirroring

SUSPENDED

The mirror copy of the database is not available. The principal database is running

without sending any logs to the mirror server, a condition known as

running

ﾉ

Expand table

```cmd
mirroring_state_desc
```