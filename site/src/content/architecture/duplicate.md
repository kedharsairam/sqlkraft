---
title: "Duplicate"
topic: "tables"
description: "2016 (13.x) and later versions Azure SQL Managed Instance You"
tags: ["tables","duplicate"]
pubDate: "2025-12-01"
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

Analytics Platform System (PDW)

You can duplicate an existing table in SQL Server by using SQL Server Management Studio or

Transact-SQL by creating a new table and then copying column information from an existing

table.

These steps described duplicate only the structure of a table, not the row data.

Requires

permission in the destination database.

1. Make sure you are connected to the database in which you want to create the table and

that the database is selected in.

2. In

, right-click

and select

and then.

3. In

right-click the table you want to copy, and select. The existing

table opens in a separate tab.

4. Select the columns in the existing table and, from the

menu, select

, or

to copy the column information to your clipboard.

5. Switch back to the new table tab and select the first column of the first row.

6. From the

menu, select

or

to paste.

7. From the

menu, select

table name

, or

to save.

8. In the

dialog box, type a name for the new table. Select. The table will

be created and visible in the.

```sql
CREATE TABLE
Ctrl+C
Ctrl+V
Ctrl+S
```
