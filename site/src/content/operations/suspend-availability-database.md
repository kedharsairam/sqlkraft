---
title: "Suspend availability database"
topic: "high-availability"
description: |
  Article
  
  •
  
  09/04/2024
  
  Applies to:
  
  SQL Server
  
  You can suspend an availability database in Always On availability groups by using SQL Server
  
  Management Studio, Transact-SQL, or PowerShell in SQL Se
tags:
  - "high-availability"
  - "suspend-availability-database"
pubDate: 2025-12-01
---

Article

•

09/04/2024

Applies to:

SQL Server

You can suspend an availability database in Always On availability groups by using SQL Server

Management Studio, Transact-SQL, or PowerShell in SQL Server. Note that a suspend

command needs to be issued on the server instance that hosts the database to be suspended

or resumed.

The effect of a suspend command depends on whether you suspend a secondary database or

a primary database, as follows:

Secondary

database

Only the local secondary database is suspended and its synchronization state becomes

NOT SYNCHRONIZING. Other secondary databases are not affected. The suspended

database stops receiving and applying data (log records) and begins to fall behind the

primary database. Existing connections on the readable secondary remain usable. New

connections to the suspended database on the readable secondary are not allowed until

data movement is resumed. This behavior only applies when connections are opened

using listener and read-only routing.

The primary database remains available. If you suspend each of the corresponding

secondary databases, the primary database runs exposed.

While a secondary database is suspended, the send queue of the

corresponding primary database will accumulate unsent transaction log records.

Connections to the secondary replica return data that was available at the time the data

movement was suspended.

Primary

database

The primary database stops data movement to every connected secondary database. The

primary database continues running, in an exposed mode. The primary database remains

available to clients, and existing connections on a readable secondary remain usable and

new connections can be made.

ﾉ

Expand table

７

Note

Suspending an Always On secondary database does not directly affect the availability of

the primary database. However, suspending a secondary database can impact redundancy

and failover capabilities for the primary database. This is in contrast to database mirroring,