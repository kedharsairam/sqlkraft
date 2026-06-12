---
title: "Disable constraints with INSERT & UPDATE"
topic: "tables"
description: "2016 (13.x) and later versions Azure SQL Managed Instance You"
tags: ["tables","disable-constraints-with-insert-update"]
pubDate: 2025-12-01
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

Analytics Platform System (PDW)

You can disable a foreign key constraint during INSERT and UPDATE transactions in SQL Server

by using SQL Server Management Studio or Transact-SQL. Use this option if you know that new

data will not violate the existing constraint or if the constraint applies only to the data already

in the database.

After you disable these constraints, future inserts or updates to the column will not be

validated against the constraint conditions.

Requires ALTER permission on the table.

1. In

, expand the table with the constraint and then expand the

folder.

2. Right-click the constraint and select.

3. In the grid under

, select

and select

from the drop-down menu.

4. Select.

5. To re-enable the constraint when desired, reverse the above steps. Select

and select

from the drop-down menu.

6. To trust the constraint by checking the existing data in the foreign key's relationship,

select

and select

from the drop-

down menu. This would ensure the foreign key constraint is trusted.
