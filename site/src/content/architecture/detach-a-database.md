---
title: "Detach a Database"
topic: "collation"
description: "This article describes how to detach a database in SQL Server with SQL Server Management Studio or Transact-SQL."
tags: ["collation","detach-a-database"]
pubDate: "2025-12-01"
---

This article describes how to detach a database in SQL Server with SQL Server Management

Studio or Transact-SQL. The detached files aren't deleted and remain in the file system. The

files can be reattached by using

or

option. The files can also be moved to another server and attached to an instance with the

same or newer version.

For a list of limitations and restrictions, see

Database detach and attach (SQL Server).

Requires membership in the

fixed database role.

If you're moving a database, before you detach it from its existing SQL Server instance, use the

page to review the files associated with the database and their current

locations.

1. In SQL Server Management Studio Object Explorer, connect to the instance of the SQL

Server Database Engine and then expand the instance.

2. Expand

, and select the name of the user database you want to detach.

3. Right-click the database name, select. Select the

page and review the

entries in the

table.

Be sure to account for all files associated with the database before you detach, move, and

attach. Then, proceed with the detach steps in the next section. For more information on

attaching the database in its new location, see

Attach a Database.

```sql
CREATE DATABASE. FOR ATTACH
FOR ATTACH_REBUILD_LOG
```
