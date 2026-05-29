---
title: "View"
topic: "collation"
description: |
  Article
  
  •
  
  05/12/2023
  
  Applies to:
  
  SQL Server
  
  This article explains how to view a SQL Server database snapshot using SQL Server
  
  Management Studio.
  
  1. In Object Explorer, connect to the instance o
tags:
  - "collation"
  - "view"
pubDate: 2025-12-01
---

Article

•

05/12/2023

Applies to:

SQL Server

This article explains how to view a SQL Server database snapshot using SQL Server

Management Studio.

1. In Object Explorer, connect to the instance of the SQL Server Database Engine and then

expand that instance.

2. Expand

3. Expand

, and select the snapshot you want to view.

1. Connect to the Database Engine.

2. From the

bar, select

.

3. To list the database snapshots of the instance of SQL Server, query the

column of the

sys.databases

catalog view for non-NULL values.

4. You can also use this query to get details about the database snapshot and its files

SQL

７

Note

To create, revert to, or delete a database snapshot, you must use Transact-SQL.

```sql
source_database_id
SELECT
db_name(db.source_database_id) source_database,
db.name
AS
snapshot_db_name,
db.database_id,
db.source_database_id,
db.create_date,
```