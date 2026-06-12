---
title: "Migrate to a partially contained database"
topic: "collation"
description: |
  Article

  •

  02/28/2023

  Applies to:

  SQL Server

  This topic discusses how to prepare to change to the partially contained database model and

  then provides the migration steps.

  Preparing to Migrate a
tags:
  - "collation"
  - "migrate-to-a-partially-contained-database"
pubDate: 2025-12-01
---

Article

•

02/28/2023

SQL Server

This topic discusses how to prepare to change to the partially contained database model and

then provides the migration steps.

Preparing to Migrate a Database

Enable Contained Databases

Converting a Database to Partially Contained

Migrating Users to Contained Database Users

Review the following items when considering migrating a database to the partially contained

database model.

You should understand the partially contained database model. For more information, see

Contained Databases.

You should understand risks that are unique to partially contained databases. For more

information, see

Security Best Practices with Contained Databases.

Contained databases do not support replication, change data capture, or change tracking.

Confirm the database does not use these features.

Review the list of database features that are modified for partially contained databases.

For more information, see

Modified Features (Contained Database).

Query

sys.dm_db_uncontained_entities (Transact-SQL)

to find uncontained objects or

features in the database. For more information, see.

Monitor the

XEvent to see when uncontained features are

used.
