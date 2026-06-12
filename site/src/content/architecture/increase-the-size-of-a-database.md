---
title: "Increase the size of a database"
topic: "collation"
description: "This article describes how to increase the size of a database in SQL Server by using SQL Server Management Studio or Transact-SQL."
tags: ["collation","increase-the-size-of-a-database"]
pubDate: 2025-12-01
---

This article describes how to increase the size of a database in SQL Server by using SQL Server

Management Studio or Transact-SQL. The database is expanded by either increasing the size of

an existing data or log file, or by adding a new file to the database.

You can't add or remove a file while a

statement is running.

Requires

permission on the database.

1. In

, connect to an instance of the SQL Server Database Engine, and then

expand that instance.

2. Expand

, right-click the database to increase, and then select.

3. In

, select the

page.

4. To increase the size of an existing file, increase the value in the

column

for the file. You must increase the size of the database by at least 1 megabyte.

5. To increase the size of the database by adding a new file, select

and then enter the

values for the new file. For more information, see

Add Data or Log Files to a Database.

6. Select.

1. Connect to the Database Engine.

2. From the Standard bar, select.

3. Copy and paste the following example into the query window and select.

```sql
BACKUP
ALTER
```
