---
title: "Grant permissions"
topic: "spatial-data"
description: |
  Applies to:

  SQL Server

  Azure SQL Database

  Azure SQL Managed Instance

  Azure Synapse Analytics

  Analytics Platform System (PDW)

  SQL database in Microsoft

  Fabric

  This article describes how to gran
tags:
  - "spatial-data"
  - "grant-permissions"
pubDate: 2025-12-01
---

SQL Server

Azure SQL Database

Azure SQL Managed Instance

Azure Synapse Analytics

Analytics Platform System (PDW)

SQL database in Microsoft

Fabric

This article describes how to grant permissions on a stored procedure by using SQL Server

Management Studio or Transact-SQL. Permissions can be granted to an existing user, database

role, or application role in the database.

You can't use SQL Server Management Studio to grant permissions on system procedures

or system functions. Use

GRANT object permissions (Transact-SQL)

instead.

The grantor (or the principal specified with the

option) must have either the permission

itself with

, or a higher permission that implies the permission being granted.

Requires

permission on the schema to which the procedure belongs, or

permission on the procedure. For more information, see

GRANT object permissions (Transact-

SQL).

1. In

, connect to an instance of Database Engine and then expand that

instance.

2. Expand

, expand the database in which the procedure belongs, and then

expand.

3. Expand

, right-click the procedure to grant permissions on, and then

select.

4. From

, select the

page.

5. To grant permissions to a user, database role, or application role, select.

6. In

, select

to add or clear the users and roles you want.

```sql
AS
GRANT OPTION
ALTER
CONTROL
```
