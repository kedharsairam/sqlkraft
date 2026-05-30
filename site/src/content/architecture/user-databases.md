---
title: "User Databases"
topic: "collation"
description: |
  Article

  •

  11/25/2024

  Applies to:

  SQL Server

  In SQL Server, you can move the data, log, and full-text catalog files of a user database to a

  new location by specifying the new file location in the
tags:
  - "collation"
  - "user-databases"
pubDate: 2025-12-01
---

Article

•

11/25/2024

Applies to:

SQL Server

In SQL Server, you can move the data, log, and full-text catalog files of a user database to a

new location by specifying the new file location in the

clause of the

ALTER DATABASE

statement. This method applies to moving database files within the same instance SQL Server.

To move a database to another instance of SQL Server or to another server, use

backup and

restore

or

detach and attach operations

.

When you move a database onto another server instance, to provide a consistent experience to

users and applications, you might have to recreate some or all the metadata for the database.

For more information, see

Manage Metadata When Making a Database Available on Another

Server

.

Some features of the SQL Server Database Engine change the way that the Database Engine

stores information in the database files. These features are restricted to specific editions of SQL

Server. A database that contains these features can't be moved to an edition of SQL Server that

doesn't support them. Use the

dynamic management view

to list all edition-specific features that are enabled in the current database.

The procedures in this article require the logical name of the database files. To obtain the

name, query the name column in the

sys.master_files

catalog view.

Full-text catalogs are integrated into the database rather than being stored in the file system.

The full-text catalogs move automatically when you move a database.

７

Note

This article covers moving user database files. For moving system database files, see

.

７

Note

Make sure the service account for the

has permissions to the new file location in the file system. For more

information, see

.

```sql
FILENAME sys.dm_db_persisted_sku_features
```
