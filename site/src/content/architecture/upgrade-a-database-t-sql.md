---
title: "Upgrade a Database (T-SQL)"
topic: "collation"
description: |
  Article

  •

  03/03/2023

  Applies to:

  SQL Server

  This topic describes how to use detach and attach operations to upgrade a database in SQL

  Server. After being attached to SQL Server, the database is
tags:
  - "collation"
  - "upgrade-a-database-t-sql"
pubDate: 2025-12-01
---

Article

•

03/03/2023

Applies to:

SQL Server

This topic describes how to use detach and attach operations to upgrade a database in SQL

Server. After being attached to SQL Server, the database is available immediately and is

automatically upgraded. This prevents the database from being used with an older version of

the Database Engine. However, metadata upgrade does not affect the

database compatibility

level

setting of a database. See more information in

Database Compatibility Level After

Upgrade

later in this topic.

Limitations and Restrictions

Recommendations

Using detach and attach operations

After Upgrading a SQL Server Database

The system databases cannot be attached.

Attach and detach disable cross-database ownership chaining for the database by setting

its

option to 0. For information about enabling chaining,

see

cross db ownership chaining Server Configuration Option

.

When attaching a replicated database that was copied instead of detached:

If you attach the database to an upgraded version of the same server instance, you

must execute

to upgrade replication after the attach
