---
title: "View the dependencies"
topic: "tables"
description: "2016 (13.x) and later versions Azure SQL Managed Instance You"
tags: ["tables","view-the-dependencies"]
pubDate: "2025-12-01"
---

2016 (13.x) and later versions

Azure

SQL Managed Instance

Analytics Platform System (PDW)

You can view a table's dependencies in SQL Server Database Engine, using SQL Server

Management Studio or Transact-SQL.

Requires

permission on the database and

permission on

for the database. By default,

permission is granted

only to members of the

fixed database role. When

and

permissions are granted to another user, the grantee can view all dependencies in the

database.

1. In

, expand

, expand a database, and then expand.

2. Right-click a table, and then select.

3. In the

<object name>

dialog box, select either

<object name>

, or

<object name>.

4. Select an object in the

grid. The type of object (such as "Trigger" or

"Stored Procedure"), appears in the

box.

７

Note

Viewing dependencies using

>

isn't supported in. Instead, use. Azure Synapse

Analytics SQL pools support tables, views, filtered statistics, and Transact-SQL stored

procedures entity types from this list. Dependency information is created and maintained

for tables, views, and filtered statistics only.

```sql
VIEW DEFINITION
SELECT sys.sql_expression_dependencies
SELECT
SELECT
VIEW DEFINITION
```
