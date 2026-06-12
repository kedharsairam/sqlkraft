---
title: "Manage metadata"
topic: "collation"
description: |
  Article

  •

  04/15/2024

  Applies to:

  SQL Server

  This article is relevant in the following situations:

  Configuring the availability replicas of an Always On availability groups availability group.

  S
tags:
  - "collation"
  - "manage-metadata"
pubDate: 2025-12-01
---

Article

•

04/15/2024

SQL Server

This article is relevant in the following situations:

Configuring the availability replicas of an Always On availability groups availability group.

Setting up database mirroring for a database.

When preparing to change roles between primary and secondary servers in a log

shipping configuration.

Restoring a database to another server instance.

Attaching a copy of a database on another server instance.

Performing database engine upgrade using the method - migrate to a new installation.

Migrating databases to Azure SQL (Virtual Machine or Managed Instance).

Some applications depend on information, entities, and/or objects that are outside of the

scope of a single user database. Typically, an application has dependencies on the

and

databases, and also on the user database. Anything stored outside of a user database

that is required for the correct functioning of that database must be made available on the

destination server instance. For example, the logins for an application are stored as metadata in

the

database, and they must be re-created on the destination server. If an application

or database maintenance plan depends on SQL Server Agent jobs, whose metadata is stored in

the

database, you must re-create those jobs on the destination server instance. Similarly,

the metadata for a server-level trigger is stored in.

When you move the database for an application to another server instance, you must re-create

all the metadata of the dependent entities and objects in

and

on the destination

server instance. For example, if a database application uses server-level triggers, just attaching

or restoring the database on the new system isn't enough. The database won't work as

expected unless you manually re-create the metadata for those triggers in the

database.

```sql
master msdb master msdb master master msdb master
```
