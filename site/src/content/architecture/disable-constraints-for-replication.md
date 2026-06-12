---
title: "Disable constraints for replication"
topic: "tables"
description: "2016 (13.x) and later versions Azure SQL Managed Instance You"
tags: ["tables","disable-constraints-for-replication"]
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

Analytics Platform System (PDW)

You can disable foreign key constraints for replication in SQL Server by using SQL Server

Management Studio or Transact-SQL. This can be useful if you are publishing data from a

previous version of SQL Server.

Requires ALTER permission on the table.

1. In

, expand the table with the foreign key constraint you want to modify,

and then expand the

folder.

2. Right-click the foreign key constraint and then select.

3. In the

dialog box, select a value of

for.

4. Select.

７

Note

If a table is published using replication, foreign key constraints are automatically disabled

for operations performed by replication agents. The NOT FOR REPLICATION option is

specified by default for foreign key constraints and check constraints; the constraints are

enforced for user operations but not agent operations. When a replication agent performs

an insert, update, or delete at a Subscriber, the constraint is not checked; if a user

performs an insert, update, or delete, the constraint is checked. The constraint is disabled

for the replication agent because the constraint was already checked at the Publisher

when the data was originally inserted, updated, or deleted.
