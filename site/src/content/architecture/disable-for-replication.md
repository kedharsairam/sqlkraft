---
title: "Disable for replication"
topic: "tables"
description: "2016 (13.x) and later versions Azure SQL Managed Instance You"
tags: ["tables","disable-for-replication"]
pubDate: "2025-12-01"
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

Analytics Platform System (PDW)

You can disable check constraints in SQL Server by using SQL Server Management Studio or

Transact-SQL. You can also explicitly disable check constraints for replication, which can be

useful if you are publishing data from a previous version of SQL Server.

Requires ALTER permission on the table.

1. In

, expand the table with the check constraint you want to modify, and

then expand the

folder.

2. Right-click the check constraint you wish to modify and then click.

3. In the

dialog box, under

, select a value of

for.

７

Note

If a table is published using replication, check constraints are automatically disabled for

operations performed by replication agents. When a replication agent performs an insert,

update, or delete at a Subscriber, the constraint is not checked; if a user performs an

insert, update, or delete, the constraint is checked. The constraint is disabled for the

replication agent because the constraint was already checked at the Publisher when the

data was originally inserted, updated, or deleted. For more information, see.
